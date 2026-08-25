class Solution(object):
    def missingMultiple(self, nums, k):
        mapp = set(nums)

        for i in range(k, k * (len(nums) + 2), k):
            if i not in mapp:
                return i