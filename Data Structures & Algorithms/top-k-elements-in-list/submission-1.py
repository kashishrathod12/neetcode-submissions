class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        result = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return [num for num, freq in result[:k]]