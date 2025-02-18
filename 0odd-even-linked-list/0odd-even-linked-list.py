# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        even = []
        odd = []
        cur = head
        
        if not cur or not cur.next:
            return head
        while cur and cur.next:
            even.append(cur.val)
            odd.append(cur.next.val)
            cur = cur.next.next
        
        if cur:
            even.append(cur.val)
            
        _sum = even+odd
        result = ListNode()
        
        for i,num in enumerate(_sum):
            if i == 0 :
                result.val = num
            else :
                node = result
                while node.next != None:
                    node = node.next
                node.next = ListNode(num)
        return result