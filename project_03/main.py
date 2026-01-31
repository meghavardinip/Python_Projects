resources_available={"Water":300,"Milk":200,"Coffee":100}
Resources_required={"Espresso":{"Water":50,"Coffee":18,"cost": 1.5},"Latte":{"Water":200,"Coffee":24,"Milk":150,"cost": 2.5},"Cappuccino":{"Water":250,"Coffee":24,"Milk":100,"cost": 3.0}}
Items_available={1:"Espresso",2:"Latte",3:"Cappuccino"}
profit=0
def resources(chosen):
    global resources_available
    if chosen in Items_available:
        Drink = Items_available[chosen]
        if Drink in Resources_required:
            res_needed = Resources_required[Drink]
            for item, quantity in res_needed.items():
                if item!="cost":
                    resources_available[item] -= quantity
    return resources_available
def report():
    dict = {"Water": "ml", "Milk": "ml", "Coffee": "g"}
    for a,b in resources_available.items():
        if a in dict.keys():
            c=dict[a]
            print(f"{a}:{b}{c}")
    print(f"Profit: ${profit}")
def sufficient(chosen):
    if chosen in Items_available:
        Drink = Items_available[chosen]
        if Drink in Resources_required:
            res_needed = Resources_required[Drink]
            for item, quantity in res_needed.items():
                if item!="cost" and resources_available[item] < quantity:
                    print(f"Not enough {item} to make {Drink}.")
                    return False
            return True
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
def is_transaction_successful(money_received,cost):
    if money_received>=cost:
        change = round(money_received-cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
def coffee_machine_on():
    for items in Items_available:
        print(f"Press {items} for {Items_available[items]}")
    print("Press 4 for report")
    chosen=int(input("What would you like to choose?"))
    if chosen==4:
        report()
    elif chosen in Items_available:
        drink=Items_available[chosen]
        og_cost=Resources_required[drink]["cost"]
        print(f"The cost is {og_cost}$")
        payment=process_coins()
        if is_transaction_successful(payment, Resources_required[drink]["cost"]):
            suff = sufficient(chosen)
            if suff:
                resources(chosen)
                print(f"{drink} is being prepared...")
                print("Enjoy your drink!")
            else:
                print("Order cannot be completed due to insufficient resources.")
    return None
def coffee_machine_on_or_off():
    while True:
        action = input("Press 'on' to start the coffee machine or 'off' to stop it: ").lower()
        if action=="on":
            while True:
                coffee_machine_on()
                c=input("Do you want to place another order? type y/n")
                if c=="y":
                    continue
                else:
                    break
        elif action=="off":
            print("Turning off the coffee machine!")
            break
        else:
            print("Invalid input. Please enter 'on' or 'off'.")
coffee_machine_on_or_off()
