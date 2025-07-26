class Solution:
    def divisorGame(self, n: int) -> bool:
        # alice -> bob
        # 0 < x < n and n % x == 0 x는 n보다 작은 약수겠군
        # n -= x
        # true if alice win -> 홀수번으로 나오면 이기는거야.
        # 약수의 개수가 2n + 1 이면 True
        
        # 1:  False
        # 2: 1고르고 True
        # 3: 1고르고 -> 1고르고 False
        # 4: 1고르고 -> 1고르고 -> 1고르고 True
        return n % 2 == 0

 