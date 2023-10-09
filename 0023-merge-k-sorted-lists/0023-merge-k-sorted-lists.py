# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        count = 0  

        for head in lists:
            if head:
                heapq.heappush(min_heap, (head.val, count, head))
                count += 1

        dummy = ListNode()
        curr = dummy

        while min_heap:
            val, _, node = heapq.heappop(min_heap) 
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, count, node.next))
                count += 1

        return dummy.next
