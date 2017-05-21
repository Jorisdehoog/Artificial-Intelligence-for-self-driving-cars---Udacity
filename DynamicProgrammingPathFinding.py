# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid, goal, cost):
    # ----------------------------------------
    # insert code below
    # use the movement functions
    # ----------------------------------------
    # set the obtacles to 99
    # [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]

    init = [len(grid)-1, len(grid[0])-1]

    x = init[0]
    y = init[1]
    v = 0

    open = [[v, x, y]]
    count = 0

    complete = False
    while complete is False:

        open.sort()
        open.reverse()
        next = open.pop()
        x = next[1]
        y = next[2]
        v = next[0]

        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]):
                if value[x2][y2] == 99 and grid[x2][y2] != 1:
                    v2 = v + cost
                    value[x2][y2] = v2
                    open.append([v2, x2, y2])

        if len(open) == 0:
            value[init[0]][init[1]] = 0
            complete = True




    # make sure your function returns a grid of values as
    # demonstrated in the previous video.
    return value

pp = compute_value(grid, goal, cost)
for row in pp:
    print row