class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        
        dic = collections.defaultdict(list)
        food = set()
        
        for order in orders:
            dic[order[1]].append(order[2])
            food.add(order[2])
            
        food = sorted(food)
        res = [["Table"] + food]
        
        d = sorted(dic.items(), key=lambda x: int(x[0]))
        
        for k,v in d:
            tmp = []
            for f in food:
                tmp.append(str(v.count(f)))
            
            res.append([k]+tmp)
        
        return res
            