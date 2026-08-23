class Solution(object):
    def sumGame(self, num):
        n = len(num) // 2

        leftSum = 0
        rightSum = 0
        leftQ = 0
        rightQ = 0

        for i in range(len(num)):
            if i < n:
                if num[i] == '?':
                    leftQ += 1
                else:
                    leftSum += int(num[i])
            else:
                if num[i] == '?':
                    rightQ += 1
                else:
                    rightSum += int(num[i])

        # Odd number of question marks → Alice wins
        if (leftQ + rightQ) % 2 != 0:
            return True

        # Can Bob balance both sides?
        difference = leftSum - rightSum
        questionDifference = rightQ - leftQ

        return difference != questionDifference * 9 // 2