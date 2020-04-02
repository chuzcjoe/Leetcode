class UndergroundSystem:

    def __init__(self):
        
        self.station_in = collections.defaultdict(dict)
        self.station_out = collections.defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_id = id
        self.in_stationName = stationName
        self.in_t = t
        
        self.station_in[self.in_stationName][self.in_id] = self.in_t
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.out_id = id
        self.out_stationName = stationName
        self.out_t = t
        
        self.station_out[self.out_stationName][self.out_id] = self.out_t

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        res = 0
        cnt = 0
        
        for ID,T in self.station_out[endStation].items():
            if ID in self.station_in[startStation]:
                res += self.station_out[endStation][ID] - self.station_in[startStation][ID]
                cnt += 1
        return res / cnt
                


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)