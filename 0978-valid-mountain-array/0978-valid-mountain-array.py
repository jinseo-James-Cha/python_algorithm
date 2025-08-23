class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        # uphill
        top = -1
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                top = i
                break
            elif arr[i] == arr[i+1]:
                return False

        if top <= 0:
            return False
        
        for j in range(i, len(arr) - 1):
            if arr[j] < arr[j+1] or arr[j] == arr[j+1]:
                return False
        return True
        