class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_dic = {}
        
        if not nums:
            return None
        
        nums.sort()
        
        for num in nums:
            if num in freq_dic.keys():
                freq_dic[num] += 1
            else:
                freq_dic[num] = 1
        
        topK_freq = []
        srt = sorted(freq_dic.items(), key=lambda item:item[1])[::-1][0:k]
        for tu in srt:
            topK_freq.append(tu[0])
        
        return topK_freq
            
        
        
        