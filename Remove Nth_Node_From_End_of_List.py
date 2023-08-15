# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        temp = head
        m=0
        while temp:
            m+=1
            temp = temp.next
        f = m-n
        res = ListNode()
        res = head
        if f==0:
            res = res.next
            return res
        for i in range(f-1):
            res = res.next   
        if res.next:    
            res.next = res.next.next 
        res = head      
        return res
