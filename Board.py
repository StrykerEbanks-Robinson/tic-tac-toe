
import time

"""
row_1_values = [" ", "|", " ", "|", " "]
row_2_values = [" ", "|", " ", "|", " "]
row_3_values = [" ", "|", " ", "|", " "]
"""

clean_board = {
    "VL": "|", "HL": "—+—+—",
    1: " ", 2: " ", 3: " ",
    4: " ", 5: " ", 6: " ",
    7: " ", 8: " ", 9: " "
}


def pause():
    time.sleep(0)


def print_board(board):
    print("")
    # Will add row + col to get board positions, so each row value must go up by 3 to represent skipping an entire row
    for row in [0, 3, 6]:
        row_values = ""
        for col in [1, 2, 3]:
            row_values = row_values + board[row + col]
            if col < 3:  # There are only 2 VLs
                row_values = row_values + board["VL"]
        print(row_values)
        if row != 6:  # Don't need a horizontal line after the last row
            print(board["HL"])
    print("")
