import csv
from csv import writer

def print_menu_options(name: str):
    print("Hi, " + name + ". Please select an option.")
    print("1. Add a result")
    print("2. What games do I have?")
    print("3. Search for results according to game type.")
    print("4. Search for results according to winner.")
    option = input("Selection: ")
    return option

def add_result(name):
    print("Let's record this game " + name +".")
    game_name = input("GAME? ") # make a list here
    winner = input("WINNER? ")
    players = input("PLAYERS? ") 
    date = input("DATE? ")
    notes = input("Any extra notes? ")
    add_game_list = [game_name, winner, players, name, date, notes]
    write_file(add_game_list)

def add_game_type(name: str): 
    count = 0
    for n in games_list:
        count += 1
        print(str(count) + ". " + n)


def read_file(filename):
    file = open('bg_stats.csv')
    type(file)
    csvreader = csv.reader(file)

    header = []
    header = next(csvreader)
    print(header)
    header
    rows = []
    for row in csvreader:
        rows.append(row)
        print(row)
    rows
    file.close()

def write_file(add_game: list):
    with open('bg_stats.csv', 'a', newline='') as f_object:  
    # Pass the CSV  file object to the writer() function
        writer_object = writer(f_object)
        # Result - a writer object
        # Pass the data in the list as an argument into the writerow() function
        writer_object.writerow(add_game)  
        # Close the file object
        f_object.close()
    print("Game has been added!")
    print(add_game)

def search_for_game(name: str):
    game = input("What game results are you looking for?")
    reader = csv.reader(open('bg_stats.csv', 'r'))
    count = 0
    for data in reader:
        #list index start from 0, thus 2938 is in data[1]
        if data[0] == game:
            count += 1
            print("Game: " + str(count))
            print("Game: " + data[0])
            print("Winner: " + data[1])
            print("Other players: " + data[2])
            print("Added by: " + data[3])
            print("Date: " + data[4])
            print("")

def search_for_winner(name: str):
    winner = input("What winner are you looking for?")
    reader = csv.reader(open('bg_stats.csv', 'r'))
    count = 0
    for winner in reader:
        #list index start from 0, thus 2938 is in data[1]
        if data[1] == winner:
            count += 1
            print("Game: " + str(count))
            print("Game: " + data[0])
            print("Winner: " + data[1])
            print("Other players: " + data[2])
            print("Added by: " + data[3])
            print("Date: " + data[4])
            print("")


menu_dictionary = {"1": add_result, "2": add_game_type, "3": search_for_game, "4": search_for_winner}
app_active = True
games_list = ["Catan", "Exploding Kittens", "Bananagrams", "30 Seconds", "Chameleon", "Agatha Christie's Death on the Cards", "Azul", "MicroMacro", "Aboretum", "A fake artist goes to New York", "Unstable Unicorns", "other"]


print("Welcome to Rebecca's board game tracker")
name = input("User?")

while app_active:
    option = print_menu_options(name)
    menu_dictionary[option](name)
    print(" ")
    repeat = input("Would you like to make another request? Y/N: ")
    if (repeat == 'N') or (repeat == 'n'):
        app_active = False

print("Have a great day")

