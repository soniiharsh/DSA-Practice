
from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        sum1 = [0] * (4 * n)
        sum2 = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, v):
            length = r - l + 1
            sum2[node] = (
                sum2[node] + 2 * v * sum1[node] + v * v * length
            ) % MOD
            sum1[node] = (sum1[node] + v * length) % MOD
            lazy[node] = (lazy[node] + v) % MOD

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return
            mid = (l + r) // 2
            v = lazy[node]
            apply(node * 2, l, mid, v)
            apply(node * 2 + 1, mid + 1, r, v)
            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)
            mid = (l + r) // 2

            if ql <= mid:
                update(node * 2, l, mid, ql, qr)
            if qr > mid:
                update(node * 2 + 1, mid + 1, r, ql, qr)

            sum1[node] = (sum1[node * 2] + sum1[node * 2 + 1]) % MOD
            sum2[node] = (sum2[node * 2] + sum2[node * 2 + 1]) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i)

            ans = (ans + sum2[1]) % MOD
            last[x] = i

        return ans
