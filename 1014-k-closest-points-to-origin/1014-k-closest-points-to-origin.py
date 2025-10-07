import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # as k much, we need the answers
        
        def quick_select(left, right, k):
            if left <= right:
                pivot_idx = partition(left, right)
                if pivot_idx == k:
                    return
                elif pivot_idx < k:
                    quick_select(pivot_idx+1, right, k)
                else:
                    quick_select(left, pivot_idx-1, k)
        
        def partition(left, right):
            pivot = dist(points[right])
            i = left
            for j in range(left, right):
                if dist(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i
        
        
        def dist(p):
            return p[0]**2 + p[1]**2
        
        quick_select(0, len(points)-1, k)
        return points[:k]        
        
        
        
        
        
        
        
        
        
        
        # quickselect
        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        def partition(left, right):
            pivot = dist(points[right])
            i = left
            for j in range(left, right):
                if dist(points[j]) <= pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[right] = points[right], points[i]
            return i

        def quickselect(left, right, k):
            if left <= right:
                pivot_index = partition(left, right)
                if pivot_index == k:
                    return
                elif pivot_index < k:
                    quickselect(pivot_index + 1, right, k)
                else:
                    quickselect(left, pivot_index - 1, k)

        quickselect(0, len(points) - 1, k)
        return points[:k]






        # priority queue -> max heap
        
        max_heap = []
        for x, y in points:
            val = (x-0)**2 + (y-0)**2
            heapq.heappush(max_heap, [-val, x, y])
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        res = []
        for val, x, y in max_heap:
            res.append([x, y])
        
        return res
