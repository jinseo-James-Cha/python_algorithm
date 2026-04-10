class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve of Eratosthenes
        if n <= 2:
            return 0

        arr = [True] * n
        arr[0], arr[1] = False, False
        for i in range(2, int(math.sqrt(n)) + 1):
            if not arr[i]:
                continue
            
            for j in range(i*i, n, i):
                arr[j] = False
        return sum([arr[i] for i in range(2, n) if arr[i]])


        # optimize brute force: O(n * sqrt(n))) : O(n times square root of n)
        def is_prime_number(i):
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    return False
            return True

        return sum([is_prime_number(x) for x in range(2, n)])
        
        # brute force : O(n^2) -> TLE
        def is_prime_number(i):
            for j in range(2, i):
                if i % j == 0:
                    return False
            return True

        return sum([is_prime_number(x) for x in range(2, n)])