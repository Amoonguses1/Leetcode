from typing import List
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # brute force
        # Time: O(nK)
        # Space: O(n)
        # K = len(primes)
        """
        numbers = [1]
        pos = [0] * len(primes)
        for _ in range(1, n):
            candidates = []
            for j, prime in enumerate(primes):
                candidates.append(prime*numbers[pos[j]])
            minimum = min(candidates)
            for j, candidate in enumerate(candidates):
                if candidate == minimum:
                    pos[j] += 1
            numbers.append(minimum)
        return numbers[-1]
        """
        # heap
        # Time: O(nlogK)
        # Space: O(n)
        nums = primes.copy()
        heapq.heapify(nums)
        p = 1
        for _ in range(n-1):
            p = heapq.heappop(nums)
            for prime in primes:
                heapq.heappush(nums, p * prime)
                if p % prime == 0:
                    break
        return p
