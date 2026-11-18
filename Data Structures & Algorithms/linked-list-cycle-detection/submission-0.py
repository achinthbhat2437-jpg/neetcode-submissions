# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head==None):
            return False
        p = head
        list1 = []
        while(p!=None):
            list1.append(p)
            if(p.next in list1):
                return True
            p = p.next
        return False
        