board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
score = []
cnt = 0
import numpy as np
board = list(np.array(board).T)

for i in moves:
    for j in list(range(len(board))):
        if board[i-1][j] !=0:
            score.append(board[i-1][j])
            board[i-1][j]=0
            break
        if len(score)>=2:
            if score[-1]==score[-2] :
                score= score[:-2]
                cnt += 2


print(cnt, score)
print(np.array(board).T)
