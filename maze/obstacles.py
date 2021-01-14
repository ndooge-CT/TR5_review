
import random
import math
print("Imported obstacles by default")
#from text import world as world
obstacles_ls = []

min_y, max_y = -200, 200
min_x, max_x = -100, 100


def set_obstacles(obs_ls):
    obstacles_ls = obs_ls


def get_boundaries():
    global min_y, min_x, max_y, max_x
    return min_y, min_x, max_y, max_x


def generate_obstacles():
    global obstacles_ls
    obstacles_ls = []
    rand_range = random.randint(0, 10)
    obstacles_ls = [(random.randint(min_x, max_x), random.randint(min_y, max_y))
                    for i in range(rand_range)]
    return obstacles_ls


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

    if obstacles_ls:
        return obstacles_ls
    else:
        return generate_obstacles()