class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cols=collections.defaultdict(set)
        # rows=collections.defaultdict(set)
        # square=collections.defaultdict(set) # key =(r//3,c//3)

        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c]==".":
        #             continue

        #         if (board[r][c] in rows[r]
        #          or board[r][c] in cols[c] 
        #          or board[r][c] in square[(r//3,c//3)]):
        #             return False

        #         rows[r].add(board[r][c])
        #         cols[c].add(board[r][c])
        #         square[(r//3,c//3)].add(board[r][c])
        # return True

#my method :

        for i in range(0,9,3):
            for j in range(0,9,3):
                h={}
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c]!=".": #if board[r][c].numeric()
                            if board[r][c] in h:
                                return False
                            h[board[r][c]]=1

    #it is check in row duplicate value
        
        for r in range(9):
            check_row={}
            for c in range(9):
                if board[r][c]!=".":
                    if board[r][c] in check_row:
                        return False
                    check_row[board[r][c]]=1

    #it is check in col duplicate value
        
        for c in range(9):
            check_col={}
            for r in range(9):
                if board[r][c]!=".":
                    if board[r][c] in check_col:
                        return False
                    check_col[board[r][c]]=1

        return True






