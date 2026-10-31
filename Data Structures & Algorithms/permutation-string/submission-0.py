class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        start = 0
        end = len(s1) - 1
        s1_seen = {}
        s2_seen = {}
        for s1_char in s1:
            s1_seen[s1_char] = s1_seen.get(s1_char, 0) + 1
        for i in range(start, end + 1):
            s2_char = s2[i]
            s2_seen[s2_char] = s2_seen.get(s2_char, 0) + 1
        if s1_seen == s2_seen:
            return True
        while end < (len(s2) - 1):
            s2_seen[s2[start]] -= 1
            if s2_seen[s2[start]] == 0:
                del s2_seen[s2[start]]
            start += 1
            end += 1
            s2_seen[s2[end]] = s2_seen.get(s2[end], 0) + 1
            if s1_seen == s2_seen:
                return True
        return False

