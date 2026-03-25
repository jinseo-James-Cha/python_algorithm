class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # n log n -> heap sort
        def max_heapify(heap_size, index):
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index
            if left < heap_size and nums[largest] < nums[left]:
                largest = left
            
            if right < heap_size and nums[largest] < nums[right]:
                largest = right
            
            if largest != index:
                nums[largest], nums[index] = nums[index], nums[largest]
                max_heapify(heap_size, largest)
        
        for i in range(len(nums)//2 - 1, -1, -1):
            max_heapify(len(nums), i)

        for i in range(len(nums) - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            max_heapify(i, 0)
        
        return nums
        """
        Quicksort -> Countsort
        Time complexity: O(n + k) # k is the maximum number in nums
        Space complexity: O(n + k) # res: n and counts: k
        constraints 
        0 <= nums[i] <= 10^3
        => Counting sort become better

        nums =   2 1 0 0 2 4 2
        counts = [2, 1, 3, 0, 1]
        res = [0,0, 1, 2,2,2, 4]
        """
        counts = [0] * (max(nums) + 1)
        for num in nums:
            counts[num] += 1
        
        res = []
        for i, count in enumerate(counts):
            res.extend([i] * count)
        
        return res

        """
        Quicksort # Useful for in-place sorting
        avg O(n log n)
        worst O(n^2) -> if it is already sorted, 1 2 3 4 and partitions keep unbalancing left and right
        = by placing each number in its sorted position one at a time

        partitioning - place left with smaller, and right with greather than the pivot
        6 8 4 2 7 3 1 5 => 5 is pivot
        4 2 3 1  5  6 8 7 
        S S S S  P  G G G => pivot 5 found its correct position 

        pseudocode
        def quicksort(nums, left, right):
            pivot_index = partition(nums, left, right)
            quicksort(nums, left, pivot_index - 1)
            quicksort(nums, pivot_index + 1, right) 
        """
        # can make worst case => T: O(n^2) S: O(n)
        def partition(nums, left, right):
            pivot = nums[right]
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[left] = nums[left], nums[i]
                    left += 1
            nums[left], nums[right] = nums[right], nums[left]
            return left                    

        def quicksort(nums, left, right):
            if left >= right:
                return

            # using random access
            random_index = random.randint(left, right)
            nums[random_index], nums[right] = nums[right], nums[random_index]

            pivot_index = partition(nums, left, right)
            quicksort(nums, left, pivot_index - 1)
            quicksort(nums, pivot_index + 1, right) 

        quicksort(nums, 0, len(nums) - 1)
        return nums

        
  

        # bottom up
        def merge(left_list, right_list):
            left_index, right_index = 0,0
            merged_list = []
            while left_index < len(left_list) and right_index < len(right_list):
                if left_list[left_index] >= right_list[right_index]:
                    merged_list.append(right_list[right_index])
                    right_index += 1
                else:
                    merged_list.append(left_list[left_index])
                    left_index += 1
            merged_list.extend(left_list[left_index:])
            merged_list.extend(right_list[right_index:])
            
            return merged_list

        n = len(nums)
        width = 1
        while width < n:
            new_nums = []
            for i in range(0, n, 2 * width):
                left = nums[i:i+width]
                right = nums[i+width:i+2*width]
                new_nums.extend(merge(left, right))
            nums = new_nums
            width *= 2
        return nums



        # top down
        def merge(left_list, right_list):
            left_index, right_index = 0,0
            merged_list = []
            while left_index < len(left_list) and right_index < len(right_list):
                if left_list[left_index] >= right_list[right_index]:
                    merged_list.append(right_list[right_index])
                    right_index += 1
                else:
                    merged_list.append(left_list[left_index])
                    left_index += 1
            merged_list.extend(left_list[left_index:])
            merged_list.extend(right_list[right_index:])
            
            return merged_list


        if len(nums) <= 1:
            return nums
        
        pivot = len(nums) // 2
        left_list = self.sortArray(nums[:pivot])
        right_list = self.sortArray(nums[pivot:])
        return merge(left_list, right_list)

