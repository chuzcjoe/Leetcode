# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        if not head.next:
            return head
        
        
        new_head = head.next
        pre = ListNode(0)
        pre.next = head
        head = pre
        
        
        
        while head.next and head.next.next:
            n1,n2 = head.next, head.next.next
            n1.next = n2.next
            n2.next = n1
            head.next = n2
            head = n1
        
            
        return new_head