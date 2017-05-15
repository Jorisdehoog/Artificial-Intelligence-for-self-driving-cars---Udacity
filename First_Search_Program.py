# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1



delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    path = 1        # remove once finished
    # create a list of the current position. First element is the g-number, the next two are the coordinates
    g_val = 1  # number of steps needed (current_pos[0])
    initial_list = [[g_val, init[0], init[1]]]   # initialize the G-value
    # initial_list.append([9, 0, 1])
    goal_reached = 0  # identifier of success

    # print initial_list

    position = init     # position (current_pos[1:2])

    # print grid[position[0]][position[1]]
    # print [1, initial_list[g_val][1], initial_list[g_val][2]]

    # test of grid
    # print [tuple(x[0] for x in grid)]

    print "Initial open list"
    for s in initial_list:
        print s
    print "--------"

    while goal_reached != 1 and g_val < len(grid)*len(grid[0]):
        # store list of g-values in pp
        pp = []
        for i in range(len(initial_list)):
            pp.append(initial_list[i][0])

        # find index of smallest pp
        ppidx = pp.index(min(pp))
        # print ppidx
        # take the list item

        # retreive element with lowest g-value (and check if goal is reached!)
        # also change check-mark on grid
        # remove this from the initial_list
        list_item = initial_list[ppidx]

        print "Take list item"
        print list_item
        print "--------"

        initial_list.pop(ppidx)
        print "New open list"
        for s in initial_list:
            print s
        print "--------"

        if [list_item[1], list_item[2]] == goal:
            path = list_item
            goal_reached = 1

        grid[list_item[1]][list_item[2]] = 1
        # print list_item

        # expand the list item into new open list
        new_list = list()

        # if g_val == 6:
        #     # print len([pp for pp in grid[0]])

        for ii in range(len(delta)):
            newstep = [a + b for a, b in zip([list_item[1], list_item[2]], delta[ii])]
            # print newstep
            # print sum(n < 0 for n in newstep)
            # grid[5][0] is out of bounds, check!
            if newstep[0] < len(grid) and newstep[1] < len(grid[0]) and sum(n < 0 for n in newstep) == 0 and grid[newstep[0]][newstep[1]] != 1 :
                new_list.append([g_val, newstep[0], newstep[1]])
                # mark grid!
                grid[newstep[0]][newstep[1]] = 1
            else:
                newstep = None

        if len(new_list) != 0:
            g_val += 1

        for iii in range(len(new_list)):
            initial_list.append(new_list[iii])

        # print initial_list

    # grid2 = list(grid)
    # grid2.pop(0)
    #
    # print grid2

    # while goal_reached == 0:
    #     # look for other positions.
    #     grid[current_pos[g_val][1]][current_pos[g_val][2]] = 1
    #     last_length = len(current_pos)      # so we dont change the length of the inner loop during operation
    #
    #     # if [current_pos[steps][1], current_pos[steps][2]] == goal:
    #     #     goal_reached = 1
    #     # else:
    #     #     current_pos.pop(steps)
    #
    #     # len(input) = amount of rows
    #     # len(input[0]) = amount of columns
    #
    #     for i in range(len(delta)):
    #         for ii in range(last_length):
    #             newstep = [a + b for a, b in zip([current_pos[ii][1], current_pos[ii][2]], delta[i])]
    #             print newstep
    #             if sum(n < 0 for n in newstep) > 0 or grid[newstep[0]][newstep[1]] == 1:
    #                 # do nothing
    #                 print ""
    #             else:
    #                 # only expand when step is possible (thats the case atm)
    #                 current_pos.append([g_val, newstep[0], newstep[1]])
    #                 grid[newstep[0]][newstep[1]] = 1
    #     g_val += 1




            # print grid



    # check neighbors (expand the one with the smallest g-value)
    # some don't need to be considered anymore as these are already checked... (create a new grid, same size as the maze
    # to keep track of the checked positions! --> NO, just put ones where there were zeros!)

    # remove the nodes that have no un-checked neighbors

    # recurse the loop


    # print current_pos


    return path

p = search(grid, init, goal, cost)
print p