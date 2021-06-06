
from Board import pause


class Player:

    def __init__(self, name, symbol, level=0):
        self.name = name
        self.symbol = symbol
        self.level = level
# This class defines a Player to have a name and a symbol


player2_computer_names = [
    "bot", "a bot", "the bot", "robot", "the robot", "a robot", "computer", "the computer", "a computer", "c", "comp",
    "you", "mac", "the mac",
]

player2_human_names = [
    "friend", "f", "my friend", "a friend", "my fiance", "fiance", "stryker", "sarah", "wife",
    "husband", "my wife", "my husband", "my hubby", "hubby", "wifey"
]


def define_player_symbol():
    pause()
    print("\nWould you like to be X's or O's?")
    while True:
        player_symbol = input("> ")
        if player_symbol.lower() in ["x", "x's", "xs", "x's please", "x's pls", "xs please", "xs pls"]:
            return "X"
        elif player_symbol.lower() in ["o", "o's", "os", "o's please", "o's pls", "os please", "os pls"]:
            return "O"
        elif player_symbol.lower() == "quit":
            return "quit"
        else:
            print("Please enter X, O, or 'quit'.")
# This function asks whether someone would like to be X or O, and returns X or O as a str


def define_players():
    pause()
    print("\nHello! Welcome to Tic-Tac-Toe!")
    pause()
    print('You can type "quit" any time to quit the game.')
    pause()
    print("\nWhat's your name?")
    response = input("> ")
    if response.lower() == "quit":
        return ""  # Might need to change this return str to a list
    else:
        player1 = Player(response, define_player_symbol())
        if player1.symbol == "quit":
            return ""  # ***See above
        else:
            pause()
            print("\nAnd would you like to play against the computer or a friend?")
            while True:
                player2 = input("> ")
                if player2.lower() == "quit":
                    return ""  # ***See above
                elif player2.lower() in player2_computer_names:
                    pause()
                    print("\nGreat! And do you want to play against the Easy, Medium, or Hard computer?")
                    while True:
                        computer_level = input("> ")
                        if computer_level.lower() in ["easy", "e", "ez", "e-z", "1"]:
                            player2 = Player("The Computer", "X" if player1.symbol == "O" else "0", 1)
                        elif computer_level.lower() in ["medium", "med", "m", "2"]:
                            player2 = Player("The Computer", "X" if player1.symbol == "O" else "0", 2)
                        elif computer_level.lower() in ["hard", "hrd", "h", "3"]:
                            player2 = Player("The Computer", "X" if player1.symbol == "O" else "0", 3)
                        pause()
                        print(f"\nSince {player1.name} is {player1.symbol}'s, {player2.name} will be {player2.symbol}'s!")
                        return [player1, player2]
                elif player2.lower() in player2_human_names:
                    pause()
                    print("\nCool! What is Player 2's name?")
                    while True:  # Make sure Player2 name not "The Computer," since that's reserved for the computer
                        player2_name = input("> ")
                        if player2_name.lower() == "quit":
                            return "" # ***See above
                        if player2_name != "The Computer":
                            break
                        else:
                            print("Please enter a different name besides 'The Computer'.")
                    player2 = Player(player2_name, "X") if player1.symbol == "O" else Player(player2_name, "O")
                    pause()
                    print(f"\nSince {player1.name} is {player1.symbol}'s, {player2.name} will be {player2.symbol}'s!")
                    return [player1, player2]
                else:
                    print("Please enter a valid input, like 'friend' or 'computer'")
# This function returns info about [player1, player2], which are in the class Player
