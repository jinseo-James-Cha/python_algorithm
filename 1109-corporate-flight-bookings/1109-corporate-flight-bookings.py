class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        prefix
        starting point += seats
        end point -= seats

        bookings = [[1,2,10],[2,3,20],[2,5,25]]
        n = 5

        [10,45,-10,-20,0]
        =>
        [10,
            10+45=55,
            55-10=45,
            45-20=25,
        25]

        """

        prefix = [0] * n

        for first, last, seats in bookings:
            prefix[first-1] += seats
            
            if last < n:
                prefix[last] -= seats
        
        for i in range(1, n):
            prefix[i] += prefix[i-1]
        
        return prefix