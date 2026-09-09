class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        p = 1000

        while p <= n:
            # Every number >= p has a comma at this position
            ans += n - p + 1

            # Move to the next comma position
            p *= 1000

        return ans