class Solution(object):
    def solve(self, i, nums, ans, temp):
        
        ans.append(temp[:])
        
        for j in range(i,len(nums)):
            if j>i and nums[j]==nums[j-1]:
                continue
            temp.append(nums[j])
            self.solve(j+1,nums,ans,temp)
            temp.pop()
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        temp = []

        self.solve(0, nums, ans, temp)

        return ans
