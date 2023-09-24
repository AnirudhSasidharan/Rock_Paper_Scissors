import random

p=0
c=0
while True:
    choices=["rock","paper","scissors"]
    player=None

    computer=random.choice(choices)
    while player not in choices:
        player=input("rock,paper or scissors:").lower()
    
    if player==computer:
        print("Computer:",computer)
        print("Player:",player)
        print("\n\t   Tied")
    elif player=="rock":
        if computer=="paper":
            print("Computer:",computer)
            print("Player:",player)
            print("\n\t Player Wins")
            p+=1
        if computer=="scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("\n\t Computer Wins")
            c+=1
    elif player=="paper":
        if computer=="rock":
            print("Computer:",computer)
            print("Player:",player)
            print("\n\t Player Wins")
            p+=1
        if computer=="scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("\n\t Computer Wins")
            c+=1
    elif player=="scissors":
        if computer=="rock":
            print("Computer:",computer)
            print("Player:",player)
            print("\n\t Computer Wins")
            c+=1
        if computer=="scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("\n\t Player Wins")
            p+=1
    print("\n-----------POINTS-----------\ncomputer = "+str(c)+"\tplayer = "+str(p))
    if p==5:
        print("\t***YOU WON THE SERIES***")
        break
    elif c==5:
        print("\t\n*** YOU LOST THE SERIES :( ***)")
        break
    Play_again=input("Do you want to play again?(Y/N):")
    if Play_again.upper()=="N":
        break



       