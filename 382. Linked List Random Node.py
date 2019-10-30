# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.first = head
        self.head = head
        self.n = 1
        while head.next:
            head = head.next
            self.n += 1

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        choi = random.choice(range(1,self.n+1))
        for i,_ in enumerate(range(choi)):
            if i == 0:
                continue
            self.head = self.head.next
            
        val = self.head.val
        self.head = self.first
        return val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()