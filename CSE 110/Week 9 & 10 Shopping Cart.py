print("Welcome to the Shopping Cart Experience")
print()
choice = int(input("Please select one of the following:"
"\n1: add item"
"\n2: view cart"
"\n3: remove items"
"\n4: view total"
"\n5: quit"
"\n"))
lists = []
costs = []

while choice != 5:
    if choice == 1:
        add_item = input("What would you like to add? ")
        lists.append(add_item)
        add_cost = float(input("How much does this item cost?"))
        costs.append(add_cost)
    elif choice == 2:
        for i in range(len(lists)):
            print(f"{i + 1}. {lists[i]} - ${costs[i]:.2f}")
    elif choice == 3:
        remove_item = int(input("What Item would you like to remove? "))
        lists.pop(remove_item - 1)
        costs.pop(remove_item - 1)
        print("Your item has successfully been removed")
    elif choice == 4:
        sum_price = sum(costs)
        print(f"Your total is: ${sum_price:.2f}")
    else:
        print("That's not a valid choice, please try again.")
    choice = int(input("Please select one of the following:"
    "\n1: add item"
    "\n2: view cart"
    "\n3: remove items"
    "\n4: view total"
    "\n5: quit"
    "\n"))
print("Thank you for sharing the Shopping Cart Experience")