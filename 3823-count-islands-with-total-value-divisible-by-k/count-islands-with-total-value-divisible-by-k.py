class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        total = 0

        def dfs(r, c):
            nonlocal total

            if r < 0 or c < 0:
                return
            if r >= rows or c >= cols:
                return

            # Add cell value and mark it visited to avoid revisiting.
            if grid[r][c] != 0:
                total += grid[r][c]
                grid[r][c] = 0
            else:
                return

            # Explore all four adjacent cells.
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Explore each island and count it if its sum is divisible by k.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    total = 0
                    dfs(r, c)
                    if total % k == 0:
                        count += 1
                    total = 0

        return count