"""
Koko eating bananas
Minimum number of days to make m bouquets
Magnetic force between two balls
Split array largest sum
Divide chocolate (for premium users only)
Cutting ribbons (for premium users only)
Minimum Speed to Arrive on Time
"""
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # what is the minimum weight for a day?
        # left = max(weights)
        # if weight > capacity? cannot happen

        # what is the maximum weight for a day?
        # right = sum(weights)

        # capacity with days within this range.
        # binary search for capacity

        def is_possible(capacity):
            curr_days = 1
            curr_weight = 0
            for w in weights:
                if curr_weight + w > capacity:
                    curr_days += 1
                    curr_weight = 0
                curr_weight += w
            
            return curr_days <= days

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if is_possible(mid):
                right = mid
            else:
                left = mid + 1
        return left