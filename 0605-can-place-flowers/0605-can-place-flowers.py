class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newbed = [0] + flowerbed[:] + [0]
        for i in range(1, len(flowerbed)+1):
            if newbed[i]:
                continue

            if not newbed[i-1] and not newbed[i+1]:
                newbed[i] = 1
                n -= 1

        return n <= 0



        # 1 0 0 0 1
        # 1 pass
        # 0 check -> prev and next are 0 then n - 1
        # -> way one
        # <- way one

        # -> way 1 "1" "1" 0 1 candidates 1, 2
        # <- way 1  0   1  1 1 only index 3 a
        # candidates = set()
        # len_flowerbed = len(flowerbed)
        # for i in range(len_flowerbed-1):
        #     if flowerbed[i]:
        #         continue
            
        #     if not flowerbed[i+1]:
        #         candidates.add(i)
        
        # for j in range(len_flowerbed-1, 0, -1):
        #     if flowerbed[j]:
        #         if j in candidates:
        #             candidates.remove(j)
        #         continue
            
        #     if flowerbed[j-1] and j in candidates:
        #         candidates.remove(j)
        
        # return len(candidates) == n