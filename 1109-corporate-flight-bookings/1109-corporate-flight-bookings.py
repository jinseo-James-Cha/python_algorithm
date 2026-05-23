class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * n

        for first, last, seats in bookings:
            prefix[first-1] += seats
            
            if last < n:
                prefix[last] -= seats
        
        for i in range(1, n):
            prefix[i] += prefix[i-1]
        
        return prefix