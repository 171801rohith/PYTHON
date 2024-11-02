# Lab
# 1. Define a list of students, each with their scores in Math,  Science and English
# 2. Store data in dictionary format
# 3. Write function to calculate total score of each student
# 4. Write another func to avgerage 
# 5. Convert dictionary to dataframe
# 6. Add a new col to df for a. total score of each student, b. average of each student, c. Pass or fail
# 7. filter out pass and fail
# 8. Display the complete dataframe with grades

import pandas as pd


Scores = {
    "Students": ["Shek", "Shetty", "Lux", "Krrish"],
    "MathS": [37, 76, 98, 45],
    "SciS": [90, 27, 67, 35],
    "EngS": [56, 36, 87, 50],
}


def totalScore(math, sci, eng):
    return math + sci + eng


def avgScore(total):
    return (total) / 3


def status(avg):
    if avg > 50:
        return "Pass"
    else:
        return "Fail"


Scores_df = pd.DataFrame(Scores)

Scores_df["ToatlScores"] = totalScore(
    Scores_df["MathS"], Scores_df["SciS"], Scores_df["EngS"]
)

Scores_df["AvgScores"] = avgScore(Scores_df["ToatlScores"])

Result = []
for i in range(len(Scores_df)):
    Result.append(status(Scores_df["AvgScores"][i]))
Scores_df["Result"] = Result

grades = []
for i in range(len(Scores_df)):
    if Scores_df["AvgScores"][i] >= 80:
        grades.append("A")
    elif Scores_df["AvgScores"][i] >= 70:
        grades.append("B")
    elif Scores_df["AvgScores"][i] >= 60:
        grades.append("C")
    else:
        grades.append("D")

Scores_df["Grades"] = grades

print()
print(Scores_df[Scores_df["Result"] == "Pass"])
print('--------------------------------------------------------------------')
print(Scores_df[Scores_df["Result"] == "Fail"])
print('--------------------------------------------------------------------')
print(Scores_df)
