class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        e = len(s) -1
        while s[e] == " ":
            e -=1
        start = e
        while start >= 0 and s[start] != " ":
            start -= 1
        
        return e - start
        