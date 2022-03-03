import os
import t_secrets
import trello as t
clear = lambda: os.system('clear')

title = "\nTrello CLI Tool"
help_block = "\nAvailable Commands:\n" \
             "create-board (Creates new board based on a specific existing template)\n" \
             "reveal-secrets (Displays Trello API Key and API Token)"


def run():
    clear()
    print(title)
    while True:
        print(help_block)
        user_input = input("> ")
        if user_input.lower() == "create-board":
            b_name = ""
            while len(b_name) == 0:
                b_name = input("Enter name for new board (Required): ")
            b_desc = input("Enter description for new board (optional): ")
            t.create_board_from_template(board_name=b_name, board_desc=b_desc)
        if user_input.lower() == "reveal-secrets":
            print(f'\nAPI Key: {t_secrets.TRELLO_KEY}')
            print(f'API Token: {t_secrets.TRELLO_TOKEN}')


run()
