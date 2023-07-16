friends = []
name = None
while name !="end":
    name = input("Type the name of a frined:")
    if name !="end":
        friends.append(name)
print()
print("Your friends name are:")
for friends in friends:
    print(friends)