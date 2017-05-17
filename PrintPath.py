# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
#
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left,
# up, and down motions. Note that the 'v' should be
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1

    # initialize the path-list:
    expand = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]

    # initialize g_val_grid
    pathing = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    pathing[init[0]][init[1]] = 0

    x = init[0]
    y = init[1]
    g = 0

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]

            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            pathing[x2][y2] = g2

    # for row in pathing:
    #     print row

    # find shortest path by counting back from last g_val to 0 in the matrix pathing
    # we know that the end point is at x and y
    expand[x][y] = '*'
    prev_g = g
    prev_x = x
    prev_y = y
    # print [g, x, y]
    # print len(pathing[0])
    flagstop = False
    while flagstop is False:
        if prev_x == 0 and prev_y == 0:
            flagstop = True
        for i in range(len(pathing)):       # y-direction
            for ii in range(len(pathing[0])):      # x-direction
                pp = pathing[i][ii]
                if pp == prev_g - 1:
                    # find out which direction we moved

                    if (ii - prev_y) == 0 and abs(i - prev_x) == 1:
                        # vertical  movement (either delta[1] or delta[3])
                        # print (2 + (i-prev_x))
                        expand[i][ii] = delta_name[(1 - (i - prev_x))]
                        prev_x = i
                        prev_g -= 1
                    if (i - prev_x) == 0 and abs(ii - prev_y) == 1:
                        # print (2 + (i - prev_y))
                        expand[i][ii] = delta_name[(2 - (ii - prev_y))]
                        prev_y = ii
                        prev_g -= 1

                    # print "test"

    return expand  # make sure you return the shortest path


p = search(grid, init, goal, cost)
for row in p:
    print row