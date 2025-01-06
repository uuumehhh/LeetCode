class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        N1 = nums1[0:m]
        N2 = nums2[0:n]
        
        for i in range(len(N2)):
            N1.append(N2[i])
            
        num1 = sorted(N1)
        
        for i in range(len(num1)):
            nums1[i] = num1[i]