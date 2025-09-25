class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = ''.join(char.lower() for char in s if char.isalnum())
        phrase = clean_text
        return phrase[::-1] == phrase