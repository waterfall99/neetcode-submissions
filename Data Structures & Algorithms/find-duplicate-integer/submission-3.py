class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow1 = slow
        slow2 = 0

        while slow1 != slow2:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
        
        return slow1
