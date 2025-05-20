class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, n):
            for j in range(i * i, n, i):
                primes[j] = False

        return primes.count(True)

# TLE
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 1:
#             return 0
        
#         primes = []
#         for num in range(2, n):
#             flag = True
#             for p in primes:
#                 if num % p == 0:
#                     flag = False
#                     break
#             if flag:
#                 primes.append(num)

#         return len(primes)

        