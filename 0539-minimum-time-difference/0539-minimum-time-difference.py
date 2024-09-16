class Solution:
    def findMinDifference(self, timePoints: List[int]) -> int:
        def timeToMinutes(time):
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes

        minutesList = [timeToMinutes(time) for time in timePoints]
        minutesList.sort()

        minDiff = float('inf')

        for i in range(1, len(minutesList)):
            minDiff = min(minDiff, minutesList[i] - minutesList[i - 1])
        
        # Considering the circular difference between the last and first time
        # 1440 minutes in a day, calculating the wrap-around difference
        minDiff = min(minDiff, 1440 + minutesList[0] - minutesList[-1])
        
        return minDiff

        