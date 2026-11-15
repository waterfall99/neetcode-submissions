"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        map = {}
        curr = head
        curr2 = curr
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next
        while curr2:
            map[curr2].next = map.get(curr2.next)
            map[curr2].random = map.get(curr2.random)
            curr2 = curr2.next
        return map[head]
        