#include <iostream>
#include <vector>
#include <unordered_set>

class Solution {
public:
    bool isValidSudoku(std::vector<std::vector<char>>& board) {
        for (int i = 0; i < 9; ++i) {
            std::unordered_set<char> row_set;
            std::unordered_set<char> col_set;
            std::unordered_set<char> square_set;

            for (int j = 0; j < 9; ++j) {
                // Check rows
                if (board[i][j] != '.') {
                    if (row_set.find(board[i][j]) != row_set.end()) {
                        return false;
                    }
                    row_set.insert(board[i][j]);
                }

                // Check columns
                if (board[j][i] != '.') {
                    if (col_set.find(board[j][i]) != col_set.end()) {
                        return false;
                    }
                    col_set.insert(board[j][i]);
                }

                // Check 3x3 squares
                int row_index = 3 * (i / 3) + j / 3;
                int col_index = 3 * (i % 3) + j % 3;
                if (board[row_index][col_index] != '.') {
                    if (square_set.find(board[row_index][col_index]) != square_set.end()) {
                        return false;
                    }
                    square_set.insert(board[row_index][col_index]);
                }
            }
        }
        return true;
    }
};

int main() {
    Solution sol;
    std::vector<std::vector<char>> board = {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };

    if (sol.isValidSudoku(board)) {
        std::cout << "Valid Sudoku" << std::endl;
    } else {
        std::cout << "Invalid Sudoku" << std::endl;
    }

    return 0;
}
