print("Welcome to the treasure Island")
direction = input("You are at the junction, Where do you want to go left or right?\n")
if(direction=='left'):
    print("you have choosen left walk straight and go to the bridge")
    bridge = input("You wann cross the bridge? Y or N\n")
    if(bridge=='y' or bridge=='Y'):
        print("You have walked to the bridge of fire\nBoom! Game Over")
    else:
        print("You did not cross the bridge\nGame Over.")
if(direction=='right'):
    river = input("You are at the river. Boat is arriving, You wanna wait or swim\n")
    if(river=='swim'):
        print("Oops! A shark ate you.\nGame Over.")
    elif(river=='wait'):
        boat=input("You wanna take the boat? Y or N\n")
        if(boat=='y' or boat=='Y'):
            print("You have crossed the river")
            door = input("Which door you would like to choose? Blue, Red or Yellow\n")
            if(door=='blue'):
                print("Oops you fell into the ocean by opening the door of oceans")
            elif(door=='red'):
                print("Oops you fell on fire")
            elif(door=='yellow'):
                print("Hooray! You won the game")