class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right - left + 1) // 2
            if left + nums[middle] < target:
                left = middle + 1
            elif right - nums[middle] > target:
                right = middle - 1
            elif nums[middle] == target:
                return middle

        


        