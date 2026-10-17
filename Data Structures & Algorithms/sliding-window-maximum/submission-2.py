class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = []
        a = []
        for i in range(len(nums)):
            while q and q[0] <= i-k:
                q.pop(0)
            while q  and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)
            if i>=k-1:
                a.append(nums[q[0]])
        return a