class Solution:
    def reformatDate(self, date: str) -> str:
        
        day, month, year = date.split(" ")
        
        day = day[:-2]
        if 1 <= int(day) <= 9:
            day = '0'+day
        
        dic = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = dic.index(month) + 1
        
        if 1 <= month <= 9:
            month = '0'+str(month)
        else:
            month = str(month)
        
        return year+'-'+month+'-'+day
        
        