import random
game_list = ['Rock' , 'Paper' , 'Scissor']
computer = c = 0
commmand = p = 0
print("Sccore : Computer" + str(c) + "  player  " + str(p))
# loop begins
run = True
while run :
    computer_choice = random.choice(game_list)
    command = input("Rock , Paper , Scissor or Quit: ")
    if command == computer_choice:
        print("tie")
    elif command == 'Rock' :
        if computer_choice == 'Scissor':
            print("player win !!")
            p += 1
        else:
            print("computer won !!")
            c += 1
    elif command == 'Paper':
        if command == 'Rock':
            print("player won!!")
            p += 1
        else:
            print("computer won !!!")
            c += 1
    elif command == 'Scissor':
        if computer_choice == "Paper":
            print("PLAYER won!!!")
            p += 1
        else :
            print("computer won ")
            c += 1
    elif command == 'Quit':
        break
    else:
        print("wrong command")
    print("player : "+ command )
    print("computer : "+ computer_choice)
    print("")
    print("Score computer  " + str(c) +"  player  " + str(p))
    print("")

