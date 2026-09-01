class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums_new = nums1 + nums2
        length = len(nums_new)
        nums_new.sort()
        half = length//2
        if length&1:
            return nums_new[half]
        else:
            return (nums_new[half] + nums_new[half-1])/2