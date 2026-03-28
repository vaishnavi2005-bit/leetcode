class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def is_valid(self, board, row, col, num):
        # Check row and column
        for x in range(9):
            if board[row][x] == num:
                return False
            if board[x][col] == num:
                return False
        
        # Check 3x3 box
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                # Platforms usually use "." for empty cells
                if board[row][col] == 0 or board[row][col] == ".":
                    for num in range(1, 10):
                        # Convert num to string if the board uses strings
                        val = str(num) if isinstance(board[row][col], str) else num
                        if self.is_valid(board, row, col, val):
                            board[row][col] = val
                            if self.solve(board):
                                return True
                            # Backtrack
                            board[row][col] = "." if isinstance(val, str) else 0
                    return False
        return True
