import random
import turtle

x = 0
y = 0

obstacle_position = []
is_coordinate_blocked = False

min_y, max_y = -200, 200
min_x, max_x = -100, 100


def create_top_wall_of_maze(starting_x, top_starting_y, ending_x, ending_y):
    """ Sets the coordinates for the top wall of the maze and creates random coordinates for a door
        Traverses through the coordinates from the starting point to the ending point
        If the counter matches the coordinate of the door, it increments by 4 - skipping that obstacle
        Appends the x and y values into the coordinates list
    """

    global obstacle_position
    global x,y
    door = random.randrange(starting_x + 4, ending_x - 8, 4)

    for i in range(starting_x, ending_x + 2, 4): # Go from the start point to the end point
        if i == door or i == door + 4: # If the door coordinate matches the coordinate that i is traversing
            i += 4
            continue

        wall_x = i
        wall_y = top_starting_y
        new_coordinates = wall_x,wall_y
        obstacle_position.append(new_coordinates) # Append the coordinates of the wall into our empty list


def create_bottom_wall_of_maze(starting_x, starting_y, ending_x, bottom_ending_y):
    """ Sets the coordinates for the bottom wall of the maze and creates random coordinates for a door
        Traverses through the coordinates from the starting point to the ending point
        If the counter matches the coordinate of the door, it increments by 4 - skipping that obstacle
        Appends the x and y values into the coordinates list
    """

    global obstacle_position
    door = random.randrange(starting_x + 4, ending_x - 8, 4)

    for i in range(starting_x, ending_x, 4):
        if i == door or i == door + 4:
            continue
        
        wall_x = i
        wall_y = starting_y
        new_coordinates = wall_x,wall_y
        obstacle_position.append(new_coordinates)


def create_left_wall_of_maze(starting_x, starting_y, left_ending_x, ending_y):
    """ Sets the coordinates for the left wall of the maze and creates random coordinates for a door
        Traverses through the coordinates from the starting point to the ending point
        If the counter matches the coordinate of the door, it increments by 4 - skipping that obstacle
        Appends the x and y values into the coordinates list
    """

    global obstacle_position
    door = random.randrange(starting_y + 4, ending_y - 8, 4)

    for i in range(starting_y, ending_y, 4):
        if i == door or i == door + 4:
            continue

        wall_x = starting_x
        wall_y = i
        new_coordinates = wall_x,wall_y
        obstacle_position.append(new_coordinates)


def create_right_wall_of_maze(right_starting_x, starting_y, ending_x, ending_y):
    """ Sets the coordinates for the right wall of the maze and creates random coordinates for a door
        Traverses through the coordinates from the starting point to the ending point
        If the counter matches the coordinate of the door, it increments by 4 - skipping that obstacle
        Appends the x and y values into the coordinates list
    """

    global obstacle_position
    door = random.randrange(starting_y + 4, ending_y - 8, 4)

    for i in range(starting_y, ending_y, 4):
        if i == door or i == door + 4:
            continue

        wall_x = right_starting_x
        wall_y = i
        new_coordinates = wall_x,wall_y
        obstacle_position.append(new_coordinates)


def create_maze():
    """ Setting the coordinates of each wall
        Setting the coordinates of the special cases for each wall
        Calling the functions that create each part of the walls as many times as I want rectangles
        Sets the coordinate values to smaller, so every time the For loop runs the next rectangle is smaller than the previous one
        Returns the coordinates so they can be used by the wall-building functions
    """
    global obstacle_position

    starting_x = -80
    starting_y = -180
    ending_x = 80
    ending_y = 180

    top_starting_y = 180
    bottom_ending_y = -180
    left_ending_x = -80
    right_starting_x = 80

    for number_of_rectangles in range(5): # I want 6 rectangles
        create_top_wall_of_maze(starting_x, top_starting_y, ending_x, ending_y)
        create_bottom_wall_of_maze(starting_x, starting_y, ending_x, bottom_ending_y)
        create_left_wall_of_maze(starting_x, starting_y, left_ending_x, ending_y)
        create_right_wall_of_maze(right_starting_x, starting_y, ending_x, ending_y)

        starting_x += 16
        starting_y += 16
        ending_x -= 16
        ending_y -= 16

        top_starting_y -= 16
        bottom_ending_y += 16
        left_ending_x += 16
        right_starting_x -= 16


def get_obstacles():
    """ Returns a list of the maze obstacles to be used in the functions below and in world.py
    """
    create_maze()
    return obstacle_position


def is_position_blocked(x,y):
    """ Compares the current X coordinate and the X coordinate in the list of obstacles. 
        If any part of the current X is touching any part of the obstacle (which is 4 x 4), the function returns True
    """

    global is_coordinate_blocked
    global obstacle_position
    obstacle_list = obstacle_position

    for coordinates in obstacle_list:
        if (x >= coordinates[0] and x <= coordinates[0] + 4) and (y >= coordinates[1] and y <= coordinates[1] + 4): # If the x or y coordinate is the same as an obstacle
            is_coordinate_blocked = True # The position is blocked

    return is_coordinate_blocked


def is_path_blocked(x1, y1, x2, y2): 
    """ Adds a fix for negative and positive numbers because the range() method doesn't allow traversing negatives. 
        If the old X is smaller than the new X, use 1. If it's bigger then use -1.
        Traverses through all of the X coordinates
        Traverses through all of the Y coordinates
        If the previous function returns that a positon is blocked, this function returns True too
    """

    global is_coordinate_blocked

    direction_x = 1 if x1 < x2 else -1
    direction_y = 1 if y1 < y2 else -1

    for x in range(x1, x2 + direction_x, direction_x):
        for y in range(y1, y2 + direction_y, direction_y):
            if is_position_blocked(x, y):
                is_coordinate_blocked = True
    return is_coordinate_blocked
