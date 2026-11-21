from math import comb
class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        # red, blue : at least 1 length
        available = n - k
        # blank_1 , red, blank_2, blue, blank_3 : sum = available, each >= 0 :example of k = 2
        # generalization: blank_1, red_1, blank_2, red_2, ..., blank_k, red_k, blank_(k+1) : sum = available, each >= 0
        
        MOD = 10**9 + 7

        return comb(n + k - 1, 2 * k) % MOD
         