class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def removenthfromend(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        fast = dummy
        slow = dummy
        
        for _ in range(n+1):
            fast = fast.next
            
        while fast:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next
    