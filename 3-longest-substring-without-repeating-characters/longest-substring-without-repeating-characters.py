class Solution(object):
    def lengthOfLongestSubstring(self, s):
        p=s
        left=0
        n=len(s)
        freq={}
        max_count=0
        for right in range(0,n):
            if s[right] in freq:
                freq[s[right]] += 1
            else:
                freq[s[right]] = 1
            while freq[s[right]]>1:
                freq[s[left]]-=1
                left+=1
            count=right-left+1
            max_count=max(count,max_count)
        return max_count
            

        