class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = len(nums) // 2
            if nums[middle] < target:
                left = middle + 1
                continue
            elif nums[middle] > target:
                right = middle - 1
                continue
            elif nums[middle] == target:
                return middle

        


        