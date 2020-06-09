# Write your code here
machine_money = 550
machine_water = 400
machine_milk = 540
coffee_beans = 120
machine_cups = 9


def get_machine_money():
    return machine_money


def get_machine_water():
    return machine_water


def get_machine_milk():
    return machine_milk


def get_machine_beans():
    return coffee_beans


def get_machine_cups():
    return machine_cups


def check_expresso():
    return get_machine_water() > 250 and get_machine_beans() > 16


def check_latte():
    return get_machine_water() > 350 and get_machine_milk() > 75 and get_machine_beans() > 20


def check_cappuccino():
    return get_machine_water() > 200 and get_machine_milk() > 100 and get_machine_beans() > 12


def make_expresso():
    global machine_water, coffee_beans, machine_money, machine_cups
    if check_expresso():
        machine_water = machine_water - 250
        coffee_beans = coffee_beans - 16
        machine_money = machine_money + 4
        machine_cups = machine_cups - 1
        print_machine_state()
    else:
        print("Not enough Ingridents")


def make_latte():
    global machine_water, machine_milk, coffee_beans, machine_money, machine_cups
    if check_latte():
        machine_water = machine_water - 350
        coffee_beans = coffee_beans - 20
        machine_milk = machine_milk - 75
        machine_money = machine_money + 7
        machine_cups = machine_cups - 1
        print_machine_state()
    else:
        print("Not enough ingridents")


def make_cappuccino():
    global machine_water, machine_milk, coffee_beans, machine_money, machine_cups
    if check_cappuccino():
        machine_water = machine_water - 200
        coffee_beans = coffee_beans - 12
        machine_milk = machine_milk - 100
        machine_money = machine_money + 6
        machine_cups = machine_cups - 1
        print_machine_state()
    else:
        print("Not enough ingridents")


def handle_buy():
    buy_options = int(input())
    if buy_options == 1:
        make_expresso()
    if buy_options == 2:
        make_latte()
    if buy_options == 3:
        make_cappuccino()


def handle_fill():
    global machine_water, machine_milk, coffee_beans, machine_cups
    user_fill_water = int(input("Write how many ml of water do you want to add:"))
    machine_water = machine_water + user_fill_water
    user_fill_milk = int(input("Write how many ml of milk do you want to add:"))
    machine_milk = machine_milk + user_fill_milk
    user_fill_bean = int(input("Write how many grams of coffee beans do you want to add:"))
    coffee_beans = coffee_beans + user_fill_bean
    user_fill_cup = int(input("Write how many disposable cups of coffee do you want to add:"))
    machine_cups = machine_cups + user_fill_cup

    print_machine_state()


def handle_take():
    global machine_money
    print(f"I gave you {machine_money}")
    machine_money = machine_money - machine_money
    print_machine_state()


def handle_options():
    options = input()
    if options == "buy":
        handle_buy()
    elif options == "fill":
        handle_fill()
    elif options == "take":
        handle_take()
    else:
        print("Option not found")


# amount_of_water_needed = 200 * num_coffee
# amount_of_milk_needed = 50 * num_coffee
# amount_of_coffee_beans_needed = 15 * num_coffee


# def getmincoffee():
#     if (amount_of_water > 0 and amount_of_milk > 0
#             and amount_of_coffee_beans > 0):
#         min_water = amount_of_water // 200
#         min_milk = amount_of_milk // 50
#         min_coffee = amount_of_coffee_beans // 15
#         return min(min_milk, min_water, min_coffee)
#     else:
#         return 0


# if (amount_of_water == amount_of_water_needed and
#         amount_of_milk == amount_of_milk_needed and
#         amount_of_coffee_beans == amount_of_coffee_beans_needed):
#     print("Yes, I can make that amount of coffee")
# elif (amount_of_water > amount_of_water_needed and
#       amount_of_milk > amount_of_milk_needed and
#       amount_of_coffee_beans > amount_of_coffee_beans_needed):
#     print(f"Yes, I can make that amount of coffee (and even {getmincoffee() - num_coffee} more than that)")
# else:
#     print(f"No, I can make only {getmincoffee()} cups of coffee")

# print(f"For {num_coffee} of coffee you will need:")
# print(f"{200 * num_coffee} of water")
# print(f"{50 * num_coffee} of milk")
# print(f"{15 * num_coffee}g of coffee beans")

def print_machine_state():
    print("The coffee machine has: ")
    print(f"{get_machine_water()} of water")
    print(f"{get_machine_milk()} of milk")
    print(f"{get_machine_beans()} of coffee beans")
    print(f"{get_machine_cups()} of disposable cups")
    print(f"{get_machine_money()} of money")


print_machine_state()
print("Write action (buy, fill, take):")
handle_options()
