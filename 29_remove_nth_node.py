# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cnt = 1
        
        pre = None
        
        def reverse(node):
            if not node:
                return None
        
            pre = None
        
            while node:
                next_node = node.next
                node.next = pre
                pre = node
                node = next_node
            
            return pre
        
        link1 = reverse(head)
        link1_ = link1
        
        while link1:
            if n == cnt and n == 1:
                    return reverse(link1.next)
                
            if cnt == n-1:
                link1.next = link1.next.next
                return reverse(link1_)
            
                
            
            cnt += 1
            link1 = link1.next
                