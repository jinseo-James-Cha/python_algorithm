from bisect import bisect_left
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # binary 1-soldier 0-civilian
        # weaker => 1. soldier less 2. if same soldier i < j
        
        # return weakest rows for k much
        # 2 4 1 2 5
        # 2 0 3 1 4

        # binary search for first 0
        def binary_search(row):
            left = 0
            right = len(row)
            while left < right:
                mid = (left + right) // 2
                if row[mid] == 1:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        soldiers = []
        for i, m in enumerate(mat):
            soldiers.append((binary_search(m) , i))

        soldiers.sort()

        res = []
        for i in range(k):
            res.append(soldiers[i][1])
        return res



        # brute force - > check by column
        added = set()
        res = []
        for col in range(len(mat[0])):
            for row in range(len(mat)):
                if mat[row][col] == 0 and row not in added:
                    added.add(row)
                    res.append(row)
                
                if len(added) == k:
                    return res
        
        if len(res) < k:
            for i in range(k):
                if i not in added:
                    added.add(i)
                    res.append(i)
                
                if len(added) == k:
                    break
        
        return res
        
        # bucket 
        # buckets = [[] for _ in range(len(mat[0]) + 1)]
        # for i, m in enumerate(mat):
        #     soldiers = m.count(1)
        #     buckets[soldiers].append(i)
        
        # res = [x for bucket in buckets for x in bucket]
        # return res[:k]

