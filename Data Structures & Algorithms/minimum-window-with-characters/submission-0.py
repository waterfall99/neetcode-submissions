class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        have = 0
        start = 0
        seen_t = {}
        seen_window = {}
        
        for char in t:
            seen_t[char] = seen_t.get(char, 0) + 1
        
        need = len(seen_t)
        res_len = float('inf')
        res = [-1, -1]

        for end in range(len(s)): 
            seen_window[s[end]] = seen_window.get(s[end], 0) + 1
            if seen_window[s[end]] == seen_t.get(s[end], 0):
                have += 1
            while have == need:
                if end - start + 1 < res_len:
                    res_len = end - start + 1
                    res = [start, end]
                seen_window[s[start]] -= 1
                if seen_window[s[start]] < seen_t.get(s[start], 0):
                    have -= 1
                start += 1
        if res_len != float('inf'):
            return s[res[0] : res[1] + 1]
        return ""
            








