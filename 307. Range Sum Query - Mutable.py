class Node:
    def __init__(self, start, end, sum=0, left=None, right=None):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = left
        self.right = right
        

class NumArray:

    def __init__(self, nums: List[int]):
        
        def buildTree(l,r,nums):
            if l > r:
                return None
            
            if l == r:
                return Node(l,l,nums[l])
            
            mid = (l+r) // 2
            left = buildTree(l,mid,nums)
            right = buildTree(mid+1,r,nums)
            
            return Node(l,r,left.sum+right.sum, left, right)
        
        self.root = buildTree(0,len(nums)-1,nums)
        

    def update(self, i: int, val: int) -> None:
        
        def updateVal(root, i, val):
            if root.start == root.end== i:
                root.sum = val
                return
            
            mid = (root.start+root.end) // 2
            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)
            
            root.sum = root.left.sum + root.right.sum
        
        return updateVal(self.root, i, val)
        

    def sumRange(self, i: int, j: int) -> int:
        
        def querysum(root, i, j):
            if root.start == i and root.end == j:
                return root.sum
            
            mid = (root.start+root.end) // 2
            if j <= mid:
                return querysum(root.left, i, j)
            elif i > mid:
                return querysum(root.right, i, j)
            else:
                return querysum(root.left, i, mid) + querysum(root.right, mid+1, j)
        
        return querysum(self.root, i, j)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)