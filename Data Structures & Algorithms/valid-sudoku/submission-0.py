class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row_map = defaultdict(set)
        col_map = defaultdict(set)
        square_map = defaultdict(set) # key row // 3, col // 3

        for i in range(9):
            for j in range(9):
                if not board[i][j].isdigit():
                    continue
                if (board[i][j] in row_map[i] or
                    board[i][j] in col_map[j] or
                    board[i][j] in square_map[i // 3, j // 3]):
                    return False
                
                row_map[i].add(board[i][j])
                col_map[j].add(board[i][j])
                square_map[i // 3, j // 3].add(board[i][j])
        return True
