class Solution:
    def minOperations(self, s: str) -> int:
        first_element_one = 0
        first_element_zero = 0
        for i in range(len(s)):
            if i%2!=0:
                if s[i]!='1':
                    first_element_zero+=1
                else:
                    first_element_one+=1
            else:
                if s[i]!='0':
                    first_element_zero+=1
                else:
                    first_element_one+=1

        return min(first_element_one,first_element_zero)

