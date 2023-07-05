# Time: O(n)
# Space: O(n)


class Solution:
    def countPrimes(self, n: int) -> int:
        """Function to count the number of prime numbers
        less than n
        Args:
            n(int): an integer
        Returns:
            int: the number of prime numbers less than n
        """
        if n < 3:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, n):
            if primes[i]:
                for j in range(i*i, n, i):
                    primes[j] = False
        return sum(primes)
