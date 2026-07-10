print("-------------WELCOME TO THE TREASURE ISLAND-------------")
choice1 = input("Enter the way you have two ways left right or left:").lower()

if choice1 == 'left':
    print("There is a waterflow in front of you")
    choice2 = input("is you will swim or wait:").lower()

    if choice2 == 'wait':
        print("The waterflow was gone you can see the doors right there")
        choice3 = input("You would like to open which door is Red or Green or yellow:").lower()

        if choice3 == 'red':
            print("Game Over")
        elif choice3 == 'blue':
            print("Game Over")
        else:
            print("-------------You Won-------------")

    else:
        print("Game Over")
else:
    print("There is hole right here you were fallen in that hole")
    print("Game Over")
