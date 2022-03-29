# Head ends here

def next_move(posr, posc, board):
    dic = {}
    distance = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'd':
                x = j
                y = i
                deltaX = x - posc
                deltaY = y - posr
                dist = (deltaX**2+deltaY**2)**(.5)
                distance.append(dist)
                dic[dist] = [x,y,deltaX,deltaY]
    closest = dic[min(distance)] # [x,y,deltaX,deltaY]
    if closest[2] == 0 and closest[3] == 0:
        move = 'CLEAN'
    else:
        if closest[2] > 0:
            horizontal = 'RIGHT'
        elif closest[2] < 0:
            horizontal = 'LEFT'
        if closest[3] > 0:
            vertical = 'DOWN'
        elif closest[3] < 0:
            vertical = 'UP'
        if abs(closest[2]) > abs(closest[3]):
            move = horizontal
        else:
            move = vertical
    print(move)

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)