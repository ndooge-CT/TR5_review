
import random
import math
print("Imported simple_maze successfully")
obstacles_ls = []

min_y, max_y = -200, 200
min_x, max_x = -100, 100


def create_random_maze():
    global obstacles_ls
    
    obstacles_ls = []

    start_x = -90
    end_x = 90
    start_y = -190
    end_y = 186

    levels = 6

    for i in range(levels):
        create_h_line(start_x, end_x, end_y)
        create_h_line(start_x, end_x, start_y)
        create_v_line(start_y, end_y, start_x)
        create_v_line(start_y, end_y, end_x - 4)

        start_x += 14
        end_x -= 14
        start_y += 14
        end_y -= 14
    


def create_h_line(start_x, end_x, end_y):
    door = random.randrange(start_x + 4, end_x - 8, 4)
    doors = (door, end_y)
    
    for i in range(start_x, end_x, 4):
        if i == door or i == door + 4:
            continue
        else:
            point = (i, end_y)
            obstacles_ls.append(point)
    


def create_v_line(start_y, end_y, start_x):
    door = random.randrange(start_y + 4, end_y - 8, 4)
    
    doors = (start_x, door)

    for i in range(start_y, end_y, 4):
        if i == door or i == door + 4:
            continue
        else:
            point = (start_x, i)
            obstacles_ls.append(point)
    

def set_border():
    global min_x, max_x, min_y, max_y
    return min_x, max_x, min_y, max_y


def is_position_blocked(x, y):
    global obstacles_ls

    for my_tuple in obstacles_ls:
        if (my_tuple[0]) <= x <= (my_tuple[0] + 4) and (my_tuple[1]) <= y <= (my_tuple[1]+4):
            return True
    return False
def is_path_blocked(x1, y1, x2, y2):
    dir_x = 1 if x1 < x2 else -1
    dir_y = 1 if y1 < y2 else -1 

    for x in range(x1, x2 + dir_x,dir_x):
        for y in range(y1,y2+dir_y,dir_y):
            if is_position_blocked(x,y):
                return True
    return False


def get_obstacles():
    global obstacles_ls
    create_random_maze()
    return obstacles_ls