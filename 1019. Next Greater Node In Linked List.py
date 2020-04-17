# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        stack = []
        ans = []
        index = 0
        
        while head:
            
            cur_val = head.val
            ans.append(0)
            
            while stack and stack[-1][0] < cur_val:
                last = stack.pop()
                ans[last[1]] = cur_val
                
            stack.append((cur_val, index))
            index += 1
            head = head.next
        
        return ans
            
        