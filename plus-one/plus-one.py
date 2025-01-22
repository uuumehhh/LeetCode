class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        result = []
        add = 1
        
        for i in reversed(digits):
            if i + add < 10:
                result.insert(0, i+add)
                add = 0
            else:
                result.insert(0, 0)
                add = 1

        if add == 1:
            result.insert(0, add)

        return result