class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        for i in s:
            if i=="(":
                stack.append(score)
                score = 0
            else:
                topEl = stack.pop()
                score = topEl + max(2*score,1)
        return score
                    
        