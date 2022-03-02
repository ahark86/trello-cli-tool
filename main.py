import trello as t
import os
clear = lambda: os.system('clear')

help_block = "\nTrello CLI Tool\n\n" \
             "Available Commands:\n" \
             "create-board (Creates new board based on a specific existing template)\n"


def run():
    clear()
    while True:
        b_name = ""
        print(help_block)
        user_input = input("> ")
        if user_input.lower() == "create-board":
            while len(b_name) == 0:
                b_name = input("Enter name for new board (Required): ")
            b_desc = input("Enter description for new board (optional): ")
            t.create_board_from_template(board_name=b_name, board_desc=b_desc)


run()
