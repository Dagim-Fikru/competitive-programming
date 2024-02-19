class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        moves = 0

        for i in s:
            if i=="(":
                stack.append(i)
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    moves+=1
        if stack:
            moves+=len(stack)
        return moves
        