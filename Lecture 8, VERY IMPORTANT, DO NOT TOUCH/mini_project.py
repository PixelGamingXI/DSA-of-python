import random

target = random.randint(1,100)

while True:
    user = int(input("Guess a number between 1-100:"))

    if(user == target):
        print("You won the game!!!")
        break
    elif(user < target):
        print("Wrong guess! Guess a bigger number:")

    else:
        print("Wrong guess! Guess a smaller number:")

print("---GAME OVER---")
