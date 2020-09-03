class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        
        if len(hand) % W:
            return False
        
        hand = sorted(hand)
        n = len(hand) // W
        
        dic = collections.OrderedDict()
        need = collections.defaultdict(list)
        need['empty'].append(0)
        
        for i in range(0,n):
            dic[i] = []
        
        for a in hand:
            if need[a]:
                while need[a]:
                    idx = need[a].pop()
                    if len(dic[idx]) < W:
                        dic[idx].append(a) 
                        if len(dic[idx]) < W:
                            need[a+1].append(idx)
                        break
                    else:
                        continue
                                   
            elif need['empty']:
                idx = need['empty'].pop()
                dic[idx].append(a)
                if len(dic[idx]) < W:
                    need[a+1].append(idx)
                if idx < n-1:
                    need['empty'].append(idx+1)
                else:
                    need['empty'] = []
        
        for _, v in dic.items():
            if len(v) != W:
                return False
        
        return True
        