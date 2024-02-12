# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"))
        dummy.next = head
        i = dummy
        j = dummy
        for k in range(n+1):
            j = j.next
        while j:
            j = j.next
            i = i.next
        i.next = i.next.next
        head = dummy.next
        return head
        
