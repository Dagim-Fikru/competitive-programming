# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head = head.next
        arr.pop(-n)
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