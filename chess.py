import turtle 
wn = turtle.Screen()
wn.bgcolor("blue")
board_builder = turtle.Turtle()
board_builder.penup()
coords = [-73.5,73.5] 
board_builder.right(90)
board_builder.shape("square")
board_builder.color("tan")
board_builder.hideturtle()
grid = [[],[],[],[],[],[],[],[]]

#board builder code xd

for i in range(8):
    board_builder.teleport(coords[0],coords[1])
    coords[0] += 21
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                board_builder.color("tan")
            else:
                board_builder.color("brown")
        else:
            if j % 2 == 0:
                board_builder.color("brown")
            else:
                board_builder.color("tan")
        board_builder.stamp()
        square = board_builder.pos()
        grid[i].append(square)
        board_builder.forward(21)

#captured area code

white_jail_builder = turtle.Turtle()
white_jail_builder.shape("square")
white_jail_builder.color("gray")
white_jail_builder.penup()
black_jail_builder = turtle.Turtle()
black_jail_builder.shape("square")
black_jail_builder.color("gray")
black_jail_builder.penup()

white_jail_coords = []
black_jail_coords = []

white_jail_builder.teleport(-73.5,125.5)
white_jail_builder.hideturtle()
for i in range(16):
    if i == 8:
        white_jail_builder.teleport(-73.5,146.5)
    white = white_jail_builder.pos()
    white_jail_coords.append(white)
    white_jail_builder.stamp()
    white_jail_builder.forward(21)

black_jail_builder.teleport(-73.5,-125.5)
black_jail_builder.hideturtle()
for i in range(16):
    if i == 8:
        black_jail_builder.teleport(-73.5,-146.5)
    black = black_jail_builder.pos()
    black_jail_coords.append(black)
    black_jail_builder.stamp()
    black_jail_builder.forward(21)

###################

positions = []
possible_positions = []

for i in range(27):
    position = turtle.Turtle()
    position.color("green")
    position.shape("square")
    position.teleport(500,500)
    positions.append(position)

#end of board builder code

white_pawns = []
black_pawns = []

#piece generator

for i in range(8):
    bpawn = turtle.Turtle()
    black_pawns.append([bpawn,"bpawn",1])
    bpawn.shape("circle")
    bpawn.color("black")
    bpawn.turtlesize(0.6)
    bpawn.teleport(grid[i][6][0],grid[i][6][1])
for i in range(8):
    wpawn = turtle.Turtle()
    white_pawns.append([wpawn,"wpawn",1])
    wpawn.shape("circle")
    wpawn.color("white")
    wpawn.turtlesize(0.6)
    wpawn.teleport(grid[i][1][0],grid[i][1][1])
#for i in range(2):
   # brook = turtle.Turtle()
  #  brook

piece = False
turn = False

#function for pawn positions###################################################################################################

def pawnfunc(item,item_coord):
    if item[1] == "bpawn": #code for finding possible positions for black pawns
        for thing in white_pawns:
            enemy_coord = thing[0].pos()
            if ((item_coord[0] - 21 < enemy_coord[0] + 5) and (item_coord[0] - 21 > enemy_coord[0] - 5)) and (item_coord[1] + 21 == enemy_coord[1]):
                positions[0].teleport(enemy_coord[0],enemy_coord[1])
                possible_positions.append(positions[0])
                positions.remove(positions[0])
            elif ((item_coord[0] + 21 < enemy_coord[0] + 5) and (item_coord[0] + 21 > enemy_coord[0] - 5)) and (item_coord[1] + 21 == enemy_coord[1]):
                positions[0].teleport(enemy_coord[0],enemy_coord[1])
                possible_positions.append(positions[0])
                positions.remove(positions[0])
        front = 0
        for cat in black_pawns:
            cat_coord = cat[0].pos()
            if ((cat_coord[0] < item_coord[0] + 5) and (cat_coord[0] > item_coord[0] - 5)) and (cat_coord[1] == item_coord[1] + 21):
                front += 1
        for dog in white_pawns:
            dog_coord = dog[0].pos()
            if ((dog_coord[0] < item_coord[0] + 5) and (dog_coord[0] > item_coord[0] - 5)) and (dog_coord[1] == item_coord[1] + 21):
                front += 1
        if (item_coord[1] + 21 > 73.5) or (item_coord[1] - 21 < -73.5):
            front += 1
        if front == 0:
            positions[0].teleport(item_coord[0],item_coord[1] + 21)
            possible_positions.append(positions[0])
            positions.remove(positions[0])
        if item[2] == 1:
            front2 = 0
            for cat in black_pawns:
                cat_coord = cat[0].pos()
                if (cat_coord[0] == item_coord[0]) and (cat_coord[1] == item_coord[1] + 42):
                    front2 += 1
            for dog in white_pawns:
                dog_coord = dog[0].pos()
                if (dog_coord[0] == item_coord[0]) and (dog_coord[1] == item_coord[1] + 42):
                    front2 += 1
            if front2 == 0:
                positions[0].teleport(item_coord[0],item_coord[1] + 42)
                possible_positions.append(positions[0])
                positions.remove(positions[0])
    else: #code for finding possible positions for white pawns
        for thing in black_pawns:
            enemy_coord = thing[0].pos()
            if ((item_coord[0] - 21 < enemy_coord[0] + 5) and (item_coord[0] - 21 > enemy_coord[0] - 5)) and (item_coord[1] - 21 == enemy_coord[1]):
                positions[0].teleport(enemy_coord[0],enemy_coord[1])
                possible_positions.append(positions[0])
                positions.remove(positions[0])
            elif ((item_coord[0] + 21 < enemy_coord[0] + 5) and (item_coord[0] + 21 > enemy_coord[0] - 5)) and (item_coord[1] - 21 == enemy_coord[1]):
                positions[0].teleport(enemy_coord[0],enemy_coord[1])
                possible_positions.append(positions[0])
                positions.remove(positions[0])
        front = 0
        for cat in black_pawns:
            cat_coord = cat[0].pos()
            if ((cat_coord[0] < item_coord[0] + 5) and (cat_coord[0] > item_coord[0] - 5)) and (cat_coord[1] == item_coord[1] - 21):
                front += 1
        for dog in white_pawns:
            dog_coord = dog[0].pos()
            if ((dog_coord[0] < item_coord[0] + 5) and (dog_coord[0] > item_coord[0] - 5)) and (dog_coord[1] == item_coord[1] - 21):
                front += 1
        if (item_coord[1] + 21 > 73.5) or (item_coord[1] - 21 < -73.5):
            front += 1
        if front == 0:
            positions[0].teleport(item_coord[0],item_coord[1] - 21)
            possible_positions.append(positions[0])
            positions.remove(positions[0])
        if item[2] == 1:
            front2 = 0
            for cat in black_pawns:
                cat_coord = cat[0].pos()
                if (cat_coord[0] == item_coord[0]) and (cat_coord[1] == item_coord[1] - 42):
                    front2 += 1
            for dog in white_pawns:
                dog_coord = dog[0].pos()
                if (dog_coord[0] == item_coord[0]) and (dog_coord[1] == item_coord[1] - 42):
                    front2 += 1
            if front2 == 0:
                positions[0].teleport(item_coord[0],item_coord[1] - 42)
                possible_positions.append(positions[0])
                positions.remove(positions[0])
        
###############################################################################################################################        
    

def click(x,y):
    global turn
    global piece
    for item in possible_positions:
        position_coord = item.pos()
        if (position_coord[0] < x + 10 and position_coord[0] > x - 10) and (position_coord[1] < y + 10 and position_coord[1] > y - 10):
            piece[0].penup()
            piece[0].goto(position_coord[0],position_coord[1])
            piece[2] = 0
            piece_coord = piece[0].pos()
            if turn == False:
                for item in white_pawns:
                    white_pawn_coord = item[0].pos()
                    if (piece_coord[0] < white_pawn_coord[0] + 5) and (piece_coord[0] > white_pawn_coord[0] - 5) and (piece_coord[1] == white_pawn_coord[1]):
                        item[0].teleport(black_jail_coords[0][0],black_jail_coords[0][1])
                        black_jail_coords.remove(black_jail_coords[0])
                turn = True
            else:
                for item in black_pawns:
                    black_pawn_coord = item[0].pos()
                    if (piece_coord[0] < black_pawn_coord[0] + 5) and (piece_coord[0] > black_pawn_coord[0] - 5) and (piece_coord[1] == black_pawn_coord[1]):
                        item[0].teleport(white_jail_coords[0][0],white_jail_coords[0][1])
                        white_jail_coords.remove(white_jail_coords[0])
                turn = False
    for item in possible_positions:
        item.teleport(500,500)
    for pops in possible_positions:
        positions.append(pops)
        possible_positions.remove(pops)
    for item in black_pawns:
        item[0].color("black")
    for item in white_pawns:
        item[0].color("white")
    if turn == False:
     for item in black_pawns:
        item_coord = item[0].pos()
        if (item_coord[0] < x + 5 and item_coord[0] > x - 5) and (item_coord[1] < y + 5 and item_coord[1] > y - 5):
            item[0].color("green")
            piece = item
            if item[1] == "bpawn":
                pawnfunc(item,item_coord)
    else:
     for item in white_pawns:
        item_coord = item[0].pos()
        if (item_coord[0] < x + 5 and item_coord[0] > x - 5) and (item_coord[1] < y + 5 and item_coord[1] > y - 5):
            item[0].color("green")
            piece = item
            if item[1] == "wpawn":
                pawnfunc(item,item_coord)



turtle.onscreenclick(click)
    
turtle.done()
