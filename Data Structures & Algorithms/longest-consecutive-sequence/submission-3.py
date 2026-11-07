class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        s = set(nums)
        for num in s:
            if num-1 not in s:
                count = 1
                curr = num
                while curr+1 in s:
                    curr+=1
                    count+=1
            max_count= max(max_count,count)
        return max_count