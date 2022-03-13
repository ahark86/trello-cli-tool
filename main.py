import os
import platform
import t_secrets
import trello as t
clear = lambda: os.system('clear')

title = "\nTrello CLI Tool"
help_block = "\nAvailable Commands:\n\n" \
             "create-board (Creates new board based on a specific existing template)\n" \
             # "get-user-id (Enter username, Trello user ID is returned)\n" \
             # "reveal-secrets (Displays Trello API Key and API Token)\n"


def run():
    if platform.system() == 'Darwin' or platform.system() == 'Linux':
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
        if user_input.lower() == "get-user-id":
            u_name = ""
            while len(u_name) == 0:
                u_name = input("Enter username: ")
            try:
                print(t.get_member_id_by_username(u_name))
            except:
                print("Invalid username or something went wrong")
        if user_input.lower() == "reveal-secrets":
            print(f'\nAPI Key: {t_secrets.TRELLO_KEY}')
            print(f'API Token: {t_secrets.TRELLO_TOKEN}')


run()
