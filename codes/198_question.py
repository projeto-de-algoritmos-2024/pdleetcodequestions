from functools import lru_cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(None)  # Memoization para evitar recomputação
        def dp(i: int) -> int:
            if i >= len(nums):
                return 0
            
            # Escolhemos roubar esta casa ou pular para a próxima
            return max(nums[i] + dp(i + 2), dp(i + 1))
        
        return dp(0)
