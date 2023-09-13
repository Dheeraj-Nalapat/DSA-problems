class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        result = []
        for i in range(k):
            temp = max(d.values())
            for i in d.keys():
                if d[i] == temp:
                    result.append(i)
                    d[i]=0
                    break
        return result  
