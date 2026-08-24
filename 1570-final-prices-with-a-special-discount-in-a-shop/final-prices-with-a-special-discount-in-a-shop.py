class Solution(object):
    def finalPrices(self, prices):
        n=len(prices)
        stack=[]
        answer = prices[:]
        for i in range(n):
            while stack and prices[i]<=prices[stack[-1]]:
                previous=stack.pop()
                answer[previous]=abs(prices[i]-prices[previous]) 
            stack.append(i) 
        return answer
        



        
        