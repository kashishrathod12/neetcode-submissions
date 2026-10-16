class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = ans = maxf = 0
        for right, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            maxf = max(maxf, count[c])
            if right - left + 1 - maxf > k:
                count[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans