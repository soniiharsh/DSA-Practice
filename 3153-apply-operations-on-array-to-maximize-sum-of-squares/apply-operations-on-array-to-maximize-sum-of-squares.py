class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_count = [0] * 32

        # Count set bits
        for num in nums:
            for bit in range(32):
                if num & (1 << bit):
                    bit_count[bit] += 1

        ans = 0

        # Greedily construct k maximum numbers
        for _ in range(k):
            x = 0

            for bit in range(32):
                if bit_count[bit] > 0:
                    x |= (1 << bit)
                    bit_count[bit] -= 1

            ans = (ans + x * x) % MOD

        return ans