# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        while head:
            arr1.append(head.val)
            head = head.next
        arr=[]
        for i in arr1:
            if arr1.count(i)==1:
                arr.append(i)  
        head2 = None
        tail = None
        for value in arr:
            node = ListNode(value)
            if tail is None:
                head2 = node
                tail = node
            else:
                tail.next = node
                tail = node
        return head2