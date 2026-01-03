class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)

        def lower_bound_binary_search(target):
            left = 0
            right = len(potions)
            while left < right:
                mid = (left + right) // 2
                if potions[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return len(potions) - left


        res = []
        potions.sort()
        for spell in spells:
            # spell * potions >= success
            # potions >= success / spell
            # ceil(a / b) = (a + b - 1) // b
            target = (success + spell - 1) // spell
            res.append(lower_bound_binary_search(target))
        return res