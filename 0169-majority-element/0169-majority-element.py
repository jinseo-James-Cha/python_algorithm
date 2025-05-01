# n = len(nums)
# n / 2 > majority num
# len 7 includes more than 4

# O(1) in space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # follow up - space O(N)
        m_e = c = 0
        for n in nums:
            if c == 0:
                m_e = n
            
            c += 1 if n == m_e else -1

        return m_e

        # time O(N)
        # space O(N)
        # h = {}
        # m_value = m_key = 0
        # for n in nums:
        #     h[n] = h.get(n, 0) + 1
        #     if h[n] > m_value:
        #         m_value = h[n]
        #         m_key = n
        # return m_key

        # memory limit exceeded
        # answer = [0] * (max(nums) + 1)
        
        # for n in nums:
        #     answer[n] += 1

        # return answer.index(max(answer))

