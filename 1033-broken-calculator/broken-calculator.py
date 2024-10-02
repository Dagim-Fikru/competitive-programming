class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        oper = 0
        while target>startValue:
            if target%2:
                target+=1
            else:
                target//=2
            oper+=1
        return oper + (startValue-target)