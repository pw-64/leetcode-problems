class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [* [int(s) for s in str(eval("".join([str(n) for n in digits])) + 1)]]