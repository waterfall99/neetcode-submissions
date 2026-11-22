class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        prev_number = 2
        prev_prev_number = 1
        for i in range(n-2):
            original_prev = prev_number
            prev_number += prev_prev_number
            prev_prev_number = original_prev
        return prev_number