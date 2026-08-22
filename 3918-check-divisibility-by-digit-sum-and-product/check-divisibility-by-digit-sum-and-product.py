class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x=n
        sum=0
        product=1
        while x>0:
            number=x%10
            sum+=number
            product*=number
            print(product,sum)
            x=x//10

        if (n%(sum+product)) == 0:
            return True
        return False

        