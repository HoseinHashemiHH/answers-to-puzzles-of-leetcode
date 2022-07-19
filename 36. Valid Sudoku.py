

import enum

def repeat(cell,array)->bool:
    t=0
    for x,ar in enumerate(array):
        if ar==cell:
            t+=1
    return t>1

def repeat_board(cell,board)->bool:
    t=0
    for b in board:
        for bb in b:
            if bb==cell:
                t+=1
    return t>1
    
def sudoko_valid(board:list)->bool:
    m=len(board)
    n=len(board[0])
    p0,p1,p2,p3=0,0,0,0
    while p0<n and p2<m:
       if p0==0 and p2==0:
         for p1 in range(9):
           for p3 in range(9):
               rcell=board[p3][p1]
               if rcell=='.':
                break

               if repeat(rcell,board[p3][:]) or repeat(rcell,board[:][p1]):
                   return False
        
       for i in range(p0,3+p0):
           for j in range(p2,3+p2):
            rcell=board[j][i]
            if rcell=='.':
                break
            if repeat_board(rcell,[item[p2:3+p2] for item in board[p0:3+p0]]):
                return False
       p0+=3
       p2+=3

    return True

def cmd_line():
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    booli=sudoko_valid(board)
    print(booli)

cmd_line()


    
    

            







            