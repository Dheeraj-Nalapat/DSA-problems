class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s ,f = head,head
        while f and f.next:
            f = f.next.next
            s = s.next
            if s==f:
                return True
        return False    
