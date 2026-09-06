class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m = len(s)
        n = len(t)

        # dp[j] = number of ways to form t[:j] 
        # using characters processed so far from s
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(m):
            # Traverse backwards so that dp[j-1] 
            # still represents the previous row
            for j in range(n, 0, -1):
                if s[i] == t[j - 1]:
                    dp[j] += dp[j - 1]

        return dp[n]