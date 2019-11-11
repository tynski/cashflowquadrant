import json


users = []
max_income_outcome_sum = 0
min_income_outcome_sum = 500000
max_income_outcome_diff = 0
min_income_outcome_diff = 500000
max_balance = 0
min_balance = 500000


def update_users():
    global users

    input_file = open('./data/users.json')
    json_users = json.load(input_file)
    users = []

    for u in json_users:
        user = {
            'id': u['id'],
            'total_income': u['total_income'],
            'total_outcome': u['total_outcome'],
            'current_balance': u['current_balance']
        }
        users.append(user)

    update_stats()


def update_stats():
    global users
    global max_income_outcome_sum
    global min_income_outcome_sum
    global max_income_outcome_diff
    global min_income_outcome_diff
    global max_balance
    global min_balance

    for user in users:
        user_income = user['total_income']
        user_outcome = user['total_outcome']
        user_balance = user['current_balance']
        user_income_outcome_sum = user_income + user_outcome
        user_income_outcome_diff = user_income - user_outcome

        if user_income_outcome_sum > max_income_outcome_sum:
            max_income_outcome_sum = user_income_outcome_sum
        elif user_income_outcome_sum < min_income_outcome_sum:
            min_income_outcome_sum = user_income_outcome_sum

        if user_income_outcome_diff > max_income_outcome_diff:
            max_income_outcome_diff = user_income_outcome_diff
        elif user_income_outcome_diff < min_income_outcome_diff:
            min_income_outcome_diff = user_income_outcome_diff

        if user_balance > max_balance:
            max_balance = user_balance
        elif user_balance < min_balance:
            min_balance = user_balance


def is_user(user_id):
    global users

    if not any(str(d.get('id', None)) == user_id for d in users):
        return False
    return True


def find_user(user_id):
    global users

    for user in users:
        if str(user['id']) == user_id:
            return user


def classify_user(user_id):
    global users
    global max_income_outcome_diff
    global min_income_outcome_diff
    global max_balance
    global min_balance

    classes = [
        "high_bal_high_diff",
        "high_bal_low_diff",
        "low_bal_high_diff",
        "low_bal_low_diff",
        "middle_bal_middle_diff"
    ]

    user = find_user(user_id)
    middle_diff = (max_income_outcome_diff - min_income_outcome_diff) / 2
    middle_balance = (max_balance + min_balance) / 2
    user_diff = user['total_income'] - user['total_outcome']
    user_balance = user['current_balance']

    if user_balance > middle_balance:
        if user_diff > middle_diff:
            return classes[0]
        else:
            return classes[1]
    else:
        if user_diff > middle_diff:
            return classes[2]
        else:
            return classes[3]


def calculate_level(user_id):
    global users
    global max_income_outcome_sum
    global min_income_outcome_sum

    user = find_user(user_id)
    middle_sum = (max_income_outcome_sum + min_income_outcome_sum) / 2

    if user["total_income"] + user["total_outcome"] >= middle_sum:
        return "high"
    else:
        return "low"
