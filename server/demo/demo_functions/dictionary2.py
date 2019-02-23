balances = [{"id":x, "bitcoin_balance":x*5} for x in range(0,10000)]
users = [{"id":x, "name": "some_name"} for x in range(0,10000)]
# convert to dictionary

def associate_balances():
    balance_dictionary = {x["id"]: x["bitcoin_balance"] for x in balances}
    for user in users:
        user["bitcoin_balance"] = balance_dictionary[user["id"]]

associate_balances()
