import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
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
    
