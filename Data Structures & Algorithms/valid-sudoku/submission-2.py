class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_rows():
            for r in range(9):
                seen = set()
                for c in range(9):
                    digit = board[r][c]
                    if digit == ".":
                        continue
                    if digit in seen:
                        return False
                    else:
                        seen.add(digit)
            return True
        
        def check_cols():
            for c in range(9):
                seen = set()
                for r in range(9):
                    digit = board[r][c]
                    if digit == ".":
                        continue
                    if digit in seen:
                        return False
                    else:
                        seen.add(digit)
            return True
        
        def check_boxes():
            for box_r in range(0, 9, 3):
                for box_c in range(0, 9, 3):
                    seen = set()
                    for r in range(3):
                        for c in range(3):
                            digit = board[box_r + r][box_c + c]
                            if digit == ".":
                                continue
                            if digit in seen:
                                return False
                            else: 
                                seen.add(digit)
            return True

        return check_rows() and check_cols() and check_boxes()
                    

