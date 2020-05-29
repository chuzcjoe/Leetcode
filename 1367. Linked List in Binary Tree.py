# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        
        vals = ''
        while head:
            vals += str(head.val)+'|'
            head = head.next
        
        #return true if starting at this node can find the pattern
        def dfs(node, path):
            if vals in path:
                return True
            
            if not node:
                return False
            
            left = dfs(node.left, path+str(node.val)+'|')
            right = dfs(node.right, path+str(node.val)+'|')
            
            return left or right
        
        return dfs(root, '')
        
        