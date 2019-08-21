class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return None
        
        queue = []
        cnt = 0
        
        def swap(q,x):
            new_q = [0] * (len(q)+1)
            if x >= q[0]:
                    new_q[1:] = q
                    new_q[0] = x
                    #print(new_q)
                    return new_q
            elif x <= q[-1]:
                    new_q[0:-1] = q
                    new_q[-1] = x
                    #print(new_q)
                    return new_q
            else:
                for i in range(1,len(q)):
                    if q[i-1] >= x and x >= q[i]:
                        new_q[0:i] = q[0:i]
                        new_q[i] = x
                        new_q[i+1:] = q[i:]
                        return new_q
                    
                    
        for num in nums:
            if not queue:
                #print(queue)
                queue.append(num)
                #print(queue)
            else:
                #print(queue)
                queue = swap(queue,num)
        return queue[k-1]
                    
            