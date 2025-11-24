import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        m, n = len(nums1), len(nums2)

        res = []
        visited = set()

        min_heap = [(nums1[0] + nums2[0], (0,0))]
        while k > 0 and min_heap:
            s, (i, j) = heapq.heappop(min_heap)
            res.append([nums1[i], nums2[j]])

            if i+1 < m and (i+1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))
            
            if j+1 < n and (i, j+1) not in visited:
                heapq.heappush(min_heap, (nums1[i]+nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
            
            k -= 1
        return res
        


        # ascending order
        # [one from nums1 , second from nums2]

        # 1 7 11 // 2 4 6
        # 12
        # 14
        # 16
        # get all combinations and then sort by sum and cut k
        # Memory Limit Exceeded
        all_combinations = []
        for num1 in nums1[:k]:
            for num2 in nums2[:k]:
                heapq.heappush(all_combinations, (num1 + num2, num1, num2))
        
        res = []
        for _ in range(k):
            s, u, v = heapq.heappop(all_combinations)
            res.append([u,v])
        return res