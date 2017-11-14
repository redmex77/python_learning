#!/usr/bin/python3.6

def mainMenu():
    print("1. Menu option 1")
    print("2. Menu option 2")
    print("3. Exit")
    selection = int(input("Choose an option: "))

    if selection==1:
        option1()
    elif selection==2:
        option2()
    elif selection==3:
        exit
    else:
        print("Invalid choice. Choose 1-3 ")
        mainMenu()

def option1():
    print("Option 1")
    anykey = input("Press anykey to return to menu")
    mainMenu()

def option2():
    print("Option 2")
    anykey = input("Press anykey to return to menu")
    mainMenu()

mainMenu()
