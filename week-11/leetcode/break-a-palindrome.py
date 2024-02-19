class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        list_of_palindrome = list(palindrome)
        if len(palindrome)==1:
            return ""
        changed = False
        for i in range(len(list_of_palindrome)):
            if list_of_palindrome[i]!='a':
                curr = list_of_palindrome[i]
                list_of_palindrome[i]='a'
                if list_of_palindrome[::-1]==list_of_palindrome:
                    list_of_palindrome[i]=curr
                    continue
                changed = True
                break
        if changed:
            return "".join(list_of_palindrome)
        list_of_palindrome[-1]="b"
        return "".join(list_of_palindrome)