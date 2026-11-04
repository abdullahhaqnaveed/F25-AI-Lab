import json
import re


def word_spans(text):
    return [(m.start(), m.end()) for m in re.finditer(r"\S+", text)]


def windows(text, size=40, overlap=10, offset=0):
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("Require size > 0 and 0 <= overlap < size")
    spans = word_spans(text)
    result = []
    for i in range(0, len(spans), size - overlap):
        j = min(i + size, len(spans))
        result.append((offset + spans[i][0], offset + spans[j - 1][1]))
        if j == len(spans):
            break
    return result


def sentence_chunks(text, size=40):
    if size <= 0:
        raise ValueError("size must be positive")
    cuts = [0]
    for m in re.finditer(r"[.!?]\s+", text):
        cuts.append(m.end())
    cuts.append(len(text))
    out = []
    pending = None
    count = 0
    for a, b in zip(cuts, cuts[1:]):
        segment = text[a:b]
        n = len(segment.split())
        if n == 0:
            continue
        if n > size:
            if pending is not None:
                out.append(pending)
            out.extend(windows(segment, size, 0, a))
            pending = None
            count = 0
        elif pending is not None and count + n <= size:
            pending = (pending[0], b)
            count = count + n
        else:
            if pending is not None:
                out.append(pending)
            pending = (a, b)
            count = n
    if pending is not None:
        out.append(pending)
    return out


def make_chunks(docs, strategy):
    result = []
    for doc_id, text in docs.items():
        if strategy == "sentence":
            spans = sentence_chunks(text)
        else:
            spans = windows(text, 40, int(strategy))
        for i, (a, b) in enumerate(spans):
            result.append({"id": doc_id + ":" + str(i), "doc": doc_id,
                           "start": a, "end": b, "text": text[a:b]})
    return result


if __name__ == "__main__":
    print("Empty text:", windows(""))
    print("Short text:", windows("short text"))
    try:
        windows("a b", 2, 2)
        print("ERROR: invalid overlap was accepted")
    except ValueError:
        print("Invalid overlap rejected")
    long = " ".join(["word"] * 95) + "."
    print("Long sentence chunks:", len(sentence_chunks(long)), "chunks, each under 40 words:",
          all(len(long[a:b].split()) <= 40 for a, b in sentence_chunks(long)))

    with open("corpus.json", encoding="utf-8") as f:
        docs = json.load(f)
    with open("queries.json", encoding="utf-8") as f:
        queries = json.load(f)

    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(docs, strategy)
        total_words = 0
        for c in chunks:
            total_words = total_words + len(c["text"].split())
        original_words = 0
        for text in docs.values():
            original_words = original_words + len(text.split())
        print(strategy, "chunks:", len(chunks),
              "total words:", total_words,
              "original words:", original_words,
              "repeated words:", total_words - original_words)

    for q in queries:
        if q["doc"] is None:
            continue
        for strategy in ["0", "10", "sentence"]:
            chunks = make_chunks(docs, strategy)
            found = False
            for c in chunks:
                if c["doc"] == q["doc"] and q["evidence"] in c["text"]:
                    found = True
            print(q["query"][:40], strategy, "evidence in one chunk:", found)
