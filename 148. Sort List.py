# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        if not head or not head.next:
            return head
        
        slow = fast = head
        prev = ListNode(None)
        prev.next = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # cut down in the half
        prev.next = None
        
        left = self.sortList(head)
        right = self.sortList(slow)
        
        return self.merge(left, right)
    
    def merge(self, left, right):
        
        dummy = prev= ListNode(None)
        
        while left and right:
            if left.val < right.val:
                prev.next = left
                prev = left
                left = left.next
            else:
                prev.next = right
                prev = right
                right = right.next
        
        if not left:
            prev.next = right
        
        if not right:
            prev.next = left
        
        return dummy.next
        