import pandas as pd

def totalScore(math, sci, eng):
    return math + sci + eng

def avgScore(total):
    return (total) / 3

Scores = {
    "Students": ["Shek", "Shetty", "Lux", "Krrish"],
    "MathS": [37, 76, 98, 45],
    "SciS": [90, 27, 67, 35],
    "EngS": [56, 36, 87, 50],
}

Scores_df = pd.DataFrame(Scores)
Scores_df["ToatlScores"] = totalScore(
    Scores_df["MathS"], Scores_df["SciS"], Scores_df["EngS"]
)
Scores_df["AvgScores"] = avgScore(Scores_df["ToatlScores"])
print()
Scores_df["Result"] = Scores_df["AvgScores"] > 50
print(Scores_df[Scores_df["Result"]])
print('--------------------------------------------------------------')
print(Scores_df)
