import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force
        # sort by descending and then nums[k-1]
        # sort by ascending and then nums[-k]

        # using min heap 
        # o(n log n)
        # adding each element and then pop the minimum in the queue if len(queue) == k
        # it contains k size elements and the first elements will be the answer
        pq = []
        for num in nums:
            heapq.heappush(pq, num)
            if len(pq) > k:
                heapq.heappop(pq)
        
        return pq[0]

        # using bucket sort
        min_val, max_val = min(nums), max(nums) # 1 , 6
        bucket = [0] * (max_val - min_val +1) # 6 - 1 + 1 => 6

        for num in nums:
            bucket[num-min_val] += 1
        
        for i in range(len(bucket)-1, -1, -1):
            k -= bucket[i]

            if k <= 0:
                return i+min_val
        
        return -1



















        # min heap
        # insert in to heapq
        # check size if > k and then we need to pop the minimum .
        # return min heap's first one.

        pq = []
        for num in nums:
            heapq.heappush(pq, num)

            if len(pq) > k:
                heapq.heappop(pq)
        return pq[0]

        # counting sort
        min_val = min(nums)
        max_val = max(nums)
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num-min_val] += 1

        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_val
        return -1



        """
        kth largest -> max heap and take out 0?

        1 2 3 4 5
        1 2 3
          2 3 4
            3 4 5 
            pop()
        3 7 8 1 2
        3 7 8
          3 7 8
        """
        pq = [] # min-heap
        for num in nums: # O(n)
            heapq.heappush(pq, num) 

            if len(pq) > k:
                heapq.heappop(pq) # O(log k)

            # if len(pq) < k:
            #     heapq.heappush(pq, num)
            # elif pq[0] < num:
            #     heapq.heappop(pq)
            #     heapq.heappush(pq, num)
        return pq[0]
        # [3,2,1,5,6,4]

