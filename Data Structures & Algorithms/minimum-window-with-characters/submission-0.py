class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(t)
        left = start = 0
        need = {}
        for c in t:
            need[c]=need.get(c, 0) + 1
        missing = len(t)
        min_len = float('inf')
        for right, c in enumerate(s):
            if need.get(c,0)>0:
                missing -= 1
            need[c] = need.get(c,0)-1
            while missing ==0:
                if right-left+1<min_len:
                    start = left
                    min_len = right-left+1
                need[s[left]] = need.get(s[left],0)+1
                if need[s[left]]>0:
                    missing += 1
                left += 1
        return "" if min_len==float('inf') else s[start:start+min_len]