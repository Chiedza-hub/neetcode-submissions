class UndergroundSystem:
    def __init__(self):
        self.checkInMap = {} # id : (startStation, time)
        self.totalMap = {} # (startstation, endstation) : [Totaltime, count]
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInMap[id]
        del self.checkInMap[id]
        if (startStation, stationName) not in self.totalMap:
            self.totalMap[(startStation, stationName)] = [0, 0]
        self.totalMap[(startStation, stationName)][0] += t - startTime
        self.totalMap[(startStation, stationName)][1] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.totalMap[(startStation, endStation)]
        return total / count
