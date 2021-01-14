import random
import turtle

obstacles_list = []
doors = []

min_y, max_y = -200, 200
min_x, max_x = -100, 100


def create_random_obstacles():
    """
    Function to generate layered circular maze
    """

    global obstacles_list,doors
    obstacles_list = []
    
    start_x = -99
    end_x = 97
    start_y = -199
    end_y = 197

    
    for i in range(10):
        door_side = random.randint(0,3)

        fill_horizontal(start_x,end_x,end_y-1,door_side,i+1)        #top strip
        fill_horizontal(start_x,end_x,start_y-1,door_side,i+11)     #bottom strip
        fill_vertical(start_y,end_y,start_x-1,door_side,i+1)        #left strip
        fill_vertical(start_y,end_y,end_x-1,door_side,i+11)         #right strip
        
        start_x += 10
        end_x -= 10
        start_y += 10
        end_y -= 10
    
    
def fill_horizontal(start_x,end_x,y,door_side,layer):
    """
    Function to fill in horizontal barriers in maze

    Params:
        start_x: starting x coord of strip
        end_x: ending x coord of strip
        y: y coord of strip
        door_side: randomly generated side to put layer's door on
        layer: int marking both how many layers have been completed and which side of the layer we're on
    """
    if layer is not 1 and layer is not 11:
        if door_side is 0 and layer < 11 or door_side is 1 and layer > 10:
            door = random.randrange(start_x+5,end_x-10,5)
        else:
            door = 0
    else:
        door = random.randrange(start_x+5,end_x-10,5)
    
    for i in range(start_x,end_x,5):
        if i == door or i == door+4:
            if layer < 11 and layer is not 1:
                obstacles_list.append((i-5,y-5))
            elif layer > 10 and layer is not 11:
                obstacles_list.append((i+5,y+5))
            continue
        if i < door:
            point = (i,y) 
        else:
            point = (i,y)
        obstacles_list.append(point)
    doors.append((door,y))

    
def fill_vertical(start_y,end_y,x,door_side,layer):
    """
    Function to fill in vertical barriers in maze

    Params:
        start_y: starting y coord of strip
        end_y: ending y coord of strip
        x: x coord of strip
        door_side: randomly generated side to put layer's door on
        layer: int marking both how many layers have been completed and which side of the layer we're on
    """
    if layer is not 1 and layer is not 11:
        if door_side is 2 and layer < 11 or door_side is 3 and layer > 10:
            door = random.randrange(start_y+5,end_y-10,5)
        else:
            door = 0
    else:
        door = random.randrange(start_y+5,end_y-10,5)
    
    for i in range(start_y,end_y,5):
        if i == door or i == door+4:
            if layer < 11 and layer is not 1:
                obstacles_list.append((x+5,i+5))
            elif layer > 10 and layer is not 11:
                obstacles_list.append((x-5,i-5))
            continue
        if i < door:
            point = (x,i)
        else:
            point = (x,i)
        obstacles_list.append(point)
    doors.append((x,door))


def is_position_blocked(x, y):
    """
    Function to detect if coord is inside obstacle
    """
    for obs in obstacles_list:
        if x in range(obs[0],obs[0]+5) and y in range(obs[1],obs[1]+5):
            return True
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Function to detect if any point in path is blocked by obstacle
    """
    dir_x = 1 if x1 < x2 else -1
    dir_y = 1 if y1 < y2 else -1
    
    for x in range(x1,x2+dir_x,dir_x):
        for y in range(y1,y2+dir_y,dir_y):
            if is_position_blocked(x,y):
                return True
    return False


def get_obstacles():
    """
    Function to return list of all obstacles
    """
    create_random_obstacles()
    return obstacles_list


def get_doors():
    return doors