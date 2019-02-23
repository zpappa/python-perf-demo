balances = [{"id": x, "bitcoin_balance": x * 5} for x in range(0, 10000)]
users = [{"id": x, "name": "some_name"} for x in range(0, 10000)]


def find_balance(x):
    for i in range(0, len(balances)):
        if balances[i]["id"] == x:
            return balances[i]["bitcoin_balance"]
    return None


def associate_balances():
    for user in users:
        user["bitcoin_balance"] = find_balance(user["id"])
