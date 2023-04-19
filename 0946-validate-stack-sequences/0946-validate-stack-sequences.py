class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        j=0
        for i in pushed:
            stack.append(i)
            while  len(stack) >0 and stack[len(stack)-1] == popped[j] :
                stack.pop()
                j+=1
        return True if len(stack) ==0 else False