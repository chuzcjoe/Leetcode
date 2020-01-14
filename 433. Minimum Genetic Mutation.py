class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        
        chars = ['A','C','G','T']
        
        def gene_neighbor_word(word):
            for i in range(len(word)):
                for c in chars:
                    if c == word[i]:
                        continue
                    nw = word[:i] + c + word[i+1:]
                    if nw in bank:
                        yield nw
        
        
        link = [(start,0)]
        seen = {start}
        
        for w, cnt in link:
            for nei_w in gene_neighbor_word(w):
                if nei_w == end:
                    return cnt + 1
                if nei_w in bank and nei_w not in seen:
                    link.append((nei_w,cnt+1))
                    seen.add(nei_w)
        return -1
        