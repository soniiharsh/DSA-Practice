class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=set()
        maxi=0
        for j in range(len(s)):
            while s[j] in seen:
                seen.remove(s[left])
                left=left+1
            seen.add(s[j])
            maxi=max(maxi,(j-left+1))
        return maxi
        


        
        