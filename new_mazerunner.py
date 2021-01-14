from collections import deque
from math import sqrt
import robot

def two_d_maze(maze, obstacle_ls):

    # Create a 2D array maze using our obstacles

    # maze : a list of lists containing rows
    #     if : obstacle present place 1 otherwise 0
    # returns: our 2D array with obstacles
    for obs in obstacle_ls:
        for y in range(obs[1]+200, obs[1]+205):
            for x in range(obs[0]+100, obs[0]+105):
                try:
                    maze[abs(y)][abs(x)] = 1
                except IndexError:
                    pass
    return maze

def make_graph(maze):
    # maze is a 2D array that is either 0 or 1
    #     1 - Wall
    #     0 - path
    
    # returns: graph (dict) : adjacency matrix about each co-ord 

    height = len(maze)
    width = len(maze[0])

    graph = {(i,j): [] for j in range(width) for i in range(height) if not maze[i][j]}

    for row, col in graph.keys():
        if row < height - 1 and not maze[row + 1][col]:
            graph[(row, col)].append(("N", (row + 1, col)))
            graph[(row + 1, col)].append(("S", (row,col)))

        if col < width - 1 and not maze[row][col + 1]:
            graph[(row, col)].append(("E", (row, col + 1)))
            graph[(row, col + 1)].append(("W", (row, col)))
    
    return graph

def find_end(ends, start):
    # Find our nearest end point 

    # ends : list of ends for specific edge
    # start : start co-ord

    # return : end co-ord that is nearest to start pos
    shortest_dist_pos = None
    shortest_dist = None

    for i in ends:
        dist = sqrt(((start[0] - i[0]) ** 2) + ((start[1] - i[1]) ** 2))
        if shortest_dist is None or dist < shortest_dist:
            shortest_dist = dist
            shortest_dist_pos = i
    
    end = shortest_dist_pos
    return end

def solvable_maze(maze, edge, x, y, obstacle_ls):

    # maze : 2D array init as 0s Only
    # edge: edge to solve to mark with 4  
    # x : start x
    # y : start y

    # returns : start pos co-ord, and end pos co-ord
    global ends
    ends = []

    for y_coord in range(len(maze)):
        for x_coord in range(len(maze[y])):
            if edge == 'bottom':
                maze[0][x_coord] = 4
            
            elif edge == 'right':
                maze[y_coord][200] = 4
            
            elif edge == 'left':
                maze[y_coord][0] = 4
            
            else:
                maze[400][x_coord] = 4
            
    maze = two_d_maze(maze, obstacle_ls)
    maze[y][x] = 5

    for y in range(len(maze)): 
        for x in range(len(maze[y])):
            char = maze[y][x]

            if char == 5:
                start = (y, x)

            if char == 4:
                ends.append((y,x))
            
    end = find_end(ends,start)
    return end,start


def find(x,y,edge,robot_name,obstacle_ls):

    import time
    starttime = time.time()
    maze = [[0 for x in range(201)] for y in range(401)]

    array_maze = two_d_maze(maze, obstacle_ls)

    graph = make_graph(array_maze)
    end,start = solvable_maze(maze,edge,x,y,obstacle_ls)

    que = deque([("",start)])
    visited = set()

    while que:
        path, current = que.popleft()
        if current == end:
            print(f"The endtime was{time.time() - starttime}")
            return path
        if current in visited:
            continue
        visited.add(current)

        for direction,neighbour in graph[current]:
            que.append((path+direction,neighbour))
    return "There is no way out"
