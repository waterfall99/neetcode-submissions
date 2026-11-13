# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next
        slow.next = None
        curr = second_half
        prev = None
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr  
            curr = nxt
        first = head
        second = prev
        while second is not None:
            firstnxt = first.next
            secondnxt = second.next
            first.next = second
            second.next = firstnxt
            first = firstnxt
            second = secondnxt







