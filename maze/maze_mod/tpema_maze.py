import random

obstacles = []

def create_obstacles(min_x, min_y, max_x, max_y):
    """Randomly generates obstacles within the limitation range and adds them to a list.
    Obstacle coordinates start from the bottom left position.
    Randomizes new obstacles if obstacle already exists

    Returns:
        obstacles [list]: returns the list of randomly generated obstacles
    """
    global obstacles
    obstacles = []
    obstacles = create_maze(min_x-4, min_y-4, max_x, max_y)
    return obstacles


def create_grid(min_x, min_y, max_x, max_y):
    grid = []
    for i in range(min_x, max_x+1, 4):
        for j in range(min_y, max_y+1, 4):
            grid.append((i, j))
    return grid


def is_position_blocked(x,y):
    """Checks if the position the robot is at is occupied by an obstacle.
    Returns True is the position is occupied

    Args:
        x [int]: Current position on the x-axis
        y [int]: Current position on the y-axis

    Returns:
        [Boolean]: Returns True is the position is occupied by an obstacle
    """
    for m, n in obstacles:
        if x in range(m, m+5) and y in range(n, n+5):
            return True
    return False
    

def is_path_blocked(x1, y1, x2, y2):
    """Checks if there is an obstacle along the path that the robot wants to move.
    Takes the starting and ending coordinates of the the robot and checks all lines inbetween for an obstacle
    Returns True if there is an obstacle along the path

    Args:
        x1 [int]: Starting position of x-axis
        y1 [int]: Starting position of y-axis
        x2 [int]: Ending position of x-axis
        y2 [int]: Endingg position of y-axis

    Returns:
        [Boolean]: Returns True if the is an obstacle that lies inbetween the starting position and the ending position
    """
    for m, n in obstacles:
        for i in range(5):
            if m+i in range(min(x1,x2), max(x1,x2)+1) and n+i in range(min(y1,y2), max(y1,y2)+1):
                return True
    return False


def get_obstacles():
    """Generates obstacles and returns it as a list

    Returns:
        obstacles [list]: returns list of all randomly generated obstacles
    """
    global obstacles
    if len(obstacles)==0:
        obstacles = create_maze(-100, -200, 100, 200)
    return obstacles


def create_maze(min_x, min_y, max_x, max_y):
    frontier =[]
    maze = []
    visited = []
    x, y = 0, 0
    # x = random.randint(min_x, max_x+1)
    # y = random.randint(min_y, max_y+1)
    visited = [(x, y)]
    maze = [(x, y)]

    f2 = [(x+8, y),(x-8, y),(x, y+8),(x, y-8)]
    for i in f2:
        tx, ty = i
        if tx in range(min_x, max_x+1) and ty in range(min_y, max_y+1):
            frontier.append((tx, ty))
     
    while frontier: # continues until frontier list empty
        rand = random.randint(0, len(frontier)-1)
        x, y = frontier.pop(rand)
        
        f2 = [(x+8, y),(x-8, y),(x, y+8),(x, y-8)]
        f1 = [(x+4, y),(x-4, y),(x, y+4),(x, y-4)]

        ran = [0, 1, 2, 3]
        random.shuffle(ran)
        for i in ran:
            tx, ty = f2[i]
            if (tx in range(min_x, max_x+1) and ty in range(min_y, max_y+1)) and (tx, ty) in visited:
                visited.append(f1[i])
                visited.append((x, y))
                maze.append(f1[i])
                maze.append((x, y))
                break # exits out of for loop as soon as it joins 2 cells

        for i in f2: # adds new frontier cells from current x, y
            tx, ty = i
            if (tx in range(min_x, max_x+1) and ty in range(min_y, max_y+1)) and ((tx, ty) not in visited and (tx, ty) not in frontier):
                frontier.append((tx, ty))

    grid = create_grid(min_x, min_y, max_x, max_y)
    new_maze = []
    for i in grid:
        if i in maze:
            new_maze.append(i)

    for i in new_maze:
        grid.remove(i)
    new_maze = []
    for i in grid:
        tx, ty = i
        if tx in range(-8, 8) and ty in range(-8, 8):
            new_maze.append(i)
    
    for i in new_maze:
        grid.remove(i)

    return grid
