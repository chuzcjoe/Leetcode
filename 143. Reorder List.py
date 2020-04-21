# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        slow = fast = head
        
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        dummy = slow.next
        slow.next = None
        
        # reverse the right part
        prev = ListNode(None)
        cur = dummy
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # start from the new root
        right = prev
        left = head
        
        while 1:
            if not prev.next.val:
                prev.next = None
                break
            prev = prev.next
            
        while left and right:
            left_second = left.next
            right_second = right.next
            
            left.next = right
            right.next = left_second
            
            left = left_second
            right = right_second
        
        return head
            
        