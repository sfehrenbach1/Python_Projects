#Treasure Hunt Adventure Game

print(''' _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|\n\n\n''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")

cave_direction = input("You are in a dark cave. You see a tiny hole of light to your left and a dark corridor to your right. Which way do you go? 'Left' or 'Right'?\n")

if cave_direction == "left" or cave_direction == "Left":
    kitchen_direction = input("You walk towards the light and find yourself in a kitchen with a boiling pot. You hear a voice in the distance. It sounds like it is getting closer. Do you hide in the boiling pot or wait. 'Hide' or 'Wait'?\n")

    if kitchen_direction == "wait" or kitchen_direction == "Wait":
        wizard_choice = input("You decide to wait and are greeted by the powerful wizard Merlin. He claims to have a map that has the directions to the treasure and offers to give it to you. Do you accept the map? 'Yes' or 'No'?\n")

        if wizard_choice == "Yes" or wizard_choice == "yes":
            map_choice = input("You accept the Merlin's map and continue your adventure. You follow the map to a room with 3 colored doors. 'Red', 'Blue', 'White'. Which door do you choose to walk through?\n")

            if map_choice == "Red" or map_choice == "red":
                print("You open the door and get hit by blazing fire coming from a dragon's mouth. You turn into ashes. Game over.")

            elif map_choice == "Blue" or map_choice == "blue":
                print("You walk into a room and the door locks behind you. The room is so cold and you end up freezing to death. Game over.")

            elif map_choice == "White" or map_choice == "white":
                print("Congratulations!! You have completed your mission of finding the treasure of Treasure Island.")

            else:
                print("Please choose an option from the list next time. Game over.")

        else:
            print("You decide to slap the map out of Merlin's hands and he turns you into a frog. Game over.")

    else:
        print("Did you really think hiding in a boiling pot was a good idea? Game over.")
   
else:
    print("You fall into a pit of spikes. Game over.")