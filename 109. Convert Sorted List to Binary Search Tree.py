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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        val = []
        
        while head:
            val.append(head.val)
            head = head.next
        
        def buildBST(nodes, left, right):
            
            if left > right:
                return
            
            mid = (left+right) // 2
            
            root = TreeNode(nodes[mid])
            
            root.left = buildBST(nodes, left, mid-1)
            root.right = buildBST(nodes, mid+1, right)
            
            return root
        
        return buildBST(val, 0, len(val)-1)
        