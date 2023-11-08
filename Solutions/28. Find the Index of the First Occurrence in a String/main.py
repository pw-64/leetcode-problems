class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack: return -1
        n_len = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i + n_len] == needle:
                return i