def displayPathtoPrincess(n,grid):
    position = [] # [x,y]
    for i in range(n):
        string = grid[i]
        for j in range(len(string)):
            if string[j] == 'p':
                position.append(j)
                position.append(i)
                break
    middle = int(n/2)
    deltaY = position[1]-middle
    deltaX = position[0]-middle
    if deltaX > 0:
        horizontal = 'RIGHT\n'
    else:
        horizontal = 'LEFT\n'
    if deltaY > 0:
        vertical = 'DOWN\n'
    else:
        vertical = 'UP\n'
    moves = ''
    for i in range(abs(deltaX)):
        moves += vertical+horizontal 
    
    print(moves)
    #print all the moves here

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)