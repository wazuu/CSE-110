input("Welcome to the Road Kill Cafe, Where you Kill it and We Grill it.Please press ENTER for our waiter to ask you some questions. Thank you!")

print()

childrens_meal = float(input("What is the price of a Childs meal?"))
adults_meal = float(input("What is the price for an Adults meal?"))
children_ordering = input("How many children will be ordering?")
adults_ordering = input("How many adults will be ordering?")
tax = float(input("What is the current sales tax in your city?"))

print()
 
print("Subtotal:$ ", float(childrens_meal) * float(children_ordering) + float(adults_meal) * float(adults_ordering)%.2)
subtotal = float(float(childrens_meal) * float(children_ordering) + float(adults_meal) * float(adults_ordering)%.2)
print("Sales Tax:$ ", float(subtotal) * float(tax)%.2)
print("Toatl:$ ", float(subtotal) + float(tax)%.2)

print()

change = float(input("What is the payment amount?"))
total = float(float(subtotal) * float(tax)%.2)
print("Change:$ ", float(change) - float(total)%.2)

print()

input("Thank you for coming to The Road Kill Cafe. We hope you enjoyed your meal! Please press ENTER to Exit")




