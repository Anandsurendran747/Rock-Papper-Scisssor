import random

# Snake Water Gun or Rock Paper Scissors
try:
    def gameWin(comp, you):
        # If two values are equal, declare a tie!
        if comp == you:
            return 't'

        # Check for all possibilities when computer chose s
        elif comp == 1:
            if you==2:
                return 'f'
            elif you==3:
                return 'w'
        
        # Check for all possibilities when computer chose w
        elif comp == 2:
            if you==3:
                return 'f'
            elif you==1:
                return 'w'
        
        # Check for all possibilities when computer chose g
        elif comp == 3:
            if you==1:
                return 'f'
            elif you==2:
                return 'w'

    print("Comp Turn: Computer Selected ")
    randNo = random.randint(1, 3) 
    if randNo == 1:
        comp = 1
    elif randNo == 2:
        comp = 2
    elif randNo == 3:
        comp = 3

    you = int(input("Your Turn:Select one:\n Snake(1) Water(2) or Gun(3)?"))
    a = gameWin(comp, you)

    if comp==1 and you==1:
        print(f"Computer chose Snake")
        print(f"You chose Snake")
    elif comp==1 and you==2:
        print(f"Computer chose Snake")
        print(f"You chose Water")
    elif comp==1 and you==3:
        print(f"Computer chose Snake")
        print(f"You chose gun")

    if comp==2 and you==1:
        print(f"Computer chose Water")
        print(f"You chose Snake")
    elif comp==2 and you==2:
        print(f"Computer chose Water")
        print(f"You chose Water")
    elif comp==2 and you==3:
        print(f"Computer chose Water")
        print(f"You chose gun")

    if comp==3 and you==1:
        print(f"Computer chose Gun")
        print(f"You chose Snake")
    elif comp==3 and you==2:
        print(f"Computer chose Gun")
        print(f"You chose Water")
    elif comp==3 and you==3:
        print(f"Computer chose Gun")
        print(f"You chose gun")

    if a =='t':
        print("The game is a tie!")
    elif a=='w':
        print("You Win!")
    elif a=='f':
        print("You Lose!")
    else:
        print('You enterd wrong value')
except Exception as e:
    print('You enterd wrong value')
