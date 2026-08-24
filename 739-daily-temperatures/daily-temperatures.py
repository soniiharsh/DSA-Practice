class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        stack=[]
        answer=[0]*n
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                previous=stack.pop()
                answer[previous]=i-previous
            stack.append(i)
        return answer


        