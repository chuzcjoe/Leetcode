class Solution:
    def entityParser(self, text: str) -> str:
        
        entities = {'&quot;':'\"','&apos;':'\'','&amp;':'&','&gt;':'>','&lt;':'<','&frasl;':'/'}
        
        res = []
        
        for i,s in enumerate(text):
            if s == '&' and text[i:i+4] in entities:
                res.append([i,i+4,entities[text[i:i+4]]])
            
            elif s == '&' and text[i:i+5] in entities:
                res.append([i,i+5,entities[text[i:i+5]]])
            
            elif s == '&' and text[i:i+6] in entities:
                res.append([i,i+6,entities[text[i:i+6]]])
            
            elif s == '&' and text[i:i+7] in entities:
                res.append([i,i+7,entities[text[i:i+7]]])
        
        txt_list = [s for s in text]
        for left, right, rep in res:
            txt_list[left:right] = ['']*(right-left)
            txt_list[left] = rep
        
        return "".join(txt_list)