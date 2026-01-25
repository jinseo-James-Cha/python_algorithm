class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # n candies
        # cancyType[i] = 
        
        # n/2 candies n is always even number
        # eat maximum number of different types of candies
        
        """
        1 1 2 2 3 3
        
        1: 2
        2: 2
        3: 2
        
        n = 6 -> alice can have up to 3 as n/2
        Alice can have 1, 2, 3 each
        
        1 1 2 3
        n = 4 -> alica can have up to 2 as n/2
        
        1, 2 or 1, 3 or 2,3
        
        min(set(types) and n/2)
        
        
        
        1 1 2 2 2 2 2 3 3 3
        
        1:2
        2:5
        3:3
        
        n//2 = 5
        type 3 3 type....1 each..
        
        """
        
        candyTypeSet = set(candyType)
        return min(len(candyType) // 2, len(candyTypeSet))