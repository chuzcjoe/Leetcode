class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        
        def gene_neighbor_word(word):
            for i in range(len(word)):
                for j in range(26):
                    nw = word[:i]+chr(97+j)+word[i+1:]
                    if nw in wordList:
                        yield nw
        
        link = [(beginWord,1)]
        seen = {beginWord}
        
        for w, cnt in link:
            for nei_w in gene_neighbor_word(w):
                if nei_w == endWord:
                    return cnt + 1
                if nei_w in wordList and nei_w not in seen:
                    link.append((nei_w,cnt+1))
                    seen.add(nei_w)
        return 0
        