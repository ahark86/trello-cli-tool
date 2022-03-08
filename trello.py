import requests
import t_secrets

TRELLO_KEY = t_secrets.TRELLO_KEY
TRELLO_TOKEN = t_secrets.TRELLO_TOKEN

headers = {"Accept": "application/json"}
data = {"key": TRELLO_KEY, "token": TRELLO_TOKEN}


def get_board(id):
    response = requests.get(
        f'https://api.trello.com/1/boards/{id}/',
        headers=headers,
        data=data)
    return response.json()


def get_member_id_by_username(username):
    response = requests.get(
        f'https://api.trello.com/1/members/{username}/',
        headers=headers,
        data=data)
    return response.json()['id']


def get_target_list_from_board(id):
    response = requests.get(
        f'https://api.trello.com/1/boards/{id}/lists',
        headers=headers,
        data=data)
    return response.json()


def get_cards_from_target_list(id):
    response = requests.get(
        f'https://api.trello.com/1/lists/{id}/cards',
        headers=headers,
        data=data)
    return response.json()


def add_member_to_card(card_id, member_id):
    query = {
        "value": member_id
    }

    response = requests.request(
        "POST",
        f'https://api.trello.com/1/cards/{card_id}/idMembers',
        params=query,
        headers=headers,
        data=data
    )


def create_board_from_template(board_name, board_desc=""):
    template_board_id = "60eba0abbfdc3321531cefc8"
    workspace_id = "60d4dc2f7279c74626cf836a"
    workspace_name = "Freedom Healthworks"

    query = {
        "name": board_name,
        "desc": board_desc,
        "idBoardSource": template_board_id,
        "idOrganization": workspace_id,
        "keepFromSource": "cards",
    }

    print(f'Creating Board: \"{board_name}\" ...')

    response = requests.request(
        "POST",
        "https://api.trello.com/1/boards/",
        params=query,
        headers=headers,
        data=data
    )

    print(f'Board: \"{board_name}\" created successfully!')

    # Get card IDs for new board
    new_board_id = response.json()['id']
    target_list_id = get_target_list_from_board(new_board_id)[1]['id']
    target_cards = get_cards_from_target_list(target_list_id)
    target_card_ids = [card['id'] for card in target_cards]

    # Get member IDs from template board
    template_list_id = get_target_list_from_board(template_board_id)[1]['id']
    template_cards = get_cards_from_target_list(template_list_id)
    template_card_member_ids = [card['idMembers'] for card in template_cards]

    print(f'Adding members to cards on Board: \"{board_name}\" (this takes several seconds) ...')

    for card in range(0, len(target_card_ids)):
        for member in template_card_member_ids[card]:
            add_member_to_card(target_card_ids[card], member)

    print("Members added successfully!")
    print("Process Complete")
