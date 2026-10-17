class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif not stack or stack.pop() != {')':'(', '}':'{', ']':'['}[c]:
                return False
        return not stack