class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGas,remainingGas = 0,0
        Start = 0

        for i in range(len(gas)):
            totalGas += gas[i]-cost[i]
            remainingGas += gas[i]-cost[i]

            if remainingGas<0:
                remainingGas = 0
                Start = i+1
        if totalGas>=0:
            return Start
        else:
            return -1      
