class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inverse = {"(":")", "[":"]", "{":"}"}

        for c in s:
            if c in ['{', '[', '(']:
                stack.append(c)
            elif stack and c == inverse[stack[-1]]:
                stack.pop()
            else:
                return False
        if stack:
            return False
        return True