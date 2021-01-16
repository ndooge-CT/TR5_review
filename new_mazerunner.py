from collections import deque
from math import sqrt
import robot

#R, C  .. R = Number of rows, C = Number of col
#m = char matrix of size R X C
#prev : {co-ord: previous position}
#visited : list of co-ords visited already
#Q position to move to next list 
#RQ, RC = row Q, col Q 
#adjacency matrix : co-ord with info about neighbors : eg: {[id / co-ord],[direction: {N: 0 , E: 1, S: 0 , W: 0}}
#eg: [(x,y) :  {N: 0 , E: 1, S: 0 , W: 0} ] 
#for each co ord we need to know if the position is blocked to see if we can move there
#1 = wall / obstacle , 0: walkable path

#start co-ord : current position
#end co-ord : find_edge

#add start to Q
#add child-nodes to Q
#pop start
#add child-child nodes to Q

#reached_end : (boolean) flag for if we reach desired edge

def find_edge(edge):
	return ends
	end_points = []
	
	if edge == 'top' or edge == '':
		for x in range(-100,100,1):
			if robot.obstacles.is_position_blocked(x,200) == False:
				end_points.append(x, 200)
		return end_points		
	elif edge == 'right':
		for y in range(-200,200,1):
			if robot.obstacles.is_position_blocked(-100,y) == False:
				end_points.append(-100, y)
		return end_points		
	elif edge == 'bottom':
		for x in range(-100,100,1):
			if robot.obstacles.is_position_blocked(x,-200) == False:
				end_points.append(x, -200)
		return end_points		
	else edge == 'left':
		for y in range(-200,200,1):
			if robot.obstacles.is_position_blocked(-100,y) == False:
				end_points.append(-100,y)
		return end_points		


def make_adjacency_matrix(obs_ls):
	#adj_dict 
	#{ 0, 0: {N: 0, E: 0, S: 0, W: 0}}
	adj_dict = {}
	temp = {}
	for x in range(-100, 100, 1):
		for y in range(-200,200,1):
			adj_dict[x,y] = {}
			adj_dict[x,y]['N'] = 0
			adj_dict[x,y]['E'] = 0
			adj_dict[x,y]['S'] = 0
			adj_dict[x,y]['W'] = 0

def is_end(ends, current):
	if current in ends:
		return True
	return False

def main_bfs(robot_name, start, edge, obs_ls):
	#ends - list of valid end co-ords
	#start - origin x,y
	#obs_ls : list of obs
	#prev : dict containing previous co-ord for use in backtracking path
	#visted : list of co-ords already visited
	#Qx, Qy: parallel q of nodes still to be visited - start with start , enque open neighbours
	#end_found: boolean: flag for when end is reached. true / false : using edge and is_end(ends , current)
	end_found = False
	q.append(start_x,start_y)
	
	while not end_found():
		current = q.deque()
		
 
