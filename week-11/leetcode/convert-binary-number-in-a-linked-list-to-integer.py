# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        count = 0
        curr = head
        while curr:
            count+=1
            curr = curr.next
        i=0
        while count>0:
            arr.append(2**i)
            i+=1
            count-=1
        arr = arr[::-1]
        total = 0
        index = 0
        curr1 = head
        while curr1:
            total+= curr1.val*arr[index]
            curr1=curr1.next
            index+=1
        return total
        