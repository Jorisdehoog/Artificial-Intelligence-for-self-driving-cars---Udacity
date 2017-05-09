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
    current_pos = [0]
    current_pos[1:2] = init

    # initiate loop (while-loop?)
    # check if current position is the final result

    # check neighbors (expand the one with the smallest g-value)
    # some don't need to be considered anymore as these are already checked... (create a new grid, same size as the maze
    # to keep track of the checked positions!)

    # remove the nodes that have no un-checked neighbors

    # recurse the loop


    print current_pos


    return path

p = search(grid, init, goal, cost)