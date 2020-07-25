# https://leetcode.com/problems/count-primes/
# 204. Count Primes

# Count the number of prime numbers less than a non-negative number, n.

# Example:
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""
Time Complexity: o(n)
Space Complexity: o(n)
"""

class Solution:
    def countPrimes(self, n: int) -> int:
      #what makes something a prime number?
      #prime numbers are numbers that have only 2 factors: 1 and themselves

      # no prime number less than 2
      if n < 3:
          return 0

      # create a list for making numbers less than n
      lst = [True] * n

      # 0 and 1 are not prime numbers
      lst[0] = lst[1] = False

      count = 0
      for i in range(2, n):
        if lst[i]:
          for j in range(i*i, n, i):  # range(2, 10, 2)
            lst[j] = False

      for i in range(n):
        if lst[i]:
          count += 1

      return count
