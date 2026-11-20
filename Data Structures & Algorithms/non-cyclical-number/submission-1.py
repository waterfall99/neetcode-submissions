class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        current_n = n
        while current_n not in seen:
            if current_n == 1:
                return True
            elif current_n not in seen:
                seen.add(current_n)
            current_sum = 0
            for string in str(current_n):
                current_sum += int(string) ** 2
            current_n = current_sum
        return False     
    
         
