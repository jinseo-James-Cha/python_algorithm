class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ### Problem
        # i < j < j, arr[i], arr[j], arr[k]
        # abs(arr[i] - arr[j]) <= a
        # ...

        ### Approaching
        # 3 nested loops..? 
        # no...uhm I wannt to do with 3 pointers.. -> no it cannot be j not moving..
        # especially, k <= next element -> res += 1

        ### Sovled O(n^3)
        res = 0
        n = len(arr)
        for i in range(n - 2):
            for j in range(i+1, n - 1):
                for k in range(j + 1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res
                    

