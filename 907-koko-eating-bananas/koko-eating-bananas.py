class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n=len(piles)
        left=1
        right=max(piles)
        while left<=right:
            mid=(left+right)//2
            hours = sum((pile + mid - 1) // mid for pile in piles)
            if hours<=h:
                right=mid-1
            elif hours>h:
                left=mid+1
        return left
            
                


        