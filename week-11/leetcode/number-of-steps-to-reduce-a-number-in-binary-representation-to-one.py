class Solution:
    def numSteps(self, s: str) -> int:
        convert = []
        i=len(s)-1
        for r in range(len(s)):
            convert.append(2**i)
            i-=1
        number = 0
        for i in range(len(convert)):
            number+= convert[i]*int(s[i])
        steps = 0
        while number>1:
            if number%2:
                number+=1
                steps+=1
            else:
                number//=2
                steps+=1
        return steps

