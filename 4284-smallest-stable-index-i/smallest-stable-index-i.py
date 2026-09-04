class Solution(object):

    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        n = len(nums)

        # Store the minimum value from index i to the end
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Maximum value from nums[0] to nums[i]
        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            # Instability score
            score = prefix_max - suffix_min[i]

            if score <= k:
                return i

        return -1