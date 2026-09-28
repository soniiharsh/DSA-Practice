class Solution(object):

    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = []

        for w, h in envelopes:
            left = 0
            right = len(dp)

            while left < right:
                mid = (left + right) // 2

                if dp[mid] < h:
                    left = mid + 1
                else:
                    right = mid

            if left == len(dp):
                dp.append(h)
            else:
                dp[left] = h

        return len(dp)