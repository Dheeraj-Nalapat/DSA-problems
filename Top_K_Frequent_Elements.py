class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        result = []
        for i in range(k):
            temp = max(d.values())
            for j in d.keys():
                if d[j] == temp:
                    result.append(j)
                    d[j]=0
                    break
        return result     
