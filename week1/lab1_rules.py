def check(score, complete, fee_clear, form_signed):
    if complete and score >= 70 and fee_clear and form_signed:
        return "Review"
    return "Hold"


cases = [
    ("pass_all", 82, True, True, True, "Review", "all four conditions pass"),
    ("fee_not_clear", 85, True, False, True, "Hold", "fee clear condition fails"),
    ("form_not_signed", 88, True, True, False, "Hold", "form signed condition fails"),
    ("boundary_score", 70, True, True, True, "Review", "score is exactly on the threshold 70"),
]

print("case | score | complete | fee_clear | form_signed | expected | actual | reason")
for name, score, complete, fee_clear, form_signed, expected, reason in cases:
    result = check(score, complete, fee_clear, form_signed)
    print(name, score, complete, fee_clear, form_signed, expected, result, reason, sep=" | ")
