class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_ele = {}
        for i in nums:
            if i in freq_ele:
                freq_ele[i] += 1
            else:
                freq_ele[i] = 1
        pairs = []
        for key, freq in freq_ele.items():
            pairs.append([freq, key])
        pairs.sort(reverse = True)
        result = []
        for i in range(k):
            result.append(pairs[i][1])
        return result