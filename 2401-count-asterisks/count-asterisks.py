class Solution:
    def countAsterisks(self, s: str) -> int:
        stack = []
        count = 0
        for char in s:
            if char=="|":
                if stack and stack[-1]=="|":
                    stack.pop()
                else:
                    stack.append(char)
            if char=="*" and not stack:
                count+=1
        return count