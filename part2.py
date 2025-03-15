import random
def num_game():
    no1=int(input("Enter start point: "))
    no2=int(input("Enter end point: "))

    while True:
        user=int(input(f"guess a number from {no1} to {no2} : "))

        random_num=random.randint(no1,no2)
        if user not in range(no1,no2+1):
            print("Number out of range!  ")
            break

        if user==(random_num):
            print("Correct!!" )
            break
        elif user<random_num:
            print("too low ")

        elif user>random_num:
            print("Too high! ")
        else:
            print("Invalid choice! ")
            break


def rock_paper():
    options = ("rock","paper","scissor")
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("enter a choice (rock, paper, scissors): ")


    print(f"player: {player}")
    print(f"computer: {computer}")

    if player == computer:
        print("it is draw")

    elif player == "rock" and computer == "scissors":
        print("you win")

    elif player == "paper" and computer == "rock":
        print("you win")

    elif player == "scissors" and computer == "paper":
        print("you win")

    else:
        print("you lose")

while(True):
    print("""Welcome to game!
    1.guess number game
    2.rock paper scissor game
    3.exit
          """)
    player=int(input("Enter your choice"))
    if player==1:
        num_game()
    elif player==2:
        rock_paper()
    elif player==3:
        print("Exited the program!")
        break
    else:
        print("invalid choice")