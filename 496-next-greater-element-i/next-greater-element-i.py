class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        n=len(nums1)
        m=len(nums2)
        ans=[-1]*n
        stack=[]
        greater={}
        for i in range(m):
            while stack and nums2[i]>nums2[stack[-1]]:
                prev=stack.pop()
                greater[nums2[prev]]=nums2[i]
            stack.append(i)
        print(greater)
        for i in range(n):
            if nums1[i] in greater:
                ans[i]=greater[nums1[i]]

        return ans
     

        