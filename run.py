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

def create_grid():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions
    global linked_words

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1
            linked_word = get_random_word(ship_size)
            linked_words.append({'row': random_row, 'col': random_col, 'word': linked_word})


def print_grid():
    """Will print the grid with rows A-J and columns 0-9"""
    global grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")
    

def main():
    battle_intro()
    enter_battle_perimeter()


if __name__ == '__main__':
    main()