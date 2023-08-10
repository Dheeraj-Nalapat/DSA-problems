class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ma = 0
        sa = max(prices)
        dif = 0
        #for index,value in enumerate(prices):
        for i in range(len(prices)):
            if prices[i]<sa:
                sa = prices[i]
            if dif<prices[i]-sa:
                dif=prices[i]-sa
        return dif         
