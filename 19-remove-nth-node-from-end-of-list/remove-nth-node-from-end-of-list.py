# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            head=None
            return head
        dummy = ListNode(0)
        dummy.next = head
        a=dummy
        b=dummy
        for i in range(n+1):
            b=b.next
        while b:
            a=a.next
            b=b.next
        a.next=a.next.next
        return dummy.next
        
        
        
        


        