class Solution(object):
    def search(self, nums, target):
        
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=nums[left]:
                #left is sorted 
                if target<nums[mid] and target>=nums[left]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                #right is sorted
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            if nums[mid]==target:
                return mid


    

           
        return -1
        