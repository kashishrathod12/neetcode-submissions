class Solution:
    def isPalindrome(self, s: str) -> bool:
        o = ""
        for c in s:
            if c.isalnum():
                o+=c.lower()
        return o == o[::-1]