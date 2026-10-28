class Solution:
    def isPalindrome(self, s: str) -> bool:
        actual = "".join(char for char in s if char.isalpha() or char.isdigit()).lower()
        if actual == actual[::-1]:
            return True
        else:
            return False