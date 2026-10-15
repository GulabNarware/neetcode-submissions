class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path=set()
        def back(r,c,i):
            if i==len(word):
                return True

            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or word[i]!=board[r][c] or (r,c) in path:
                return False

            path.add((r,c))

            res =(back(r+1,c,i+1) or back(r-1,c,i+1) or back(r,c+1,i+1) or back(r,c-1,i+1))
            path.remove((r,c))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                res=back(r,c,0)
                if res:
                    return True
        return False



        
            