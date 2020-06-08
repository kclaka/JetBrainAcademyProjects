# Write your code here


amount_of_water = int(input("Write how many ml of water the coffee machine has:"))
amount_of_milk = int(input("Write how many ml of milk the coffee machine has:"))
amount_of_coffee_beans = int(input("Write how many grams of coffee beans the coffee machine has:"))

num_coffee = int(input("Write how many cups of coffee you will need:"))

amount_of_water_needed = 200 * num_coffee
amount_of_milk_needed = 50 * num_coffee
amount_of_coffee_beans_needed = 15 * num_coffee


def getmincoffee():
    if (amount_of_water > 0 and amount_of_milk > 0
            and amount_of_coffee_beans > 0):
        min_water = amount_of_water // 200
        min_milk = amount_of_milk // 50
        min_coffee = amount_of_coffee_beans // 15
        return min(min_milk, min_water, min_coffee)
    else:
        return 0


if (amount_of_water == amount_of_water_needed and
        amount_of_milk == amount_of_milk_needed and
        amount_of_coffee_beans == amount_of_coffee_beans_needed):
    print("Yes, I can make that amount of coffee")
elif (amount_of_water > amount_of_water_needed and
      amount_of_milk > amount_of_milk_needed and
      amount_of_coffee_beans > amount_of_coffee_beans_needed):
    print(f"Yes, I can make that amount of coffee (and even {getmincoffee() - num_coffee} more than that)")
else:
    print(f"No, I can make only {getmincoffee()} cups of coffee")

# print(f"For {num_coffee} of coffee you will need:")
# print(f"{200 * num_coffee} of water")
# print(f"{50 * num_coffee} of milk")
# print(f"{15 * num_coffee}g of coffee beans")
