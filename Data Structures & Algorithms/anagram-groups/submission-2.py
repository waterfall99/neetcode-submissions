class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_storage = {}
        for i in strs:
            my_key = tuple(sorted(i))
            if my_key in anagram_storage:
                    anagram_storage[my_key].append(i)
            else:
                anagram_storage[my_key] = [i]
        return list(value for key, value in anagram_storage.items())        
        
