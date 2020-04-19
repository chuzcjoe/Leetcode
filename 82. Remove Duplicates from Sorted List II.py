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
        
        prev = dummy = ListNode(None)
        prev.next = head
        cur = head
        flg = False
            
        
        while cur and cur.next:
            while cur.next and cur.val == cur.next.val:
                flg = True
                cur = cur.next
                
            if flg:
                cur = cur.next
                prev.next = cur
                flg = False
                continue
            
            prev = cur
            cur = cur.next
        
        return dummy.next
            
            
            
        