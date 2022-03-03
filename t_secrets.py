from pathlib import Path
import os
clear = lambda: os.system('clear')

clear()
home_path = Path.home()
if os.path.exists(f'{home_path}/t_secrets.txt'):
    with open(f'{home_path}/t_secrets.txt', 'r') as f:
        secret_values = f.readlines()
        TRELLO_KEY = secret_values[0]
        TRELLO_TOKEN = secret_values[1]
else:
    t_key = ""
    t_token = ""
    while len(t_key) < 1 or len(t_token) < 1:
        print("\n")
        t_key = input("Enter Trello API key: ")
        t_token = input("Enter Trello API token: ")
    with open(f'{home_path}/t_secrets.txt', 'w') as f:
        f.write(f'{t_key}\n'
                f'{t_token}')
    TRELLO_KEY = t_key
    TRELLO_TOKEN = t_token