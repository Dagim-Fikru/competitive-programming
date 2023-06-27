# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        while head:
            arr.append(head.val)
            head = head.next
        x = Deque(arr)
        x.rotate(k)
        while arr:
            arr.pop()
        arr.extend(x)
        # list_to_linked_list(arr)
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
        
        