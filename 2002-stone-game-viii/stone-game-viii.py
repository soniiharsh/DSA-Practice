class Solution(object):
    def stoneGameVIII(self, stones):
        
        prefix = [0] * len(stones)
        prefix[0] = stones[0]

        for i in range(1, len(stones)):
            prefix[i] = prefix[i - 1] + stones[i]

        dp = prefix[-1]

        for i in range(len(stones) - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)

        return dp