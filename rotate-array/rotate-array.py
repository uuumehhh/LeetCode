class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        temps = [0] * len(nums)
        
        for i, n in enumerate(nums):
            temps[(i+k)%len(nums)] = n        
        
        for i, n in enumerate(temps):
            nums[i] = n