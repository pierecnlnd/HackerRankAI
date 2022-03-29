def nextMove(n,r,c,grid):
    position = [] # [x,y]
    for i in range(n):
        string = grid[i]
        for j in range(len(string)):
            if string[j] == 'p':
                position.append(j)
                position.append(i)
                break
    # r : Y, c : X
    deltaY = position[1]-r
    deltaX = position[0]-c
    if deltaX > 0:
        horizontal = 'RIGHT\n'
    else:
        horizontal = 'LEFT\n'
    if deltaY > 0:
        vertical = 'DOWN\n'
    else:
        vertical = 'UP\n'
    if abs(deltaX) > abs(deltaY):
        return horizontal
    else:
        return vertical

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))