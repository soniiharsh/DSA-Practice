class Solution(object):

    def resultArray(self, nums, k, queries):
        """
        :type nums: List[int]
        :type k: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        n = len(nums)

        # Each node:
        # [product_mod_k, prefix_counts]
        #
        # prefix_counts[r] =
        # number of prefixes whose product % k == r

        size = 4 * n
        prod = [0] * size
        pref = [[0] * k for _ in range(size)]

        def merge(node, left, right):
            # Product of entire combined segment
            prod[node] = (prod[left] * prod[right]) % k

            # Prefixes entirely inside left segment
            for r in range(k):
                pref[node][r] = pref[left][r]

            # Prefixes that extend from left into right
            left_prod = prod[left]

            for r in range(k):
                count = pref[right][r]

                if count:
                    new_r = (left_prod * r) % k
                    pref[node][new_r] += count

        def build(node, l, r):
            if l == r:
                value = nums[l] % k

                prod[node] = value
                pref[node][value] = 1

                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            merge(node, node * 2, node * 2 + 1)

        def update(node, l, r, index, value):
            if l == r:
                value %= k

                prod[node] = value

                # Reset prefix counts
                for i in range(k):
                    pref[node][i] = 0

                pref[node][value] = 1
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            merge(node, node * 2, node * 2 + 1)

        def query(node, l, r, ql, qr):
            # Completely outside
            if qr < l or r < ql:
                return None

            # Completely inside
            if ql <= l and r <= qr:
                return (prod[node], pref[node][:])

            mid = (l + r) // 2

            left_result = query(node * 2, l, mid, ql, qr)
            right_result = query(node * 2 + 1, mid + 1, r, ql, qr)

            if left_result is None:
                return right_result

            if right_result is None:
                return left_result

            left_prod, left_pref = left_result
            right_prod, right_pref = right_result

            combined_prod = (left_prod * right_prod) % k
            combined_pref = left_pref[:]

            for r in range(k):
                if right_pref[r]:
                    new_r = (left_prod * r) % k
                    combined_pref[new_r] += right_pref[r]

            return (combined_prod, combined_pref)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Persistent update
            update(1, 0, n - 1, index, value)

            # We need prefixes of nums[start:n]
            _, prefix_counts = query(1, 0, n - 1, start, n - 1)

            answer.append(prefix_counts[x])

        return answer