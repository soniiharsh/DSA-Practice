from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        start = sum(x < target for x in nums)
        count = nums.count(target)
        return list(range(start, start + count))