class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        opening,closing = 0,0
        s =[]
        ans =[]
        def backtrack(opening,closing):
            if opening == closing == n:
                ans.append("".join(s.copy()))
                return 
            if closing <= opening:
                if opening < n:
                    s.append("(")
                    opening +=1
                    backtrack(opening,closing)
                    opening-=1
                    s.pop()
                s.append(")")
                closing +=1
                backtrack(opening,closing)
                closing-=1
                s.pop()
        backtrack(opening,closing)
        return ans