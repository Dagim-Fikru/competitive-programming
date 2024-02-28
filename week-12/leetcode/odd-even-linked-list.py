# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = []
        even = []
        current = head
        count = 0
        while current:
            count+=1
            if count%2:
                odd.append(current.val)
            else:
                even.append(current.val)
            current = current.next
        head2 = None
        tail = None
        for value in odd:
            node = ListNode(value)
            if tail is None:
                head2 = node
                tail = node
            else:
                tail.next = node
                tail = node
        for value in even:
            node = ListNode(value)
            if tail is None:
                head2 = node
                tail = node
            else:
                tail.next = node
                tail = node
        return head2