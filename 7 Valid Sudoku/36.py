import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]])-> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set) # key = (r/3,c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]):
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
    
# Test Cases
def test_valid_sudoku():
    solution = Solution()

    # Test Case 1: Valid Sudoku
    board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    #It uses assert statements to check if the actual result matches the expected result.
    #If an assert statement fails, an AssertionError is raised, indicating a test failure.
    assert solution.isValidSudoku(board1) == True 
    print("Test Case 1: Valid")

    # Test case 2: Invalid Sudoku (duplicate in row)
    board2 = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solution.isValidSudoku(board2) == False
    print("Test Case 2: Invalid")

    # Test Case 3: Invalid Sudoku (duplicate in column)
    board3 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", "3", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solution.isValidSudoku(board3) == False
    print("Test Case 3: Invalid")

    # Test Case 4: Invalid Sudoku (duplicate in square)
    board4 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        ["5", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert solution.isValidSudoku(board4) == False
    print("Test Case 4: Invalid")

#run the test cases
test_valid_sudoku()

#Time Complexity: O(n^2), where n is the size of the Sudoku board (9 in this case). This is because the code iterates through each cell of the board exactly once using nested loops. So it is O(81) which is considered O(1) or constant. However if we generalize the problem to n*n board, it becomes O(n^2).

#Space Complexity: O(n^2) in the worst case, where n is 9. In the worst-case scenario, all cells contain unique digits, and each of the cols, rows, and squares dictionaries will store up to 9 sets, each containing up to 9 elements. Therefore, the space complexity is O(9 * 9 * 3) which is O(1). If we generalize it, it becomes O(n^2).