def isSafe(row,col,num,board):
    #check in row
    for i in range (9):
        if board[row][i]==num:
            return False
        
    #check in col
    for i in range (9):
        if board[i][col]==num:
            return False
        
    #check in boxes
    startRow = row - row%3
    startCol = col - col%3
    
    for i in range (3):
        for j in range (3):
            if board[startRow+i][startCol+j]==num:
                return False
            
    return True
        

def helper(row,col,board):
    if row == 9-1 and col == 9:
        return True
    
    if col == 9:
        col=0
        row+=1
        
    if board[row][col]>0:
        return helper(row,col+1,board)
    
    for num in range (1,10):
        if isSafe(row,col,num,board):
            board[row][col]=num
            
            if helper(row,col+1,board):
                return True
            
        board[row][col]=0
        
    return False


def solveSudoku(board):
    ans = helper(0,0,board)
    return ans

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')