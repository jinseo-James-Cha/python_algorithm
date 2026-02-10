class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        # 1-> 1 2
        # 3-> 3 4
        poisoned = duration
        prev = timeSeries[0]
        for i in range(1, len(timeSeries)):
            if timeSeries[i] >= prev + duration:
                poisoned += duration
            else:
                poisoned += timeSeries[i] - prev 
            prev = timeSeries[i]
        return poisoned