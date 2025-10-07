import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 1  5   9
        # 10 11  13
        # 12 13  15
        n = len(matrix)
        pq = []
        for i in range(n):
            for j in range(n):
                heapq.heappush(pq, -matrix[i][j])
        
        for largest in range(n*n - k):
            heapq.heappop(pq)
        
        return -pq[0]
            
        