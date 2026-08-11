class Solution:
    def isValidSudoku(self, board) -> bool:
        nums = set()
        valid = set(['1','2','3','4','5','6','7','8','9'])
        for row in board:
            nums = set()
            for item in row:
                if item in valid:
                    if item in nums:
                        return False
                    else:
                        nums.add(item)

        for i in range(9):
            nums = set()
            for row in board:
                if row[i] in valid:
                    if row[i] in nums:
                        return False
                    else:
                        nums.add(row[i])
        
        s = -3
        e = 0
        total = 0
        nums = set()
        for i in range(3):
            s += 3
            e += 3
            for j in range(9):
                row = board[j]
                for k in range(s, e):
                    if total == 9:
                        total = 0
                        nums = set()

                    if row[k] in valid:
                        if row[k] in nums:
                            return False
                        else:
                            nums.add(row[k])
                    total += 1

        
        return True

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        """Initialize a Solution instance before each test."""
        self.solution = Solution()
        
        # Valid Sudoku board
        self.valid_board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        
        # Invalid Sudoku board (duplicate in first row)
        self.invalid_row_board = [
            ["5","3","3",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        
        # Invalid Sudoku board (duplicate in first column)
        self.invalid_col_board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            ["5","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        
        # Invalid Sudoku board (duplicate in first 3x3 box)
        self.invalid_box_board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","5",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
    
    def test_valid_board(self):
        """Test a valid Sudoku board."""
        result = self.solution.isValidSudoku(self.valid_board)
        self.assertTrue(result, "Should return True for a valid Sudoku board")
    
    def test_invalid_row(self):
        """Test a Sudoku board with duplicate numbers in a row."""
        result = self.solution.isValidSudoku(self.invalid_row_board)
        self.assertFalse(result, "Should return False when there are duplicate numbers in a row")
    
    def test_invalid_column(self):
        """Test a Sudoku board with duplicate numbers in a column."""
        result = self.solution.isValidSudoku(self.invalid_col_board)
        self.assertFalse(result, "Should return False when there are duplicate numbers in a column")
    
    def test_invalid_box(self):
        """Test a Sudoku board with duplicate numbers in a 3x3 box."""
        result = self.solution.isValidSudoku(self.invalid_box_board)
        self.assertFalse(result, "Should return False when there are duplicate numbers in a 3x3 box")
    
    def test_empty_board(self):
        """Test a completely empty Sudoku board."""
        empty_board = [["." for _ in range(9)] for _ in range(9)]
        result = self.solution.isValidSudoku(empty_board)
        self.assertTrue(result, "Should return True for an empty board")

if __name__ == "__main__":
    unittest.main()
        


