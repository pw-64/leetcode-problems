class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        for char in [*s]:
            if char == "(": brackets.append("(")
            if char == "[": brackets.append("[")
            if char == "{": brackets.append("{")
            if char == ")":
                if brackets[-1:] == ["("]: brackets.pop(-1)
                else: return False
            if char == "]":
                if brackets[-1:] == ["["]: brackets.pop(-1)
                else: return False
            if char == "}":
                if brackets[-1:] == ["{"]: brackets.pop(-1)
                else: return False
        return len(brackets) == 0