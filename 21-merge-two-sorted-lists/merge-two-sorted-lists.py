# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head=dummy
        temp=head
        t1=list1
        t2=list2
        while t1 and t2:
            if t1.val<= t2.val:
                 temp.next=ListNode(t1.val)
                 t1=t1.next
            else:
                temp.next=ListNode(t2.val)
                t2=t2.next
            temp=temp.next
        
        if t1:
            temp.next = t1

        if t2:
            temp.next = t2
        return head.next




            #jo bhi kum hai usko dummy ke end me dal0




        

        