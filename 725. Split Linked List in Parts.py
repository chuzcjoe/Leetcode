# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        
        LEN = []
        dummy = root
        n = 0
        while dummy:
            n += 1
            dummy = dummy.next
        
        for _ in range(k):
            if n % k == 0:
                LEN.append(n//k)
                n -= n//k
            else:
                LEN.append(n//k+1)
                n -= n//k + 1
            k -= 1
        
        dummy = prev = ListNode(None)
        res = []
        while LEN:
            l = LEN.pop(0)
            dummy = root
            cnt = 0
            while cnt < l:
                cnt += 1
                prev = root
                root = root.next
            prev.next = None
            res.append(dummy)
        
        return res