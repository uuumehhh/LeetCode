# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        turtle = rabbit = head
        i = 0
        loop = -1
        
        while(rabbit and rabbit.next):
            turtle = turtle.next
            rabbit = rabbit.next.next
            
            if turtle == rabbit:
                turtle = head
                
                while(turtle != rabbit):
                    turtle = turtle.next
                    rabbit = rabbit.next
                return turtle
        return None
        