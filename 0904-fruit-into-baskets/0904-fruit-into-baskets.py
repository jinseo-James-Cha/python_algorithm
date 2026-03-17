class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # sliding window
        baskets = {}
        max_fruit = 0

        left = 0
        for right, fruit in enumerate(fruits):
            baskets[fruit] = baskets.get(fruit, 0) + 1

            while len(baskets) > 2:
                baskets[fruits[left]] -= 1

                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                left += 1
            
            max_fruit = max(max_fruit, right - left + 1)
        return max_fruit