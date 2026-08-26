class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        left = 0
        ones = 0
        ans = ""

        for right in range(len(s)):

            # expand window
            if s[right] == '1':
                ones += 1

            # if more than k ones, shrink
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # exactly k ones
            if ones == k:

                # remove useless leading zeros
                while s[left] == '0':
                    left += 1

                curr = s[left:right + 1]

                if ans == "" or len(curr) < len(ans):
                    ans = curr

                elif len(curr) == len(ans) and curr < ans:
                    ans = curr

        return ans