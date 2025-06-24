class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # flowers cannot be planted in adjacent plots.
        # 0 or 1
        # 0 -> empty
        # 1 -> not empty
        # n >= count is true
        # 1 0 0 0 1 -> 1 0 1 0 1  -> 1 is true but 2 is false

        # lets get the maximum num and check n <= count
        # fixed sliding window ?!
        # size 3 and move all to right and check 000 or not. 000 is count +=1
        count = 0
        l = len(flowerbed)
        if l < 3:
            if not 1 in flowerbed:
                count = 1
            return n <= count

        # check first 2
        if True not in flowerbed[0:2]:
            flowerbed[0] = 1
            count += 1
        
        # check last 2
        if True not in flowerbed[len(flowerbed)-2:]:
            flowerbed[len(flowerbed)-1] = 1
            count += 1

        # check middle
        left = 0
        right = 3
        while right < len(flowerbed):                
            if True not in flowerbed[left:right]:
                flowerbed[left + 1] = 1
                count += 1
            left += 1
            right += 1
        
        
        return n <= count