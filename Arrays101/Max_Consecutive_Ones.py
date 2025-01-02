# 0,1로 이루어진 배열 입력 / 연속된 1의 최대 개수 출력

count = 0
max_count = 0

num = list(map(int, input().split(',')))

for i in range(len(num)):
    if num[i] == 1:
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0

max_count = max(max_count, count)
print(max_count)

# At LeetCode
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        max_count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0
        
        return max(max_count, count)
