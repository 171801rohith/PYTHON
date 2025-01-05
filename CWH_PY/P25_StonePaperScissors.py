# Stone Paper Scissors
import random

def check_winner(user, computer):
    if user == computer:
        return "It's a Tie !! -_-"
    elif (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
        return "You Win !! :)"
    else :
        return "You Lose !! :("

while True:
    user = int(input("Enter your choice:    1. Snake     2. Water    3. Gun   4. Exit : "))
    # computer = int(random.uniform(1, 4))
                #  OR
    computer = random.randint(1, 3)
    if user == 4:
        print("Exiting.....")
        break
    else:
        print("Computer choose ", computer)
        print(check_winner(user, computer))
    
