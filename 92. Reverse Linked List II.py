# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        prev = ListNode(None)
        cur = head
        prev.next = head
        dummy = head
        left = right = ListNode(None)
        start = end = ListNode(None)
        
        i = 0
        while head:
            i += 1
            if i == m:
                start = prev
                left = head
            if i == n:
                end = head.next
                right = head
                break
            prev = head
            head = head.next


        right.next = None
        dummy_left = left
        prev = ListNode(None)
    
        while left:
            nxt = left.next
            left.next = prev
            prev = left
            left = nxt
        
        print(start)
        start.next = prev
        dummy_left.next = end

        if m == 1:
            return start.next
        else:
            return dummy