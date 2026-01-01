class ListNode:
    def __init__ (self, x):
        self.val = x
        self.next = None
        
        
class Solution:
    def detectcycle(self, head):
        if not head or not head.next:
            return None
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                start = head
                while start != slow:
                    start = start.next 
                    slow = slow.next
                    
                return start
            
        return None    