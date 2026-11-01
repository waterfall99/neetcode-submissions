class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_no = len(matrix)
        cols_no = len(matrix[0])
        left = 0
        right = rows_no * cols_no - 1
        while left <= right:
            middle = (left + right) // 2
            row = middle // cols_no
            col = middle % cols_no
            if matrix[row][col] < target:
                left = middle + 1
            if matrix[row][col]> target:
                right = middle - 1
            if matrix[row][col] == target:
                return True
        return False
