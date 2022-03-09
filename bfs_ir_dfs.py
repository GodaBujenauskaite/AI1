from collections import deque as queue
import copy

HEIGHT = -1
WIDTH = -1
dRow = [0, 1, 0, -1]
dCol = [-1, 0, 1, 0]
visited = [[]]
goal = (-1,-1)
wallChar='|'
PathChar=' '
solutionChar='X'

def isValid(row, col, grid):
    global HEIGHT
    global WIDTH
    global visited
    if (row < 0 or col < 0 or row >= HEIGHT or col >= WIDTH):
        return False
    if (visited[row][col] or grid[row][col] == wallChar):
        return False
    return True

def PrintSolution(grid):
    fs = open("output.txt", "a")
    for row in grid:
        str=""
        str=str.join(row)+'\n'
        fs.write(str)
    fs.write('\n')
    fs.close()

def DFS(row, col, grid):
    global dRow
    global dCol
    global visited
    global goal

    if (isValid(row, col, grid) == False):
        return
    grid[row][col]=solutionChar
    if ((row,col) == goal):
        PrintSolution(grid)
    visited[row][col] = True

    for i in range(4):
        DFS(row + dRow[i], col + dCol[i], grid)
    grid[row][col]=PathChar  #jei norim tik galutinio kelio

def BFS(row, col, grid):
    global dRow
    global dCol
    global visited
    global goal
    q = queue()
    q.append(( row, col ))
    visited[row][col] = True
 
    while (len(q) > 0):
        cell = q.popleft()
        x = cell[0]
        y = cell[1]
        grid[x][y]=solutionChar
        if ((x,y) == goal):
            PrintSolution(grid)
            q.clear()
            return

        for i in range(4):
            adjacentY = y + dRow[i]
            adjacentX = x + dCol[i]
            if (isValid(adjacentX, adjacentY, grid)):
                q.append((adjacentX, adjacentY))
                visited[adjacentX][adjacentY] = True

if __name__ == '__main__':
    fs = open("output.txt", "w")
    fs.close()
    grid =  [[]]
    with open('input.txt', 'r') as fd:
        reader = fd.read().splitlines()
        for idy, row in enumerate(reader):
            grid.append([])
            for idx, el in enumerate(row):
                grid[idy].append(el)
        grid.pop()
        fd.close()
    PrintSolution(grid)
    HEIGHT=len(grid)
    WIDTH=len(grid[0])
    goal=(HEIGHT-1,WIDTH-1)
    visited = [[False for i in range(HEIGHT)] for j in range(WIDTH)]
    grid2=copy.deepcopy(grid)
    DFS(0, 0, grid)
    visited = [[False for i in range(HEIGHT)] for j in range(WIDTH)]
    BFS(0, 0, grid2)