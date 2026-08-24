class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        n=len(prices)
        ans=[1]*n
        for i in range(n):
            discount=0
            for j in range(i+1,n):  
                if prices[j]<=prices[i]:
                    discount=abs(prices[j])
                    break
            ans[i]=prices[i]-discount
            print(ans)

        return ans


        