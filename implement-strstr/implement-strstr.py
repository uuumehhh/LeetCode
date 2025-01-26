class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        m = len(needle)
        
        if len(needle) == 0:
                return 0
        
        for i in range(len(haystack)):
            
            if haystack[i] == needle[0] and haystack[i:i+m] == needle:
                return i
        
        else:
            return -1