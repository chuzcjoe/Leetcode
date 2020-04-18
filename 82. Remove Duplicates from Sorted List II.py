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
        
        prev = ListNode(None)
        prev.next = head
        dummy = head
        cur = head
        flg = False
        
        counter = collections.Counter()
        while head:
            counter[head.val] += 1
            head = head.next
        
        while dummy:
            if counter[dummy.val] == 1:
                break
            else:
                dummy = dummy.next
            
        
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
        
        return dummy
            
            
            
        