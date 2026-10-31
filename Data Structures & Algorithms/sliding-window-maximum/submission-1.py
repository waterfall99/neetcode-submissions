from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        start = 0
        end = k - 1
        res = []
        q = deque()

        for i in range(k - 1):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        
        while end < len(nums):
            if q and q[0] < start:
                q.popleft()
            while q and nums[q[-1]] < nums[end]:
                q.pop()
            q.append(end)   
            res.append(nums[q[0]])
            start += 1
            end += 1
        return res