# Create a list to store questions and correct answers
# Display the amount won

ques_ans = {
    "20 * 9": "180",
    "Iron Man alias": "TONY STARK",
    "Deadpool release year": "2017",
    "Google CEO": "Sunder Pichai",
}

option = [
    ["100", "180", "287"],
    ["TONY STARK", "THOR", "STEVE ROGERS"],
    ["2024", "2016", "2017"],
    ["Sunder Pichai", "Mukesh Ambani", "Bill Gates"],
]

winCount = 0
i = 0
for key in ques_ans:
    print(i + 1, ") ", key, sep="")
    for j in range(0, len(option[i])):
        print(j + 1, ": ", option[i][j], sep="", end="       ")
    print()
    userOp = int(input("Enter your option : "))
    userAns = option[i][userOp - 1]
    if userAns == ques_ans[key]:
        i += 1
        winCount += 1
    else:
        break

if winCount != 0:
    amount = 100 * winCount
    print("You won :) $", amount)
else:
    print("You lost :(")
