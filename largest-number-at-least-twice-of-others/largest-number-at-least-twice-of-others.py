class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        max_num = max(nums)
        check_num = max_num // 2
        
        check = [num for num in nums if check_num < num]
        
        if len(set(check)) > 1:
            return -1
        else:
            return nums.index(max_num)