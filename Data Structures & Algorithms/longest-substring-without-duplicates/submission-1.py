class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = ans = 0
        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left += 1
            seen.add(c)
            ans = max(ans, right - left + 1)
        return ans