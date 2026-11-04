def retrieval_metrics(rankings, relevant):
    hits = []
    rr = []
    for ids, good in zip(rankings, relevant):
        ranks = []
        for r, chunk_id in enumerate(ids[:3], 1):
            if chunk_id in good:
                ranks.append(r)
        hits.append(bool(ranks))
        if ranks:
            rr.append(1 / ranks[0])
        else:
            rr.append(0)
    return sum(hits) / len(hits), sum(rr) / len(rr)


rankings = [["a", "b", "c"], ["c", "a", "b"], ["x", "y", "z"]]
relevant = [{"a"}, {"a"}, {"a"}]
hit, mrr = retrieval_metrics(rankings, relevant)
print("Hit@3=" + format(hit, ".3f") + "; MRR@3=" + format(mrr, ".3f"))
assert abs(hit - 2 / 3) < 1e-9 and abs(mrr - 0.5) < 1e-9
print("Metric check passed")
