class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        # n = len(fruits)
        # fruits[i] = quantity of i type
        # basckets[j] = capacity of j basket

        # left most basket i -> 0..1.2. >= quantity
        # one type per basket
        # not possible -> no place

        # return the number of fruit types(i) cannot place -> no place..
        # 4 2 5
        # 3 5 4

        taken = set()
        n = len(fruits)

        for i in range(n):
            for j in range(n):
                if j in taken:
                    continue
                if fruits[i] <= baskets[j]:
                    taken.add(j)
                    break

        return n - len(taken)