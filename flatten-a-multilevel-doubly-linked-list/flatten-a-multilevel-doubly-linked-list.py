"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return
        
        stack = []
        current = head
        
        while current:
            if current.child:
                if current.next:
                    stack.append(current.next)
                current.next = current.child
                current.next.prev = current
                current.child = None
            
            elif not current.next and stack:
                current.next = stack.pop()
                current.next.prev = current
            current = current.next
        
        return head