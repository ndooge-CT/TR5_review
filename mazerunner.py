import robot
"""
find wall
move to wall
find door 
move to door
move through door
find next wall
move there
find next door
move through it
until end 

"""
final_dest = False


def move_to_wall_n(n_wall_x, n_wall_y, robot_name):
    x_pos, y_pos = robot.world.get_position()
    
    steps = n_wall_y - y_pos - 1
    flag, output = robot.do_forward(robot_name, steps)
    print(output)
    print(robot.world.show_position(robot_name))


def move_to_wall_e(e_wall_x, e_wall_y, robot_name):
    x_pos, y_pos = robot.world.get_position()
    
    steps = e_wall_x - x_pos - 1
    flag, output = robot.do_forward(robot_name, steps)
    print(output)
    print(robot.world.show_position(robot_name))


def move_to_wall_s(s_wall_x, s_wall_y, robot_name):
    x_pos, y_pos = robot.world.get_position()
    
    steps = y_pos - s_wall_y - 1
    flag, output = robot.do_forward(robot_name, steps)
    print(output)
    print(robot.world.show_position(robot_name))


def move_to_wall_w(w_wall_x, w_wall_y, robot_name):
    x_pos, y_pos = robot.world.get_position()
    
    steps = x_pos - w_wall_x - 1
    flag, output = robot.do_forward(robot_name, steps)
    print(output)
    print(robot.world.show_position(robot_name))

    """we have found our first wall , now we seek an opening
    looking for a path from our y-pos, we search through potential 'doors'
    """

def find_door_n(n_wall_y):
    door_found = False
    door_ls = []
    print ("n_wall_y", + n_wall_y)

    print (robot.world.get_position())
    
    for i in range(-100, 100):
        if (robot.obstacles.is_position_blocked(i,n_wall_y) == False):
                point = (i, n_wall_y)
                door_ls.append(point)
    #determine nearest door location - move to it if possible
    #if not accessable - find door on e, if not possible  then S, lastly W. 
    print (door_ls)
    return door_ls

def find_door_e(e_wall_x):
    door_found = False
    door_ls = robot.obstacles.get_doors()

    while door_found is False:
        for i in range(-200, 200):
            if (e_wall_x, i) in door_ls:
                return i


def find_door_s(s_wall_y):
    door_found = False
    door_ls = robot.obstacles.get_doors()
    
    while door_found is False:
        for i in range(-100, 100):
            if (i, s_wall_y - 4) in door_ls:
                return i


def find_door_w(w_wall_x):
    door_found = False
    door_ls = robot.obstacles.get_doors()
    
    while door_found is False:
        for i in range(-200, 200):
            if (w_wall_x - 4, i) in door_ls:
                return i


def move_to_door_n(x_door, robot_name):
    x_pos, y_pos = robot.world.get_position()

    if x_pos < x_door:
        # move right ++
        flag, output = robot.do_right_turn(robot_name)
        print(output)
        steps = x_door - x_pos
        flag, output = robot.do_forward(robot_name, steps)
        print(output)
        print(robot.world.show_position(robot_name))

    elif x_pos > x_door:
        # move left --
        flag, output = robot.do_left_turn(robot_name)

        print(output)
        steps = x_pos - x_door + 2
        flag, output = robot.do_forward(robot_name, steps)
        print(output)
        print(robot.world.show_position(robot_name))

    elif x_pos == x_door:
        if robot.obstacles.is_position_blocked(x_pos + 1, y_pos+1) is False:
            # move right 1 unit.
            flag, output = robot.do_right_turn(robot_name)

            print(output)
            flag, output = robot.do_forward(robot_name, 1)
            print(output)
            print(robot.world.show_position(robot_name))

            flag, output = robot.do_left_turn(robot_name)

            print(output)

        elif robot.obstacles.is_position_blocked(x_pos - 1, y_pos + 1) is False:
            # move left
            flag, output = robot.do_left_turn(robot_name)

            print(output)
            flag, output = robot.do_forward(robot_name, 1)
            print(output)
            print(robot.world.show_position(robot_name))

            flag, output = robot.do_right_turn(robot_name)
            print(output)

    return True


def move_to_door_e(y_door, robot_name):
    x_pos, y_pos = robot.world.get_position()

    if y_pos < y_door:
        # move up
        flag, output = robot.do_left_turn(robot_name)
        print(output)
        steps = y_door - y_pos + 2
        flag, output = robot.do_forward(robot_name, steps)
        print(output)

        print(robot.world.show_position(robot_name))
        flag, output = robot.do_right_turn(robot_name)
        print(output)

    elif y_pos > y_door:
        # move down
        flag, output = robot.do_right_turn(robot_name)

        print(output)
        steps = y_pos - y_door
        flag, output = robot.do_forward(robot_name, steps)
        print(output)

        print(robot.world.show_position(robot_name))
        flag, output = robot.do_left_turn(robot_name)

        print(output)

    elif y_pos == y_door:
        if robot.obstacles.is_position_blocked(x_pos + 1, y_pos+1) is False:
            # move right 1 unit.
            flag, output = robot.do_right_turn(robot_name)

            print(output)
            flag, output = robot.do_forward(robot_name, 1)
            print(output)
            print(robot.world.show_position(robot_name))

            flag, output = robot.do_left_turn(robot_name)

            print(output)

        elif robot.obstacles.is_position_blocked(x_pos - 1, y_pos + 1) is False:
            # move left
            flag, output = robot.do_left_turn(robot_name)

            print(output)
            flag, output = robot.do_forward(robot_name, 1)
            print(output)
            print(robot.world.show_position(robot_name))

            flag, output = robot.do_right_turn(robot_name)
            print(output)

    return True


def move_to_door_s(x_door, robot_name):
    x_pos, y_pos = robot.world.get_position()

    if x_pos < x_door:
        # move right ++
        flag, output = robot.do_left_turn(robot_name)
        print(output)
        steps = x_door - x_pos + 2
        flag, output = robot.do_forward(robot_name, steps)
        print(output)
        print(robot.world.show_position(robot_name))
        flag, output = robot.do_right_turn(robot_name)
        print(output)

    elif x_pos > x_door:
        # move left --
        flag, output = robot.do_right_turn(robot_name)

        print(output)
        steps = x_pos - x_door + 2
        flag, output = robot.do_forward(robot_name, steps)
        print(output)
        print(robot.world.show_position(robot_name))
        flag, output = robot.do_left_turn(robot_name)
        print(output)

    elif x_pos == x_door:
        if robot.obstacles.is_position_blocked(x_pos + 1, y_pos+1) is False:
            # move right 1 unit.
            flag, output = robot.do_right_turn(robot_name)

            print(output)
            flag, output = robot.do_forward(robot_name, 1)
            print(output)
            print(robot.world.show_position(robot_name))

            flag, output = robot.do_left_turn(robot_name)

            print(output)

        elif robot.obstacles.is_position_blocked(x_pos - 1, y_pos + 1) is False:
            # move left
            flag, output = robot.do_left_turn(robot_name)

            print(output)
            flag, output = robot.do_forward(robot_name, 1)
            print(output)
            print(robot.world.show_position(robot_name))

            flag, output = robot.do_right_turn(robot_name)
            print(output)

    return True


def move_to_door_w(y_door, robot_name):
    x_pos, y_pos = robot.world.get_position()

    if y_pos < y_door:
        # move up
        flag, output = robot.do_right_turn(robot_name)
        print(output)
        steps = y_door - y_pos
        flag, output = robot.do_forward(robot_name, steps)
        print(output)
        print(robot.world.show_position(robot_name))
        flag, output = robot.do_left_turn(robot_name)
        print(output)

    elif y_pos > y_door:
        # move down
        flag, output = robot.do_left_turn(robot_name)

        print(output)
        steps = y_pos - y_door + 2
        flag, output = robot.do_forward(robot_name, steps)
        print(output)
        print(robot.world.show_position(robot_name))
        flag, output = robot.do_right_turn(robot_name)
        print(output)

    elif y_pos == y_door:
        if robot.obstacles.is_position_blocked(x_pos + 1, y_pos+1) is False:
            # move right 1 unit.
            flag, output = robot.do_right_turn(robot_name)

            print(output)
            flag, output = robot.do_forward(robot_name, 1)
            print(output)
            print(robot.world.show_position(robot_name))

            flag, output = robot.do_left_turn(robot_name)

            print(output)

        elif robot.obstacles.is_position_blocked(x_pos - 1, y_pos + 1) is False:
            # move left
            flag, output = robot.do_left_turn(robot_name)

            print(output)
            flag, output = robot.do_forward(robot_name, 1)
            print(output)
            print(robot.world.show_position(robot_name))

            flag, output = robot.do_right_turn(robot_name)
            print(output)

    return True


def find_n_wall():
    final_dest = False
    x_pos, y_pos = robot.world.get_position()
    n_wall = []
    if robot.obstacles.is_path_blocked(x_pos, y_pos, x_pos, 200) is False:
        
        final_dest = True
        n_wall_x = x_pos
        n_wall_y = 201
        return n_wall_x, n_wall_y

    for i in range(y_pos, 201):

        if robot.obstacles.is_position_blocked(x_pos, i) is True:
            n_wall_x = x_pos
            n_wall_y = (i)
            n_wall = (n_wall_x, n_wall_y)
            
            break
    return n_wall_x, n_wall_y


def find_e_wall():
    final_dest = False
    x_pos, y_pos = robot.world.get_position()
    e_wall = []
    if robot.obstacles.is_path_blocked(x_pos, y_pos, 100, y_pos) is False:
        
        final_dest = True
        e_wall_x = 101
        e_wall_y = y_pos
        return e_wall_x, e_wall_y

    for i in range(x_pos, 101):

        if robot.obstacles.is_position_blocked(i, y_pos) is True:
            e_wall_x = i
            e_wall_y = y_pos
            n_wall = (e_wall_x, e_wall_y)
            
            break
    return e_wall_x, e_wall_y


def find_s_wall():
    final_dest = False
    x_pos, y_pos = robot.world.get_position()
    s_wall = []
    if robot.obstacles.is_path_blocked(x_pos, y_pos, x_pos, -201) is False:
        
        final_dest = True
        s_wall_x = x_pos
        s_wall_y = -201
        return s_wall_x, s_wall_y

    for i in range(y_pos, -201, -1):

        if robot.obstacles.is_position_blocked(x_pos, i) is True:
            s_wall_x = x_pos
            s_wall_y = (i)
            s_wall = (s_wall_x, s_wall_y)
            
            break
    return s_wall_x, s_wall_y


def find_w_wall():
    final_dest = False
    x_pos, y_pos = robot.world.get_position()
    w_wall = []
    if robot.obstacles.is_path_blocked(x_pos, y_pos, -100, y_pos) is False:
        
        final_dest = True
        w_wall_x = -101
        w_wall_y = y_pos
        return w_wall_x, w_wall_y

    for i in range(x_pos, -101, -1):

        if robot.obstacles.is_position_blocked(i, y_pos) is True:
            w_wall_x = i
            w_wall_y = y_pos
            w_wall = (w_wall_x, w_wall_y)
            
            break
    return w_wall_x, w_wall_y


def path_finder_n(robot_name):
    global final_dest
    x_pos, y_pos = robot.world.get_position()
    edge_found = False
    while edge_found is False:
        n_wall_x, n_wall_y = find_n_wall()
       
        move_to_wall_n(n_wall_x, n_wall_y, robot_name)
       
        x_pos, y_pos = robot.world.get_position()
        if y_pos == 200:
            
            edge_found = True
            break

        door_x = find_door_n(n_wall_y)
      
        move_to_door_n(door_x, robot_name)
      
        x_pos, y_pos = robot.world.get_position()

    return "Zen"


def path_finder_e(robot_name):
    global final_dest
    x_pos, y_pos = robot.world.get_position()
    flag, output = robot.do_right_turn(robot_name)
    print(output)
    edge_found = False
    while edge_found is False:
        e_wall_x, e_wall_y = find_e_wall()
       
        move_to_wall_e(e_wall_x, e_wall_y, robot_name)
       
        x_pos, y_pos = robot.world.get_position()
        if x_pos == 100:
            
            edge_found = True
            break
        print(f"e-wally{e_wall_x}")
        door_y = find_door_e(e_wall_x)
        print(f"{door_y}door-x")
      
        move_to_door_e(door_y, robot_name)
      
        x_pos, y_pos = robot.world.get_position()

    
    return "Zen"


def path_finder_s(robot_name):
    global final_dest
    x_pos, y_pos = robot.world.get_position()
    edge_found = False
    flag, output = robot.do_right_turn(robot_name)
    print(output)
    flag, output = robot.do_right_turn(robot_name)
    print(output)
    while edge_found is False:
        s_wall_x, s_wall_y = find_s_wall()
        
        move_to_wall_s(s_wall_x, s_wall_y, robot_name)
       
        x_pos, y_pos = robot.world.get_position()
        if y_pos == -200:
            
            edge_found = True
            break
        
        door_x = find_door_s(s_wall_y)

        move_to_door_s(door_x, robot_name)
      
        x_pos, y_pos = robot.world.get_position()

    return "Zen"


def path_finder_w(robot_name):
    global final_dest
    x_pos, y_pos = robot.world.get_position()
    edge_found = False
    flag, output = robot.do_left_turn(robot_name)
    print(output)
    while edge_found is False:
        w_wall_x, w_wall_y = find_w_wall()
       
        move_to_wall_w(w_wall_x, w_wall_y, robot_name)

        x_pos, y_pos = robot.world.get_position()
        if x_pos == -100:
            
            edge_found = True
            break

        door_y = find_door_w(w_wall_x)

        move_to_door_w(door_y, robot_name)

        x_pos, y_pos = robot.world.get_position()

    return "Zen"
