# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        aMap = set()
        
        while headA:
            aMap.add(headA) 
            headA = headA.next
        
        while headB:
            if headB in aMap:
                return headB
            else:
                headB = headB.next
        return None