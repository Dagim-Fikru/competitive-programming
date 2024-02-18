class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split('/')
        # print(temp)
        for i in temp:
            if i != '.' and i != '' and i != '..':
                stack.append(i)
            elif i == '..':
                if stack:
                    stack.pop()
        # stack.append('debebe')
        return "/" + "/" .join(stack)
        