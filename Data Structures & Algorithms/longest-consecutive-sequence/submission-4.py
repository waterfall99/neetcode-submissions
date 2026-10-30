class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 1
        seen = set()
        if len(nums) == 0:
            return 0
        for i in nums:
            seen.add(i)
        for i in nums:
            if (i - 1) not in seen:
                j = i
                current_length = 1
                while (j + 1) in seen:
                    j += 1
                    current_length += 1
                if current_length > max_length:
                    max_length = current_length
        return max_length