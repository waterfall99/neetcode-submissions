class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        string_s_set = {}
        string_t_set = {}

        for char in s:
            if char in string_s_set:
                string_s_set[char] += 1
            else:
                string_s_set[char] = 1
        for char in t:
            if char in string_t_set:
                string_t_set[char] += 1
            else:
                string_t_set[char] = 1
        if string_s_set == string_t_set:
            return True
        return False
        
        
        
            