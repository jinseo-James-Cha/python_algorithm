# Sliding window
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_days = 0
        fruit_basket = defaultdict(int)
        fruit_set = set()
        for right in range(len(fruits)):
            fruit_basket[fruits[right]] += 1
            fruit_set.add(fruits[right])
            
            while len(fruit_set) > 2:
                fruit_basket[fruits[left]] -= 1
                if fruit_basket[fruits[left]] == 0:
                    fruit_set.remove(fruits[left])
                left += 1
            
            max_days = max(max_days, right - left + 1)
        
        return max_days

        # two types only
        # baskets = set() # allow two type -> X
        # set is not available cuz I need to move left one by one
        # try with hashmap
        baskets = {} # 'type': count
        maximum = 0

        # left pointer remove respectively
        left = 0
        for right in range(len(fruits)):
            # baskets.add(fruits[right])
            baskets[fruits[right]] = baskets.get(fruits[right], 0) + 1
            
            while len(baskets) > 2: # two types fruit only
                baskets[fruits[left]] -= 1
                
                if baskets[fruits[left]] == 0:
                    del baskets[fruits[left]]
                
                left += 1
            maximum = max(maximum, right - left + 1)
        return maximum







# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         if len(fruits) == 1:
#             return 1
        
#         # save two fruit types 
#         # using dict? or what?
#         baskets = {} 
#         left = 0
#         m = 0
#         for right in range(len(fruits)):
#             baskets[fruits[right]] = baskets.get(fruits[right], 0) + 1
            
#             while len(baskets) > 2:
#                 baskets[fruits[left]] -= 1
#                 if baskets[fruits[left]] == 0:
#                     del baskets[fruits[left]]
#                 left += 1

#             m = max(right - left + 1, m)
#         return m


# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
#         # count # of two types
#         # 1 <= fruits.length <= 10^5 -> O(N^2) is not available

#         # my idea
#         # add +1 into Dictionary and descending order and sum first 2 value
#         # but we dont need key, so let me try with array
#         d = [0] * len(fruits)
#         for f in fruits:
#             d[f] += 1
        
#         d.sort(reverse = True)
#         return d[0] + d[1]


# class Solution:
#     def totalFruit(self, fruits: List[int]) -> int:
        # problem understanding failed
        # it wants the maximum num of 2 types in a row
        # I think I have done something like this and it uses two pointers.
        # if len(fruits) == 1:
        #     return 1
        
        # baskets = {}
        # left = 0
        
        # baskets[fruits[left]] = left
        # m = 1
        # for right in range(1, len(fruits)):
        #     print("right", right)
        #     if len(baskets) < 2:
        #         if fruits[right] not in baskets:
        #             # register the first index of the type
        #             baskets[fruits[right]] = right
        #         else:
        #             # already registered 
        #             continue
        #     elif fruits[right] in baskets:
        #         print("got same continue")
        #     else:
        #         # update baskets with new type
        #         del baskets[fruits[left]]

        #         # update left with remained basket
        #         for t, i in baskets.items():
        #             left = i
        #         baskets[fruits[right]] = right

        #     print("left", left)
        #     print("baskets", baskets)

        #     if len(baskets) == 2:
        #         print("answer", right- left + 1)
        #         m = max(right - left + 1, m)

        # return m
