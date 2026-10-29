class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product = 1
        right_product = 1
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = left_product
            left_product *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= right_product
            right_product *= nums[j]
        return output

