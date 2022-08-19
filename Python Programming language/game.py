money = int(input("How much money do you want?"))
import random
i = 1

while i == 1:
    print("Welcome to Dice Rolling Guessing Game")
    print(" ")
    print("Your balance ", money)
    print(" ")
    bet = int(input("How much money do you want to bet?"))
    print(" ")
    choice1 = input("Will the number be even or odd?")
    dice = random.randint(1,6)
    choice1.lower()
    def gamewin(money,bet):
        print("You win!")
        bet = bet * 2
        money = money + bet
        bet = 0
    def gamelose(money,bet):
        print("You lost!")
        bet = 0
    if dice % 2 == 0 and choice1 == "even":
        gamewin(money,bet)
        choice2 = input("Do you want to play again?")
        choice2.lower()
        if choice2 == "yes":
            continue
        else:
            print("Thank you for playing!")
            print("Your balance ", money)
            break
    if dice % 2 == 0 and choice1 == "odd":
        gamelose(money,bet)
        choice2 = input("Do you want to play again?")
        choice2.lower()
        if choice2 == "yes":
            continue
        else:
            print("Thank you for playing!")
            print("Your balance ", money)
            break
    if dice % 2 == 1 and choice1 == "odd":
        gamewin(money,bet)
        choice2 = input("Do you want to play again?")
        choice2.lower()
        if choice2 == "yes":
            continue
        else:
            print("Thank you for playing!")
            print("Your balance ", money)
            break
    if dice % 2 == 1 and choice1 == "even":
        gamelose(money,bet)
        choice2 = input("Do you want to play again?")
        choice2.lower()
        if choice2 == "yes":
            continue
        else:
            print("Thank you for playing!")
            print("Your balance ", money)
            break