
import sys
import robot

obstacles_ls = [()]

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def get_position():
    global position_x, position_y
    return position_x, position_y


def set_direction(setter_current_direction_index):
    global current_direction_index
    current_direction_index = setter_current_direction_index


def get_direction_index():
    global current_direction_index
    return current_direction_index


def show_position(robot_name):
    print(' > '+robot_name+' now at position (' +
          str(position_x)+','+str(position_y)+').')


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def obstacle_found_in_path():
    return True


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y, current_direction_index, directions, obstacles_ls
    #obstacles_ls = obstacles.get_obstacles()
    #print (f"world position{obstacles_ls}")
    # obstacles.set_obstacles(obstacles_ls)
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    #obstacles_ls = obstacles.get_obstacles()

    if is_position_allowed(new_x, new_y) and (robot.obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == False):
        position_x = new_x
        position_y = new_y
        return True
    elif is_position_allowed(new_x, new_y) == False and (robot.obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == False):
        return "boundary"
    elif (robot.obstacles.is_path_blocked(position_x, position_y, new_x, new_y) == True):
        return "found"


def start_world():
    global obstacles_ls, position_x, position_y, current_direction_index

    position_x = 0
    position_y = 0

    current_direction_index = 0
    generate_obstacles()


def generate_obstacles():
    obstacles_ls = robot.obstacles.generate_obstacles()
    if obstacles_ls:
        print("There are some obstacles:")
        for obs in obstacles_ls:
            print(
                f"- At position {obs[0]},{obs[1]} (to {obs[0] + 4},{obs[1] + 4})")
