class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        
        if n < 3 or m < 3:            
            return
    
    
        def dfs(row, col):
            board[row][col] = 'R'
            if row > 0 and board[row - 1][col] == 'O':
                dfs(row - 1, col)
            if row < n - 1 and board[row + 1][col] == 'O':
                dfs(row + 1, col)
            if col > 0 and board[row][col - 1] == 'O':
                dfs(row, col - 1)
            if col < m - 1 and board[row][col + 1] == 'O':
                dfs(row, col + 1)
        for row in range(n):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][m - 1] == 'O':
                dfs(row, m - 1)
        for col in range(1, m - 1):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[n - 1][col] == 'O':
                dfs(n - 1, col)
        
      
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'R':
                    board[row][col] = 'O'