def scan_dirt(dimx,dimy,board):
    dirt_post = [(j,i) for i in range(dimy) for j in range(dimx) if board[i][j] == 'd']
    return dirt_post
def closest(posx,posy,dirt_post):
    dist = [abs(d[0]-posx)+abs(d[1]-posy) for d in dirt_post]
    index_min = min(range(len(dist)), key=dist.__getitem__)
    return dirt_post[index_min]
def decide_move(posx,posy,closest_dirt):
    delta = (closest_dirt[0]-posx,closest_dirt[1]-posy)
    if delta[0] == 0 and delta[1] == 0:
        move = 'CLEAN'
    else:
        if delta[0] > 0:
            horizontal = 'RIGHT'
        elif delta[0] < 0:
            horizontal = 'LEFT'
        if delta[1] > 0:
            vertical = 'DOWN'
        elif delta[1] < 0:
            vertical = 'UP'
        if abs(delta[0]) > abs(delta[1]):
            move = horizontal
        else:
            move = vertical
    return move
def next_move(posx, posy, dimx, dimy, board):
    dirt_post = scan_dirt(dimx,dimy,board) # [(x1,y1),(x2,y2),...]
    closest_dirt = closest(posx,posy,dirt_post)
    move = decide_move(posx,posy,closest_dirt)
    print(move)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)

'''  ----Different Version----
# If merged
def next_move(posx, posy, dimx, dimy, board):
    dirt_post = [(j,i) for i in range(dimy) for j in range(dimx) if board[i][j] == 'd']
    dist = [abs(d[0]-posx)+abs(d[1]-posy) for d in dirt_post]
    index_min = min(range(len(dist)), key=dist.__getitem__)
    closest_dirt = dirt_post[index_min]
    delta = (closest_dirt[0]-posx,closest_dirt[1]-posy)
    if delta[0] == 0 and delta[1] == 0:
        move = 'CLEAN'
    else:
        if delta[0] > 0:
            horizontal = 'RIGHT'
        elif delta[0] < 0:
            horizontal = 'LEFT'
        if delta[1] > 0:
            vertical = 'DOWN'
        elif delta[1] < 0:
            vertical = 'UP'
        if abs(delta[0]) > abs(delta[1]):
            move = horizontal
        else:
            move = vertical
    print(move)

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)

'''