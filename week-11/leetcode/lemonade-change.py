class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_ten = 0
        count_five = 0

        for i in range(len(bills)):
            if count_ten<0 or count_five<0:
                return False
            if bills[i]==5:
                count_five+=1
            elif bills[i]==10:
                count_ten+=1
                count_five-=1
            else:
                if count_five>=3 and count_ten==0:
                    count_five-=3
                else:
                    count_ten-=1
                    count_five-=1
        return count_five>=0 and count_ten>=0
