# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        curr_next = curr.next
        curr.next = prev
        prev = curr
        curr = curr_next
    return prev

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        while True:
            scout = tail
            for _ in range(k):
                scout = scout.next
                if scout is None:
                    return dummy.next
            end_attachment = scout.next
            new_end = tail.next
            scout.next = None
            tail.next = None
            tail.next = reverse(new_end)
            new_end.next = end_attachment
            tail = new_end
        return dummy.next





