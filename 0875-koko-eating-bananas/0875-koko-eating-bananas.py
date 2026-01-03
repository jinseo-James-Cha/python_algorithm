class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        n = len(piles)
        piles[i] = how many banana
        guards have gone and will come back in n hour

        koko eating speed k
        if k > piles[i] -> koko eats all

        koko likes to eat slowly but still wants to finish eating all before guards return

        return minimum integer k she can eat all the bananas within h hours
        
        what is the question ?
        n = len(piles)
        h = guard will come back
        k = bananas per hour eating speed
        
        3 6 7 11
        1 2 2 3 => 8

        it doesn't need to keep the order.
        3 6 7 11

        return will be min ~ max
        if return hour <= h return 
        """
        left = 1
        right = max(piles)
        while left < right:
            middle = (left + right) // 2
            hour_spent = 0

            for pile in piles:
                hour_spent += math.ceil( pile / middle)
            
            if hour_spent <= h:
                right = middle
            else:
                left = middle + 1
        
        return left


        # TLE
        eating_speed_k = 1
        while True:
            total_hour = 0

            for pile in piles:
                total_hour += math.ceil(pile / eating_speed_k)
            
            if total_hour <= h:
                return eating_speed_k
            else:
                eating_speed_k += 1
        return -1


        # def check(target):
        #     total_hour = 0
        #     for num in piles:
        #         curr_target = target
        #         curr_hour = 1
        #         while num > curr_target: # 6 >= 4
        #             curr_target += curr_target
        #             curr_hour += 1
        #         total_hour += curr_hour
        #     return total_hour

        # n = len(piles)
        # min_b, max_b = min(piles), max(piles)
        # for k in range(min_b, max_b+1):
        #     if h >= check(k):
        #         return k
        # return max_b
