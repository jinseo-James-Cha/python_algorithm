class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heap sort
        def max_heapify(heap_size, index):
            left = index * 2 + 1
            right = index * 2 + 2
            largest = index

            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            
            if right < heap_size and nums[right] > nums[largest]:
                largest = right
            
            if largest != index:
                nums[largest], nums[index] = nums[index], nums[largest]
                max_heapify(heap_size, largest)
            
        # initial heapify
        for i in range(len(nums)//2 -1, -1, -1):
            max_heapify(len(nums), i)
        
        # swap first and last and heapify
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            max_heapify(i, 0)
        
        return nums[len(nums) - k]
    
