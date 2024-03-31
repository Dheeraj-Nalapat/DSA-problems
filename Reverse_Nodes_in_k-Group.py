# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None
        current = head
        Next = None
        Prev = None
        count = 0
        count1 = 0
        current1 =head
        while current1 and count1<k:
            current1 = current1.next
            count1 += 1
        if count1 == k:   
            while current and count < k:
                Next = current.next
                current.next = Prev
                Prev = current
                current = Next
                count += 1
        else :
            Prev = current
            while current and count < k:
                current = current.next 
                count += 1       
        if current:
            head.next = self.reverseKGroup(current,k)
        return Prev    
