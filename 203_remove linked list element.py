# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        head_ = head
        dummy = ListNode(0)
        dummy.next = head
        
        pre = dummy
        
        while head:
            if head.val != val:
                pre = head
                head = head.next
            else:
                pre.next = head.next
                head = head.next
            
        return dummy.next
                
                
        