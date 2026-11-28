class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        
        dp = [0] * len(nums)

        for i in range(0, 2):
            dp[i] = nums[i]
        
        dp[2] = nums[0] + nums[2]

        for money in range(3, len(nums)):
            dp[money] = nums[money] + max(dp[money - 2], dp[money - 3])
        
        return max(dp[-1], dp[-2])

