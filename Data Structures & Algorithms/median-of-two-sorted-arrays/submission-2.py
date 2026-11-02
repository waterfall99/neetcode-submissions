class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        low = 0
        high = len(nums1)
        total_left_size = (len(nums1) + len(nums2) + 1) // 2
        while low <= high:
            mid = (low + high) // 2
            mid2 = total_left_size - mid
            
            LeftA = nums1[mid - 1] if mid > 0 else float('-inf')
            LeftB = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            RightA = nums1[mid] if mid < len(nums1) else float('inf')
            RightB = nums2[mid2] if mid2 < len(nums2) else float('inf')
            
            if LeftA <= RightB and LeftB <= RightA:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(LeftA, LeftB) + min(RightA, RightB)) / 2
                else:
                    return max(LeftA, LeftB)
            elif LeftA > RightB:
                high = mid - 1
            else:
                low = mid + 1
