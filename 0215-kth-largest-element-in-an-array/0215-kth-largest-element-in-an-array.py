import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # count sort
        min_val = min(nums)
        max_val = max(nums)
        count = [0] * (max_val - min_val + 1)

        for num in nums:
            count[num - min_val] += 1
        
        remain = k
        for num in range(len(count) - 1, -1, -1):
            remain -= count[num]
            if remain <= 0:
                return num + min_val
        return -1


        n = len(nums)
        heapq.heapify(nums)

        for _ in range(n - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)








        # counting sort
        min_num = min(nums)
        max_num = max(nums)
        counts = [0] * (max_num - min_num + 1)

        for num in nums:
            count_idx = num - min_num
            counts[count_idx] += 1
        
        remain = k
        for num in range(len(counts) -1, -1, -1):
            remain -= counts[num]
            if remain <= 0:
                return num + min_num
        
        return -1




        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

        # using max heap
        heapq.heapify(nums)
        i = len(nums)
        while i > k:
            heapq.heappop(nums)
            i -= 1
        
        return nums[0]
        
        # min heap
        def min_heapify(heap_size, index):
            left = index * 2 + 1
            right = index * 2 + 2
            largest = index

            if left < heap_size and nums[left] < nums[largest]:
                largest = left
            
            if right < heap_size and nums[right] < nums[largest]:
                largest = right
            
            if largest != index:
                nums[largest], nums[index] = nums[index], nums[largest]
                min_heapify(heap_size, largest)
            
        # initial heapify
        for i in range(len(nums)//2 -1, -1, -1):
            min_heapify(len(nums), i)
        
        # swap first and last and heapify
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            min_heapify(i, 0)
        
        return nums[k-1]
    
