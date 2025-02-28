class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        new_h = sorted(heights)
        match = 0
        
        for i in range(len(heights)):
            if heights[i] != new_h[i]:
                match += 1
                
        return match