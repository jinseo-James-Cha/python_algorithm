class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        """
        find all subarray and add its minimum element into return value
        """

        # monotonic stack
        MOD = 10 ** 9 + 7
        m_stack = []
        res = 0

        for i in range(len(arr) + 1):
            while m_stack and (i == len(arr) or arr[m_stack[-1]] >= arr[i]):
                mid = m_stack.pop()
                left = -1 if not m_stack else m_stack[-1]
                right = i

                count = (mid - left) * (right - mid)
                res += (count * arr[mid])
            
            m_stack.append(i)
        return res % MOD
    