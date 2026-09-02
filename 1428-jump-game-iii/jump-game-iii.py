class Solution(object):
    def canReach(self, arr, start):
        visited = set()
        stack = [start]

        while stack:
            i = stack.pop()

            if i in visited:
                continue

            if arr[i] == 0:
                return True

            visited.add(i)

            left = i - arr[i]
            right = i + arr[i]

            if left >= 0:
                stack.append(left)

            if right < len(arr):
                stack.append(right)

        return False