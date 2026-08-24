class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        ans=[-1]*n
        greater={}
        nums2 = nums * 2
        stack=[]
        for i in range(len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                p=stack.pop()
                if p < n:
                    ans[p]=nums2[i]
            stack.append(i)
        return ans
                
           
        