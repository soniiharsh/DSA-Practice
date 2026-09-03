class Solution(object):
    def uniformArray(self, nums1):
        """
        :type nums1: List[int]
        :rtype: bool
        """
        # Find the minimum element in the array
        min_val = min(nums1)
        
        # If the minimum element is odd, we can always convert all even numbers to odd.
        if min_val % 2 != 0:
            return True
            
        # If the minimum element is even, it's impossible to convert it to an odd number.
        # So we can only succeed if all the elements in the array are ALREADY even.
        for x in nums1:
            if x % 2 != 0:
                return False
                
        return True