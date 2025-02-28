class Solution(object):
    def minSubArrayLen(self, target, nums):

        left, right, current_sum, min_len = 0, 0, 0, float('inf')

        while right < len(nums):
            current_sum += nums[right]
            right += 1

            while current_sum >= target:
                min_len = min(min_len, right - left)
                current_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len