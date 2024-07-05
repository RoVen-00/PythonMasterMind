import readchar as readchar
import random
import os
def clear(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":\
                os.system ("cls")
#3 caracter in x axis = 1 unit in x axis
"""\
   XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      XXX   XXX   XXX   XXX   XXX   XXXXXX   XXXXXX      XXX
XXX         XXX   XXX      XXX         XXX            XXXXXX
XXXXXXXXX   XXX         XXX      XXX   XXX   XXXXXX   XXXXXX
XXXXXXXXX      XXX   XXX   XXX   XXX   XXX   XXXXXX   XXXXXX
XXXXXXXXXXXX         XXX         XXX         XXX         XXX
XXXXXXXXXXXX   XXX   XXX   XXXXXXXXXXXX   XXX      XXX   XXX
XXXXXX         XXXXXXXXX   XXX   XXX            XXXXXX   XXX
XXXXXXXXXXXX   XXX   XXX   XXX   XXX   XXXXXX   XXX   XXXXXX
XXXXXXXXXXXX               XXX   XXX   XXXXXX   XXX   XXXXXX
XXXXXXXXXXXXXXXXXX   XXX         XXX   XXXXXX   XXX   XXXXXX
XXX                        XXX         XXX               
XXXXXX   XXXXXXXXXXXXXXXXXXXXX   XXXXXXXXX   XXXXXXXXX   XXX
XXXXXX                           XXXXX                   XXX
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\
"""
#1character in x axis = 1 unit in x axis
obstacle_definition ="""\
 XXXXXXXXXXXXXXXXXXX
  X X X X X XX XX  X
X   X X  X   X    XX
XXX X   X  X X XX XX
XXX  X X X X X XX XX
XXXX   X   X   X   X
XXXX X X XXXX X  X X
XX   XXX X X    XX X
XXXX X X X X XX X XX
XXXX     X X XX X XX
XXXXXX X   X XX X XX
X        X   X      
XX XXXXXXX XXX XXX X
XX         XX      X
XXXXXXXXXXXXXXXXXXXX\
"""
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_X = len(obstacle_definition[0])
MAP_Y = len(obstacle_definition)
X = 0
Y = 1
while True:
    my_position = [0,0]
    game_objets = []
    tail_length = 0
    tail = []
    input_ok = False
    while input_ok == False:
        NUMBER_OF_OBJETS = int(input("Con cuantos objetos quieres jugar?"))
        if NUMBER_OF_OBJETS < MAP_Y*MAP_X and NUMBER_OF_OBJETS > 0 :
            input_ok = True
        else:
            print("No caben tantos objetos en el mapa, intentelo de nuevo")
    while len(game_objets) < NUMBER_OF_OBJETS:
        object_to_introduce =[random.randint(0, MAP_X - 1), random.randint(0, MAP_Y - 1)]
        if object_to_introduce not in game_objets \
                and object_to_introduce != my_position\
                and obstacle_definition[object_to_introduce[Y]][object_to_introduce[X]] != "X":
            game_objets.append(object_to_introduce)
    clear()
    restart = False
    while restart == False:
        if len(game_objets) == 0:
            while len(game_objets) < NUMBER_OF_OBJETS:
                object_to_introduce = [random.randint(0, MAP_X - 1), random.randint(0, MAP_Y - 1)]
                if object_to_introduce not in game_objets \
                        and object_to_introduce not in tail \
                        and object_to_introduce != my_position\
                        and obstacle_definition[object_to_introduce[Y]][object_to_introduce[X]] != "X":
                    game_objets.append(object_to_introduce)
        print("+"+"---"*MAP_X+"+"+" {} points.".format(tail_length))
        for coordinate_y in range(MAP_Y):
            print("|",end="")
            for coordinate_x in range(MAP_X):
                chart_to_draw = "   "
                if [coordinate_x,coordinate_y] in game_objets:
                    chart_to_draw = " * "
                if [coordinate_x,coordinate_y] == my_position:
                    chart_to_draw = " @ "
                if [coordinate_x,coordinate_y] in tail:
                    chart_to_draw = " # "
                if obstacle_definition[coordinate_y][coordinate_x] == "X":
                    chart_to_draw = "XXX"
                print(chart_to_draw,end="")
            print("|")
        print("+"+"---"*MAP_X+"+")

        # -----------------------------------------------------------------------------------------
        """# control de movimiento consola"""
        print(" W    Q to exit \nASD")
        direction = readchar.readchar().lower()

        """#control de movimiento pycharm"""
       # direction = input(" W    Q to exit \nASD").lower()
        clear()
        # -----------------------------------------------------------------------------------------
        #aplicacion del movimiento en x o y
        # -----------------------------------------------------------------------------------------
        next_position = my_position.copy()
        if direction == "w":
            next_position[Y] += -1
            if obstacle_definition[next_position[Y]][next_position[X]] == " ":
                tail.insert(0, my_position.copy())
                my_position[Y] += -1
            else:
                print("No puedes atravezar paredes UwU")

        # -----------------------------------------------------------------------------------------
        elif direction == "s":
            next_position[Y] += 1
            if obstacle_definition[next_position[Y]][next_position[X]] == " ":
                tail.insert(0, my_position.copy())
                my_position[Y] += 1
            else:
                print("No puedes atravezar paredes UwU")
        # -----------------------------------------------------------------------------------------
        elif direction == "a":
            next_position[X] += -1
            if obstacle_definition[next_position[Y]][next_position[X]] == " ":
                tail.insert(0, my_position.copy())
                my_position[X] += -1
            else:
                print("No puedes atravezar paredes UwU")
        # -----------------------------------------------------------------------------------------
        elif direction == "d":
            next_position[X] += +1
            if obstacle_definition[next_position[Y]][next_position[X]] == " ":
                tail.insert(0, my_position.copy())
                my_position[X] += +1
            else:
                print("No puedes atravezar paredes UwU")
        # -----------------------------------------------------------------------------------------
        elif direction == "q":
            exit()
        if len(tail) > tail_length :
            tail.pop()
        while my_position in game_objets:
            for position3 in range(len(game_objets)):
                if game_objets[position3] == my_position:
                    game_objets.pop(position3)
                    tail_length += 1
                    break
        if my_position in tail and tail_length<MAP_X *MAP_Y\
                or my_position[X] >= MAP_X \
                or my_position[Y] >= MAP_Y \
                or my_position[X] < 0 \
                or my_position[Y] < 0 :
            input("You fail.\nPress ``enter´´ to restart.")
            restart = True
            clear()
        elif tail_length == ( MAP_X * MAP_Y )-1:
            input("Congratulation you win\nPress ``enter´´ to restart")
            restart = True
            clear()