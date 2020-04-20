# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(None)
        second = ListNode(None)
        prev = ListNode(None)
        dummy.next = head
        cur = head
        prev.next = head
        
        while cur:
            if not prev.val:
                prev = cur
                cur = cur.next
                continue
            
            if prev and prev.val <= cur.val:
                prev = cur
                cur = cur.next
            else:
                prev.next = cur.next
                start = dummy
                val = cur.val
                while 1:
                    if val <= start.next.val:
                        insert = ListNode(val, start.next)
                        start.next = insert
                        break
                    else:
                        start = start.next
                        
                cur = cur.next
            
        
        return dummy.next