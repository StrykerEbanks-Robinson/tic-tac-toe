
# This is a game of tic-tac-toe that you can play against a human or bot!

import random
import Board
from Player_Information import Player
from Player_Information import define_players
import Turns


def play_again(player1, player2):
    if player1.name == "quit" and player2.name == "quit":
        Board.pause()
        print("\nSorry to see you go so early! Come back soon!\n")
        return False
    else:
        Board.pause()
        print("\nThanks for playing!")
        Board.pause()
        print("Would you like to play again?")
        while True:
            answer = input("> ")
            if answer.lower() in ["y", "yes", "yes please", "yeah", "i guess"]:
                return True
            elif answer.lower() in ["n", "no", "no thanks", "not really", "nope"]:
                Board.pause()
                print("\nOkay, bye!")
                return False
            else:
                print("Please enter 'Y', 'N', or something equivalent.")


def play_game():
    players = define_players()
    if players == "":
        player1 = Player("quit", "quit")
        player2 = Player("quit", "quit")
        return [player1, player2]
    else:
        game_board = Board.clean_board.copy()
        Board.print_board(game_board)
        # Choose a random player
        first_player = random.randint(0, 1)
        Board.pause()
        print(f"{players[first_player].name} goes first!")
        player1 = players[first_player]  # This makes the random player become P1
        player2 = players[(first_player - 1) % 2]  # This will change 1 -> 0 and 0 -> 1.

        if player1.level == 0 and player2.level == 0:  # humans have a default level of 0
            while True:
                turn1 = Turns.take_human_turn(player1, game_board)
                if turn1 == "quit":
                    player1 = Player("quit", "quit")
                    player2 = Player("quit", "quit")
                    break
                elif turn1:
                    break
                turn2 = Turns.take_human_turn(player2, game_board)
                if turn2 == "quit":
                    player1 = Player("quit", "quit")
                    player2 = Player("quit", "quit")
                    break
                elif turn2:
                    break

        else:
            final_players = Turns.play_computer_game(player1, player2, game_board)
            player1 = final_players[0]
            player2 = final_players[1]

        return [player1, player2]


if __name__ == '__main__':
    while True:
        main_players = play_game()
        if play_again(main_players[0], main_players[1]):
            Board.pause()
            print("Great!")
        else:
            break
