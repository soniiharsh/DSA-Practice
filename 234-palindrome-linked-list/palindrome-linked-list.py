# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        prev=None
        curr=head
        while curr:
            store=curr.next
            curr.next=prev
            prev=curr
            curr=store
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=self.reverseList(slow)
        first =head
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next
        return True

        
    
        