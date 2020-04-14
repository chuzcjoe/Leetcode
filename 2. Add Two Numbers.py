# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num1 = num2 = ""
        
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        
        res = str(int(num1[::-1]) + int(num2[::-1]))[::-1]

        p = head = ListNode(0)
        n = 0
        
        while n < len(res):
            cur = ListNode(res[n])
            p.next = cur
            p = cur
            n += 1
        
        return head.next

            
        
        
        
        