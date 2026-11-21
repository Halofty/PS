class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix_min[i] = nums[i:]의 최솟값
        suffix_min = [0] * n
        suffix_min[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        prefix_max = nums[0]
        for i, num in enumerate(nums):
            prefix_max = max(prefix_max, num)
            if prefix_max - suffix_min[i] <= k:
                return i

        return -1
