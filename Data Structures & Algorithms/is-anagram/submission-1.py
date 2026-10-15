class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in a:
                a[s[i]]+=1
            else:
                a[s[i]]=1
        for j in range(len(t)):
            if t[j] in b:
                b[t[j]]+=1
            else:
                b[t[j]]=1
        return a == b
            