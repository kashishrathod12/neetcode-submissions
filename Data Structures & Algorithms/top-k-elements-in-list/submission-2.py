class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for i in nums:
            if i in s:
                s[i] += 1
            else: s[i] = 1
        result = sorted(s.items(), key=lambda item: item[1], reverse=True)
        return [num for num, freq in result[:k]]