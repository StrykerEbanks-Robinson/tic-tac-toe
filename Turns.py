from Board import pause
from Board import print_board
import random
import math  # for minimax
from Board import clean_board  # For running tests
from Player_Information import Player  # For running tests


def winning_combos(board):
    return [
        board[1] + board[2] + board[3],  # Rows
        board[4] + board[5] + board[6],
        board[7] + board[8] + board[9],
        board[1] + board[4] + board[7],  # Columns
        board[2] + board[5] + board[8],
        board[3] + board[6] + board[9],
        board[1] + board[5] + board[9],  # Diagonals
        board[3] + board[5] + board[7]
    ]


def win_check(player, board, print_result=True):
    winning_symbol = player.symbol + player.symbol + player.symbol
    combos = winning_combos(board)
    if winning_symbol in combos:
        if print_result:
            pause()
            print(f"{player.name} wins! Congratulations, {player.name}!!")
        return True
    else:
        return False


def tie_check(board, print_result=True):
    position_values = ""
    for position in range(1, 10):
        position_values += board[position]
    if " " not in position_values:
        if print_result:
            pause()
            print("Oh, no! It was a tie! :(")
        return True
    else:
        return False


def take_human_turn(player, board):
    pause()
    print(f"{player.name}, what spot would you like to play in?")
    position = None
    while True:  # Check position is empty
        response = input("> ")
        if response.lower() == "quit":
            break
        else:
            try:
                position = int(response)
                if board[position] == " ":
                    break
                else:
                    print("Please select a space that doesn't have an X or O.")
            except ValueError:
                print("Please pick a valid position from 1 - 9, or type \"quit\" to quit.")
            except KeyError:
                print("Please pick a valid position from 1 - 9, or type \"quit\" to quit.")
    if response.lower() == "quit":
        return "quit"
    else:
        board[position] = player.symbol
        print_board(board)
        if win_check(player, board, print_result=True):
            return True
        elif tie_check(board, print_result=True):
            return True
        else:
            return False


def minimax(board, max_player, player1, player2):

    # defining empty_spots for use throughout function
    empty_spots = [spot for spot in range(1, 10) if board[spot] == " "]

    # checking if the previous move was a win or tie
    if win_check(player2, board, print_result=False):
        return {"position": None, "score": 1 * (len(empty_spots) + 1) if max_player == player2 else -1 * (
                len(empty_spots) + 1)}
    elif tie_check(board, print_result=False):
        return {"position": None, "score": 0}

    # setting the basis for the best possible move
    if player1 == max_player:
        best = {"position": None, "score": -math.inf}  # each score should be maximized
    else:
        best = {"position": None, "score": math.inf}  # each score should be minimized

    # moving into recursive 'for' loop
    for possible_move in empty_spots:
        board[possible_move] = player1.symbol
        sim_score = minimax(board, max_player, player2, player1)  # simulate a game after making that move

        # undo-ing previous move bc a result was returned
        board[possible_move] = " "
        sim_score["position"] = possible_move  # this represents the most optimal next move

        if player1 == max_player:
            if sim_score["score"] > best["score"]:
                best = sim_score
        else:
            if sim_score["score"] < best["score"]:
                best = sim_score

    return best


# Lvl 1 comp
def easy_computer_player(computer, board):
    empty_spots = [spot for spot in range(1, 10) if board[spot] == " "]
    position = random.choice(empty_spots)
    pause()
    print(f"The computer would like to play in spot {position}.")
    board[position] = computer.symbol
    print_board(board)
    if win_check(computer, board, print_result=True):
        return True
    elif tie_check(board, print_result=True):
        return True
    else:
        return False


# Lvl 2 comp
def medium_computer_player(computer, opponent, board):

    # Create a list of all current board values so comp can check if it has played its first move yet
    board_values = [board[spot] for spot in range(1, 10)]

    # Check if any of the pre-win or pre-lose combos are present on the board
    win_lose_combo_present = False
    win_lose_combos = [
        " " + computer.symbol + computer.symbol, computer.symbol + " " + computer.symbol,
        computer.symbol + computer.symbol + " ", " " + opponent.symbol + opponent.symbol,
        opponent.symbol + " " + opponent.symbol, opponent.symbol + opponent.symbol + " "
    ]
    for combo in win_lose_combos:
        if combo in winning_combos(board):
            win_lose_combo_present = True
            break

    # First, check if the computer is on its first turn
    if computer.symbol not in board_values:
        while True:
            first_play = random.choice([1, 3, 5, 7, 9])  # randomly choose one of these offensive positions
            if board[first_play] == " ":
                break
        pause()
        print(f"The Computer would like to start in spot {first_play}.")
        board[first_play] = computer.symbol
    # Next, check if one of the pre-win or pre-lose combos are present on the board
    elif win_lose_combo_present:
        position = minimax(board, computer, computer, opponent)["position"]
        pause()
        print(f"The Computer has decided that the best move would be spot {position}.")
        board[position] = computer.symbol
    # If neither of the previous are the case, pick a random spot to play in
    else:
        empty_spots = [spot for spot in range(1, 10) if board[spot] == " "]
        position = random.choice(empty_spots)
        pause()
        print(f"The Computer wants to play in spot {position}.")
        board[position] = computer.symbol
    print_board(board)
    if win_check(computer, board, print_result=True):
        return True
    elif tie_check(board, print_result=True):
        return True
    else:
        return False


# Lvl 3 comp
def hard_computer_player(computer, opponent, board):
    position = minimax(board, computer, computer, opponent)["position"]
    pause()
    print(f"The Computer would like to play in spot {position}.")
    board[position] = computer.symbol
    print_board(board)
    if win_check(computer, board, print_result=True):
        return True
    elif tie_check(board, print_result=True):
        return True
    else:
        return False


def play_computer_game(player1, player2, board):
    if player1.level in [1, 2, 3]:
        while True:
            # Computer's turn
            if player1.level == 1:
                if easy_computer_player(player1, board):
                    return [player1, player2]
            elif player1.level == 2:
                if medium_computer_player(player1, player2, board):
                    return [player1, player2]
            else:
                if hard_computer_player(player1, player2, board):
                    return [player1, player2]
            # Human's turn
            hum_turn = take_human_turn(player2, board)
            if hum_turn == "quit":
                player1 = Player("quit", "quit")
                player2 = Player("quit", "quit")
                return [player1, player2]
            elif hum_turn:
                return [player1, player2]

    elif player2.level in [1, 2, 3]:
        while True:
            # Human's turn
            hum_turn = take_human_turn(player1, board)
            if hum_turn == "quit":
                player1 = Player("quit", "quit")
                player2 = Player("quit", "quit")
                return [player1, player2]
            elif hum_turn:
                return [player1, player2]
            # Computer's turn
            if player2.level == 1:
                if easy_computer_player(player2, board):
                    return [player1, player2]
            elif player2.level == 2:
                if medium_computer_player(player2, player1, board):
                    return [player1, player2]
            else:
                if hard_computer_player(player2, player1, board):
                    return [player1, player2]

    else:
        print("Something has gone wrong. It appears that two Players with level=0 are trying to execute\
                 play_computer_game().")


def minimax_print(board, max_player, player1, player2):

    # defining empty_spots for use throughout function
    print("1. Defining empty_spots")
    empty_spots = [spot for spot in range(1, 10) if board[spot] == " "]
    print(f"empty_spots = {empty_spots}")

    # checking if the previous move was a win or tie
    print("2. Checking for previous winner or tie.")
    if win_check(player2, board, print_result=False):
        print(f"Based on {player2.name}'s last move, they won!")
        return {"position": None, "score": 1 * (len(empty_spots) + 1) if max_player == player2 else -1 * (
                len(empty_spots) + 1)}
    elif tie_check(board, print_result=False):
        print(f"Based on {player2.name}'s last move, there was a tie.")
        return {"position": None, "score": 0}

    # setting the basis for the best possible move
    print("3. Defining best move scenarios.")
    if player1 == max_player:
        best = {"position": None, "score": -math.inf}  # each score should be maximized
        print(f"Current 'best' = {best}")
    else:
        best = {"position": None, "score": math.inf}  # each score should be minimized
        print(f"Current 'best' = {best}")

    # moving into recursive 'for' loop
    print("4. Moving into for loop.")
    for possible_move in empty_spots:
        print(f"Playing possible move: {possible_move}, {player1.symbol}")
        board[possible_move] = player1.symbol
        print(f"Running next iteration for {player2.name}'s turn")
        sim_score = minimax_print(board, max_player, player2, player1)  # simulate a game after making that move

        # undo-ing previous move bc a result was returned
        print(f"5. A result was returned. Resetting spot {possible_move} to \" \".")
        board[possible_move] = " "
        sim_score["position"] = possible_move  # this represents the most optimal next move

        print("6. Comparing sim_score to best.")
        if player1 == max_player:
            if sim_score["score"] > best["score"]:
                best = sim_score
                print(f"7. Since {player1.name} is the max_player, the new best move is {best}")
        else:
            if sim_score["score"] < best["score"]:
                best = sim_score
                print(f"7. Since {player1.name} is not the max_player, the new best move is {best}")

    print(f"The optimal move to make is {best}")
    return best


"""
temp_board = clean_board.copy()
p1 = Player("The Computer", "O")
p2 = Player("Stryker", "X")
temp_board[1] = p1.symbol
temp_board[7] = p2.symbol
temp_board[3] = p1.symbol
temp_board[5] = p2.symbol

board_values = [temp_board[spot] for spot in range(1,10)]
print(board_values)
print(p2.symbol not in board_values)
# minimax_print(temp_board, p1, p1, p2)



def random_comp_turn(player, board):  # lvl 1 difficulty
    empty_spots = [spot for spot in range(1, 10) if board[spot] == " "]
    board[random.choice(empty_spots)] = player.symbol


def offensive_comp_turn(player, opponent, board):
    board[minimax(board, player, player, opponent)["position"]] = player.symbol


def test_play(random_player, offense_player, board):
    first_player = random.choice([random_player, offense_player])
    if first_player == random_player:
        while True:

            random_comp_turn(random_player, board)
            if win_check(random_player, board, False):
                return "R"
            elif tie_check(board, False):
                return "T"

            offensive_comp_turn(offense_player, random_player, board)
            if win_check(offense_player, board, False):
                return "O"
            elif tie_check(board, False):
                return "T"

    else:
        while True:

            offensive_comp_turn(offense_player, random_player, board)
            if win_check(offense_player, board, False):
                return "O"
            elif tie_check(board, False):
                return "T"

            random_comp_turn(random_player, board)
            if win_check(random_player, board, False):
                return "R"
            elif tie_check(board, False):
                return "T"


results = {"R": 0, "O": 0, "T": 0}
for _ in range(1000):
    game_board = clean_board.copy()
    p1 = Player("Random Computer", random.choice(["X", "O"]))
    p2 = Player("Offense Computer", "O" if p1.symbol == "X" else "X")
    results[test_play(p1, p2, game_board)] += 1
    print(f"Game {_} done.")

print(f'The random computer won {results["R"]} times, the Minimax computer won {results["O"]} times, and there\
 were {results["T"]} ties.')
"""
