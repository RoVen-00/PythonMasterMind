import os
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [0, 0]

while True:
    #Draw map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_x in range(MAP_WIDTH):
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                print(" @ ", end="")
            else:
                print("   ", end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    #Ask user where he wants to move

    direction = readchar.readchar()
    #print(direction)
    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "d":
        my_position[POS_X] += 1
    elif direction == "q":
        break
    os.system("cls")


