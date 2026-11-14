# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
 #        self.val = val
 #       self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None or head.next == None):
            return head
        elif(head.next.next == None):
            p = head
            q = p.next
            q.next = p
            p.next = None
        else:
            p = head
            q = p.next
            r = q.next
            head.next = None
            q.next = p
            while r!=None:
                p = q
                q = r
                r = r.next
                q.next = p
        head = q
        return head



        

            
        
