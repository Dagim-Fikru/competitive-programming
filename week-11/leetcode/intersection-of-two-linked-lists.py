# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        memory_to_value = {}
        curr2 = headB
        curr1 = headA
        if curr1.next==None and curr2.next==None:
            if curr1.val==curr2.val:
                return curr1
        while curr1:
            memory_to_value[curr1] = curr1.val
            curr1 = curr1.next
        while curr2:
            if curr2 in memory_to_value:
                return curr2
            curr2 = curr2.next
        return 

