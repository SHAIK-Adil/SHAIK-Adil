import random
while True:
    player = input("Rock, Paper, Scissors? : ")
    computer = random.choice(['Rock', 'Paper', 'Scissors'])

    if player == computer:
        print("Tie.....!!!! po ra beppam")
    elif player == "Rock":
        if computer == "Paper":
            print("you loose!!!", computer, "covers", player)
        else:
            print("you win!!!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("you loose!!!", computer, "cut",player)
        else:
            print("you win!!!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("you win!!!", computer, "smashes", player)
        else:
            print("you loose!!!", player, "cut", computer)
    else:
        print("check your spelling`!!")