import os
clear = lambda: os.system('clear')

help_block = "\nTrello CLI Tool\n\n" \
             "Available Commands:\n" \
             "create-board (Creates new board based on a specific existing template)\n"


def run():
    clear()
    if not os.path.exists('secrets.py'):
        t_key = ""
        t_token = ""
        while len(t_key) < 1 or len(t_token) < 1:
            print("\n")
            t_key = input("Enter Trello API key: ")
            t_token = input("Enter Trello API token: ")
        with open('secrets.py', 'w') as f:
            f.write(f'TRELLO_KEY = \"{t_key}\"\n'
                    f'TRELLO_TOKEN = \"{t_token}\"')
    import trello as t
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
