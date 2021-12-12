print("\n\n\t####### WELCOME TO SNAKE WATER GUN GAME ##########",
      "\n You have 10 chance Majorty Win the Game")

name=input("Enter your Name : ")

computer_point = 0
user_point = 0

for i in range(0, 10):

    import random
    lst = [["Snake"], ["Water"], ["Gun"]]
    choice = random.choice(lst)
    print("\nYou have", 10-i, "chance left")

    print("\nChoose : \t1 for Snake \t2 for Water \t3 for Gun : ")
    a = int(input("Your Choice : "))
    if a == 1:
        print("You choose Snake")
        print("Computer choose", choice)
        if choice == ["Snake"]:
            print("\tIt's Draw")
            computer_point += 0
            user_point += 0
        elif choice == ["Water"]:
            print(f"\t{name} win the chance")
            user_point += 1
        else:
            print("\t Computer win the chance")
            computer_point += 1
    elif a == 2:
        print("You choose Water")
        print("Computer choose", choice)
        if choice == ["Water"]:
            print("\tIt's Draw")
            computer_point += 0
            user_point += 0
        elif choice == ["Gun"]:
            print(f"\t{name} win the chance")
            user_point += 1
        else:
            print("\t Computer win the chance")
            computer_point += 1
    elif a == 3:
        print("You choose Gun")
        print("Computer choose", choice)
        if choice == ["Gun"]:
            print("\tIt's Draw")
            computer_point += 0
            user_point += 0
        elif choice == ["Snake"]:
            print(f"\t{name} win the chance")
            user_point += 1
        else:
            print("\t Computer win the chance")
            computer_point += 1
    else:
        print("\tWRONG ENTRY!!!!!!!!!")
    print(f"{name} Score :", user_point, "\tComputer Score :", computer_point)


if user_point == computer_point:
    print("Its Draw.......")
elif user_point > computer_point:
    print(f"$$$$$$$$ {name} WIN THE GAME $$$$$$$")
else:
    print("$$$$$$$$ COMPUTER WIN THE GAME $$$$$$$$$$")
