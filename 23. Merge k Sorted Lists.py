# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        k = len(lists)
        res = []
        
        val_lists = [collections.deque([]) for i in range(k)]
        
        while any(lists):
            MIN_idx = 0
            MIN = float("inf")
            for i in range(k):
                if lists[i] and lists[i].val < MIN:
                    MIN_idx = i
                    MIN = lists[i].val
            
            root_val = lists[MIN_idx].val
            res.append(root_val)    
            lists[MIN_idx] = lists[MIN_idx].next
        
        if not res:
            return None
        
        head = ListNode(res[0])

        p = head
        for i in range(1, len(res)):
            cur = ListNode(res[i])
            p.next = cur
            p = p.next
        
        return head
        