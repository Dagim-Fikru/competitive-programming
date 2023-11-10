class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for i in operations:
            if i.startswith('-') or i.isdigit() :
                # i=i[1:]
                # if i.isdigit()==True:
                stack.append(int(i))
                print(stack)
            elif i=='+':
                if len(stack)>=2:
                    stack.append(stack[len(stack)-1]+stack[len(stack)-2])
            elif i=='D':
                if stack:
                    stack.append(2*stack[len(stack)-1])
            elif i=='C':
                if stack:
                    stack.pop()
                # print(stack)
        print(stack)
        return sum(stack)