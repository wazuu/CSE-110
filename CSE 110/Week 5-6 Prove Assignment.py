choices = input("You are standing alone under the only streetlight in a county park.The light burns out. Do you pull out a LIGHTER or a FLASHLIGHT from your back pack?")
if choices.lower() == "lighter":
    choices = input("The lighter lights up a little around you, but ont much. You hear footsteps in the dastance. Do you go TOWARDS the footsteps, or do you LOOK for the sidewalk that leads you home?")
    if choices.lower() == "towards":
        choices = input("You slowly walk towards the footsteps. You see a stray dog. Do you TAKE the dog home, SEND it to the pound, or LEAVE it?")
        if choices.lower() == "take":
            print("Good job, you just added a nice new member to the family.")
        elif choices.lower() == "send":
            print("A family who was looking for the perfect pet, found this dog. Nice job.")
        elif choices.lower() == "leave":
            print("Not sure what ever happened to this dog. But, this isn't the best solution. Better luck next time.")
    elif choices.lower() == "look":
         choices = input("You slowly found the sidewalk home, but your lighter is still too dim to see anything. Do you CALL for a ride, or, do you take COURAGE and walk home?")
    if choices.lower() == "call":
            print("Your parents come and get you and take you directly home. Good Choice.")
    elif choices.lower() == "courage":
            print("You keep on the path to go home, but you ended up getting spooked out and finally called for a ride. Not the best route to take.")
elif choices.lower() == "flashlight":
        choices = input("You see the sidewalk that will lead you home, but you hear footsteps in the distance. Do you FOLLOW the sidewalk home, or do you TRACk the footsteps?")
        if choices.lower() == "follow":
            choices = input("You are on your way home when you see a shooting star. Do you TAKE out your camera to capture the beauty or do you CONTINUE to walk home?")
            if choices.lower() == "take":
                print("You capture the shooting star, but you ened up getting home late. YOur parents aren't too happy. Okay choice, but could have made a better one.")
            elif choices.lower() == "continue":
                print("You make it home before your curfew. Your parents are happy and reward you with a nice banana split. Great choice.")
        elif choices.lower() == "track":
            choices = input("You track down the footsteps and find a stray dog. Do you TAKE the dog home, SEND it to the pound, or LEAVE it?")
            if choices.lower() == "take":
                print("Good job, you just added a nice new member to the family.")
            elif choices.lower() == "send":
                print("A family who was looking for the perfect pet, found this dog. Nice job.")
            elif choices.lower() == "leave":
                print("Not sure what ever happened to this dog. But, this isn't the best solution. Better luck next time.")
else:
    print("Sorry, that's not a valid option")
    


