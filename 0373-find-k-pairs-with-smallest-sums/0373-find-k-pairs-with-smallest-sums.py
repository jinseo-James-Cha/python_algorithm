import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        one from nums1
        one from nums2
        return k number of smallest sum combinations
        """
        m, n = len(nums1), len(nums2)
        res = []
        seen_combinations = set()
        pq = [(nums1[0] + nums2[0], 0, 0)]
        while k > 0 and pq:
            curr_sum, u, v = heapq.heappop(pq)
            res.append([nums1[u], nums2[v]])

            if u+1 < m and (u+1, v) not in seen_combinations:
                heapq.heappush(pq, (nums1[u+1] + nums2[v], u+1, v))
                seen_combinations.add((u+1, v))
            
            if v+1 < n and (u, v+1) not in seen_combinations:
                heapq.heappush(pq, (nums1[u] + nums2[v+1], u, v+1))
                seen_combinations.add((u,v+1))
            k -= 1
        return res





        # brute force -> MLE
        # save all combinations and min heap pop
        all_combi = []
        for u in nums1[:k]:
            for v in nums2[:k]:
                heapq.heappush(all_combi, (u+v, u, v))
        
        res = []
        for _ in range(k):
            s, u, v = heapq.heappop(all_combi)
            res.append([u,v])
        return res
