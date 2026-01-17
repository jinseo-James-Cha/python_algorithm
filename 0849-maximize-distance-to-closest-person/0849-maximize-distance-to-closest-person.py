class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maximum_closest = 0
        
        # in between
        left = -1
        for right in range(len(seats)):
            if seats[right] == 1:
                if left == -1:
                    maximum_closest = right
                else:
                    maximum_closest = max(maximum_closest, (right - left) // 2)
                left = right
        
        # 0 end in the seats
        if left != -1:
            maximum_closest = max(maximum_closest, len(seats) - 1 - left) # 4 - 0 or 2-2
        
        return maximum_closest