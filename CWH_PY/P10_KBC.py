# Create a list to store questions and correct answers
# Display the amount won

questions = ["20 * 9", "Iron Man alias", "Deadpool release year", "Google CEO"]
option = [
    ["100", "180", "287"],
    ["TONY STARK", "THOR", "STEVE ROGERS"],
    ["2024", "2016", "2017"],
    ["Sunder Pichai", "Mukesh Ambani", "Bill Gates"]
]
answer = ["180", "TONY STARK", "2017", "Sunder Pichai"]
winCount = 0
for i in range(len(questions)):
    print(i + 1, ") ", questions[i], sep="")
    for j in range(0, len(option[i])):
        print(j + 1, ": ", option[i][j], sep="", end="       ")
    print()
    userOp = int(input("Enter your option : "))
    userAns = option[i][userOp-1]
    if userAns in answer:
        winCount += 1
    else:
        break

if winCount != 0:
    amount = 100 * winCount
    print("You won :) $", amount)
else:
    print("You lost :(")
