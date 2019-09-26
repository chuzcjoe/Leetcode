# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        head_ = head
        
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
                continue
            head = head.next
            
            
        return head_
            
            
        