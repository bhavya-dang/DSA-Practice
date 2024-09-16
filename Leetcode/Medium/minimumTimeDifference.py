def findMinDifference(timePoints: list[int]) -> int:
    def timeToMinutes(time: str) -> int:
        hours, minutes = map(int, time.split(":"))
        return hours * 60 + minutes

    minutesList = [timeToMinutes(time) for time in timePoints]
    minutesList.sort() # since we need to find the minimum difference
    # now we know that the adjacent values will have the minimum diff

    minDiff = float('inf')

    for i in range(1, len(minutesList)):
        minDiff = min(minDiff, minutesList[i] - minutesList[i - 1])
    
    # Considering the circular difference between the last and first time
    # 1440 minutes in a day, calculating the wrap-around difference
    minDiff = min(minDiff, 1440 + minutesList[0] - minutesList[-1])
    
    return minDiff

timePoints1 = ["23:59", "00:00"]
timePoints2 = ["00:00", "23:59", "00:00"]

print(findMinDifference(timePoints1))  
print(findMinDifference(timePoints2))  
