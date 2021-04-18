class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0
        
        mod = 67108863
        mod26 = mod * 26
        assciA = 97
        target = 0
        num = 1
        length = len(needle)
        for n in needle:
            target = (target + ord(n) - assciA) * 26 % mod
            num = (num * 26) % mod
        now = 0
        for n in haystack[:length-1]:
            now = (now + ord(n) - assciA) * 26 % mod

        for i in range(len(haystack) - length+1):
            now = (now + ord(haystack[i+length-1]) - assciA) * 26 % mod
            if now == target:
                return i
            now = (now+mod26 - (ord(haystack[i]) - assciA)*num) % mod
        return -1