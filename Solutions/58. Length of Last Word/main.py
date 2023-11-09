class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        array = s.split(" ")
        for _ in range(array.count("")): array.remove("")
        return len(array[-1])