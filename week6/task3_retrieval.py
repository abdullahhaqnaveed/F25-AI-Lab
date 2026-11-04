import csv
import json
import time

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from task2_chunks import make_chunks

try:
    from sentence_transformers import SentenceTransformer
    HAVE_MODEL = True
except ImportError:
    HAVE_MODEL = False


def evaluate(scores, chunks, items):
    hits = []
    reciprocal = []
    for row, q in zip(scores, items):
        if q["doc"] is None:
            continue
        top = np.argsort(-row, kind="stable")[:3]
        good = []
        for rank, i in enumerate(top, 1):
            if chunks[i]["doc"] == q["doc"] and q["evidence"] in chunks[i]["text"]:
                good.append(rank)
        hits.append(bool(good))
        if good:
            reciprocal.append(1 / good[0])
        else:
            reciprocal.append(0)
    if not hits:
        return None, None
    return float(np.mean(hits)), float(np.mean(reciprocal))


def main():
    with open("corpus.json", encoding="utf-8") as f:
        docs = json.load(f)
    with open("queries.json", encoding="utf-8") as f:
        items = json.load(f)

    model = None
    if HAVE_MODEL:
        t = time.perf_counter()
        model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2", device="cpu")
        print("Model load seconds:", round(time.perf_counter() - t, 2))
        print("Model max token length:", model.max_seq_length)
    else:
        print("Sentence model not available. Embedding runs are skipped.")
        print("TF-IDF results below are real. Embedding results are not claimed.")

    query_texts = [q["query"] for q in items]
    logs = []
    results = {}
    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(docs, strategy)
        texts = [c["text"] for c in chunks]
        methods = ["tfidf"]
        if HAVE_MODEL:
            methods.append("embedding")
        for method in methods:
            t = time.perf_counter()
            if method == "tfidf":
                vectorizer = TfidfVectorizer()
                C = vectorizer.fit_transform(texts)
                Q = vectorizer.transform(query_texts)
            else:
                lengths = []
                for text in texts + query_texts:
                    ids = model.tokenizer(text, truncation=False)["input_ids"]
                    lengths.append(len(ids))
                print(strategy, "max token length:", max(lengths),
                      "limit:", model.max_seq_length)
                if max(lengths) > model.max_seq_length:
                    raise ValueError("Model limit exceeded")
                C = model.encode(texts, normalize_embeddings=True)
                Q = model.encode(query_texts, normalize_embeddings=True)
            encode_seconds = time.perf_counter() - t
            t = time.perf_counter()
            if method == "tfidf":
                scores = (Q @ C.T).toarray()
            else:
                scores = Q @ C.T
            search_seconds = time.perf_counter() - t
            for split in ["dev", "test"]:
                indices = [i for i, q in enumerate(items) if q["split"] == split]
                result = evaluate(scores[indices], chunks,
                                  [items[i] for i in indices])
                results[(strategy, method, split)] = result
                print(strategy, method, split, "Hit/MRR:", result,
                      "chunks:", len(chunks),
                      "encode seconds:", round(encode_seconds, 2),
                      "search seconds:", round(search_seconds, 4))
            for row, q in zip(scores, items):
                for rank, i in enumerate(np.argsort(-row, kind="stable")[:3], 1):
                    c = chunks[i]
                    record = {"strategy": strategy, "method": method,
                              "query": q["query"], "split": q["split"],
                              "rank": rank, "score": float(row[i]),
                              "chunk_id": c["id"], "doc": c["doc"],
                              "start": c["start"], "end": c["end"],
                              "text": c["text"],
                              "answerable": q["doc"] is not None}
                    logs.append(record)
                    print(strategy, method, "top", rank, "for:", q["query"][:45],
                          "->", c["id"], "score:", round(float(row[i]), 3),
                          "chars:", c["start"], c["end"])

    print()
    print("Failures (answerable queries with no relevant chunk in top 3):")
    failures = 0
    for q in items:
        if q["doc"] is None:
            continue
        for strategy in ["0", "10", "sentence"]:
            for method in (["tfidf"] + (["embedding"] if HAVE_MODEL else [])):
                found = False
                for record in logs:
                    if (record["strategy"] == strategy
                            and record["method"] == method
                            and record["query"] == q["query"]
                            and record["doc"] == q["doc"]
                            and q["evidence"] in record["text"]):
                        found = True
                if not found:
                    failures += 1
                    print(strategy, method, "missed:", q["query"])
    if failures == 0:
        print("No failures: every answerable query had a relevant chunk in top 3.")
    print()
    print("Unanswerable queries still return ranked text, but with no relevant evidence:")
    for q in items:
        if q["doc"] is None:
            print("Unanswerable:", q["query"])

    with open("retrieval_log.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(logs[0]))
        writer.writeheader()
        writer.writerows(logs)
    print("Wrote retrieval_log.csv with", len(logs), "rows")

    print()
    print("Development results (used to pick the strategy):")
    best = None
    for strategy in ["0", "10", "sentence"]:
        for method in (["tfidf"] + (["embedding"] if HAVE_MODEL else [])):
            hit, mrr = results[(strategy, method, "dev")]
            print(strategy, method, "dev Hit:", hit, "MRR:", mrr)
            score = (hit, mrr, 1 if method == "embedding" else 0)
            if best is None or score > best[0]:
                best = (score, strategy, method, hit, mrr)
    print("Picked strategy and method:", best[1], best[2],
          "with dev Hit:", best[3], "MRR:", best[4])
    print("Held-out test results for the picked setup:",
          results[(best[1], best[2], "test")])


if __name__ == "__main__":
    main()
