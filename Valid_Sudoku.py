class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for j in range(9)]
        square = {}
        for i in range(9):
            col = []
            for j in range(9):
                square[(j//3,i//3)] = square.get((j//3,i//3),[])
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] in col or board[j][i] in row[j] or board[j][i] in square[(j//3,i//3)] :
                        return False
                    col.append(board[j][i])    
                    row[j].append(board[j][i])
                    square[(j//3,i//3)].append(board[j][i])        
        return True
