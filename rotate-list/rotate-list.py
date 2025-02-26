# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        nhead = head
        count = 1
        
        while nhead.next:
            count += 1
            nhead = nhead.next
        
        k %= count
        k = count - k
        
        if k == count:
            return head
        
        nhead = head
        
        while k > 1:
            k -= 1
            nhead = nhead.next
        
        ans = nhead.next
        nhead.next = None
        
        findTail = ans
        
        while findTail.next:
            findTail = findTail.next
        
        findTail.next = head
        
        return ans