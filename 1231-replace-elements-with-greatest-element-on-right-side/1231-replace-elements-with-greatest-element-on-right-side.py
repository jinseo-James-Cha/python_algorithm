class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in reversed(range(len(arr))):
            current = arr[i]
            arr[i] = greatest
            if current > greatest:
                greatest = current
        return arr


        # brute force
        # o(n^2) -> TL
        # res = [-1] * len(arr)

        # for i in range(len(arr) - 1):
        #     temp = 0 
        #     for j in range(i + 1, len(arr)):
        #         if arr[j] > temp:
        #             temp = arr[j]
        #     res[i] = temp
        # return res