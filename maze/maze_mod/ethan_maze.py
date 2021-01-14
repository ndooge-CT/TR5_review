import random

obstacle_list = []
    
def generate_obstacles():
    """
    Generates a list of tuples containing
    x and y cordinates for obstacles.
    """
    global obstacle_list

    number_of_obstacles = random.randint(3, 9)

    min_x, max_x = -104, 100
    min_y, max_y = -204, 200

    for i in range(0, number_of_obstacles):
        max_x -= 10
        min_x += 10
        min_y += 10
        max_y -= 10

        temp_obstacles = []
        temp_x = []
        temp_y = []

        temp_obstacles.append((max_x, max_y))
        for i in range(min_y, max_y, 4):
            temp_obstacles.append((max_x, i))
            temp_obstacles.append((min_x, i))
            temp_y.append(i)
        for i in range(min_x, max_x, 4):
            temp_obstacles.append((i, min_y))
            temp_obstacles.append((i, max_y))
            temp_x.append(i)

        temp_obstacles.remove((min_x, temp_y[random.randint(0, len(temp_y) - 1)]))
        temp_obstacles.remove((max_x, temp_y[random.randint(0, len(temp_y) - 1)]))
        temp_obstacles.remove((temp_x[random.randint(0, len(temp_x) - 1)], min_y))
        temp_obstacles.remove((temp_x[random.randint(0, len(temp_x) - 1)], max_y))
        obstacle_list += temp_obstacles


def is_position_blocked(x,y):
    """
    Checks to see if the the position
    the robot is trying to go to is blocked
    :param: position of the robots x and y axis
    :return: Boolean
    """

    for obstacle in obstacle_list:
        if (x >= obstacle[0] and x <= (obstacle[0] + 4)) and (y >= obstacle[1] and y <= (obstacle[1] + 4)):
            return True
    
    return False


def is_path_blocked(x1, y1, x2, y2):
    """
    Checks to see if the position the robot
    is trying to go to has any obstacles in between
    it and the new distination if there is an obstacle
    in the way it will return true if there is nothing
    it will return false.
    :param: initial x and y co-ordinates
    :param: new position x and y co-ordinates
    :return: either true or false
    """

    for obstacle in obstacle_list:
        list_of_x = [obstacle[0] + i for i in range(0, 5)]
        list_of_y = [obstacle[1] + i for i in range(0, 5)]

        for x in list_of_x:
            for y in list_of_y:
                if (x >= x1 and x <= x2) and (y >= y1 and y <= y2):
                    return True
                elif (x <= x1 and x >= x2) and (y >= y1 and y <= y2):
                    return True
                elif (x >= x1 and x <= x2) and (y <= y1 and y >= y2):
                    return True
                elif (x <= x1 and x >= x2) and (y <= y1 and y >= y2):
                    return True
    return False


def get_obstacles():
    generate_obstacles()
    return obstacle_list