class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        
        temp = []
        
        for i in range(len(arr)):
            if arr[i] == 0:
                temp.append(arr[i])
            temp.append(arr[i])
        
        answer = temp[0:len(arr)]
        
        for i in range(len(arr)):
            arr[i] = answer[i]