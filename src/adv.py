from room import Room
from player import Player
from item import Item
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


item = {
    'coins':  Item("Item: ~~[Money", "--Just a few lose coins to take to the tavern]~~"),
    'tools':  Item("Item: ~~[Grappling hook", "--This might come in handy. It is very heavy]~~"),
    'jewel': Item("Item: ~~[Gem", "--Next time you ask that stranger for information. He might be willing to help for this type of payment]~~"),
    'torch': Item("Item: ~~[Torch", "--Let there be light. Is someone sneaking around? Why is this on the floor?!?]~~"),
    'medallion': Item("Item: ~~[Medallion", "--It reflects light and glows slightly orange it may be magical. There is an inscription in an unknown language. Inscription:Hul werud ezes ulud egembelu owog. Kyul buol engumet ullyetuk.]~~ "),
}



# room['foyer'].items = [str(item['coins'])]
room['overlook'].items = [str(item['medallion'])]
room['narrow'].items = [str(item['jewel'])]
room['treasure'].items = [str(item['tools'])]

options = "\nOptions:\nInventory:[View]\nItem:[Take][Drop]\nDirections:[N][S][E][W]\nSystem:[Q] to Quit\n\n"
directions={"n", "s", "e", "w"}
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def game():
    name = 'Word Game'
    player = Player(name, room['outside'])
    print(f'\nYou are playing a word game.')
    
    user_input = input(f'\nTo play game press "P" or to quit game press "Q": ')
    
    if user_input == "p":
        print(f'\nYou are in {player.current_room.name}. {player.current_room.description}')
    elif user_input != 'p':
        print(f'Thanks for playing.')
    
    while user_input == 'p':
        choice = input("Please choose an option: \n(n) North   (s) South \n(e) East   (w) West\n").lower().strip()
        if choice in directions:
            player.move(choice)
        elif choice == 'h':
            print(f"{options}")
        elif choice == 'q':
            print(f"\nThanks for Playing! GoodBye Adventurer {player.name}!")
            sys.exit()

game()