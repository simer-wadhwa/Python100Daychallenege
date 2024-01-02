def report(resources, money):
    for k, v in resources.items():
        print(f"{k}: {v}")
    print(f"Money: ${money}")


def check_resources(resources, coffee_resources, coffee):
    if coffee_resources["water"] > resources["water"]:
        #print(coffee_resources["water"])
        print("Sorry there is not enough water.")
        return False
    if coffee_resources["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    if coffee != "espresso":
        if coffee_resources["milk"] > resources["milk"]:
            print("Sorry there is not enough milk.")
            return False

    return True


def transaction(cost, money):
    print("Please insert coins.")
    quaters = int(input("how many quarters?"))
    dimes = int(input("how many dimes?"))
    nickles = int(input("how many nickles?"))
    pennies = int(input("how many pennies?"))
    total = 0.25*quaters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    if total < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False,money
    change = total - cost
    change = format(change, ".2f")
    money = money + cost
    print(f"Here is ${change} in change.")
    return True, money


def make_coffee(resources, coffee_resources, coffee):
    resources["water"] = resources["water"] - coffee_resources["water"]
    resources["coffee"] = resources["coffee"] - coffee_resources["coffee"]
    if coffee != "espresso":
        resources["milk"] = resources["milk"] - coffee_resources["milk"]


def machine():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    status = True
    money = 0
    while status:
        choose = input(f"What would you like? (espresso/latte/cappuccino):")
        if choose == "report":
            report(resources, money)
        elif choose.lower() == "off":
            status = False
        # elif choose == 'espresso':
        #     if check_resources(resources, MENU["espresso"]["ingredients"], "espresso"):
        #         success, money = transaction(MENU["espresso"]["cost"], money)
        #         if success:
        #             make_coffee(resources, MENU["espresso"]["ingredients"], "latte")
        #             print(f"Here is your espresso ☕️. Enjoy!")
        # elif choose == 'latte':
        #     if check_resources(resources, MENU["latte"]["ingredients"], "latte"):
        #         success, money = transaction(MENU["latte"]["cost"], money)
        #         if success:
        #             make_coffee(resources, MENU["latte"]["ingredients"], "latte")
        #             print(f"Here is your espresso ☕️. Enjoy!")
        # elif choose == 'cappuccino':
        #     if check_resources(resources, MENU["cappuccino"]["ingredients"], "cappuccino"):
        #         success, money = transaction(MENU["cappuccino"]["cost"], money)
        #         if success:
        #             make_coffee(resources, MENU["cappuccino"]["ingredients"], "cappuccino")
        #             print(f"Here is your espresso ☕️. Enjoy!")
        else:
            if check_resources(resources, MENU[choose]["ingredients"], choose):
                success, money = transaction(MENU[choose]["cost"], money)
                if success:
                    make_coffee(resources, MENU[choose]["ingredients"], choose)
                    print(f"Here is your {choose} ☕️. Enjoy!")


machine()