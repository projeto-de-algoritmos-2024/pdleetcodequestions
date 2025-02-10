from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)  # Memoization para evitar recomputação
        def dp(i: int, j: int) -> bool:
            # Caso base: ambos os índices chegaram ao fim
            if j == len(p):
                return i == len(s)
            
            # Verifica se há um caractere correspondente ou um ponto '.'
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # Se houver um '*', podemos ignorar ou usar o caractere anterior
            if j + 1 < len(p) and p[j + 1] == '*':
                return dp(i, j + 2) or (match and dp(i + 1, j))
            
            # Caso normal: avança um caractere se houver correspondência
            return match and dp(i + 1, j + 1)
        
        return dp(0, 0)
