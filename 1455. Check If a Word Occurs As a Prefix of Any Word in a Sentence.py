class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        sentence = sentence.split(" ")
        
        for i,s in enumerate(sentence):
            if len(s) >= len(searchWord) and searchWord==s[:len(searchWord)]:
                return i+1
        
        return -1
            