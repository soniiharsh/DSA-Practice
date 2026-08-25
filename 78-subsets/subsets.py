class Solution(object):
    def solve(self, i, nums, ans, temp):
        if i >= len(nums):
            ans.append(temp[:])
            return

        # take
        temp.append(nums[i])
        self.solve(i + 1, nums, ans, temp)
        temp.pop()

        # not take
        self.solve(i + 1, nums, ans, temp)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        temp = []

        self.solve(0, nums, ans, temp)

        return ans