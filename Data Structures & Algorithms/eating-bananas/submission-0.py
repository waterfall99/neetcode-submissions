class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        while start <= end:
            total_hours = 0
            middle = (start + end) // 2
            for number in piles:
                total_hours += (number + middle - 1) // middle
            if total_hours <= h:
                end = middle - 1
            elif total_hours > h:
                start = middle + 1
        return start
