class Solution:
    def interpret(self, command: str) -> str:
        arr=[]
        for i in command:
            if i=='G' or i=="(":
                arr.append(i)
            elif i==')':
                if arr[-1]=='(':
                    arr.pop()
                    arr.append('o')
                elif arr[-1]=='l':
                    for i in range(3):
                        arr.pop()
                    arr.append('al')
            else:
                arr.append(i)
        return "".join(arr)
            
        