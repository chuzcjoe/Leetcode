class Solution:
    def arrangeWords(self, text: str) -> str:
        
        text = text.lower().split(" ")
        text = sorted(text, key=lambda x: len(x))
        
        text[0] = text[0][0].upper() + text[0][1:]
        
        return " ".join(text)