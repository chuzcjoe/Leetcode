# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return None
        
        
        odd = ListNode(0)
        even = ListNode(0)
        
        odd = head
        odd_ = head
        even = head.next
        
        evenhead = head.next
        
        while odd.next and odd.next.next:
            
            odd.next = odd.next.next
            odd = odd.next
            temp = odd.next
            even.next = temp
            even = temp
            
        odd.next = evenhead
        return head
            