# Create game introduction 
def battle_intro():
    print("----------Welcome to BattleScrabble!----------")
    name = input("What's your name? \n")
    age = int(input("What's your age: \n"))
    if age >= 18:
        print("You are eligible to enter the battlefield.")
    else:
        print(f"Hello {name.capitalize()}, you are too young to play this game.")

def enter_battle_perimeter():
    print("YOU ARE ENTERING THE BATTLE PERIMETER!\n")

def main():
    battle_intro()


if __name__ == '__main__':
    main()