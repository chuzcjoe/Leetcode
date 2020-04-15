# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        
        
        dummy = cur = ListNode(0)
        
        cur.next = head
        seen = collections.OrderedDict()
        prefix = 0
        
        while cur:
            prefix += cur.val
            
            if prefix in seen:
                node = seen[prefix]
            else:
                node = cur
            
            while prefix in seen:
                seen.popitem()
            
            seen[prefix] = node
            node.next = cur.next
            cur = cur.next
        
        return dummy.next
            