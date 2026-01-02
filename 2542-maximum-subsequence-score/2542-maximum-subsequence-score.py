class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        n = len(nums1), len(nums2)
        k > 0

        choose subsequence of indices from nums1 as k much
        sum nums1 elements..
        selected elements * minimum in nums2

        return the maximum possible score

        1 3 3 2
        2 1 3 4    k == 3

        0 1 2
        0 1 3
        0 2 3
        1 2 3
        
        1 + 3 + 3 * min(2, 1 , 3)
        """
        # priority queue
        pairs = []
        for num1, num2 in zip(nums1, nums2):
            pairs.append((num1, num2))

        pairs.sort(key=lambda x: x[1], reverse=True)

        top_k_heap = [x[0] for x in pairs[:k]]
        top_k_sum = sum(top_k_heap)
        heapq.heapify(top_k_heap)

        # [(2, 4), (3, 3), (1, 2), (3, 1)]
        # 6, [1,2,3]
        answer = top_k_sum * pairs[k-1][1]

        for i in range(k, len(nums1)):
            top_k_sum -= heapq.heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heapq.heappush(top_k_heap, pairs[i][0])

            answer = max(answer, top_k_sum * pairs[i][1])
        return answer