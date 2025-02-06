class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        prev_answer = self.getRow(rowIndex-1)
        answer = [] 
        answer.append(1)
        
        for i in range(rowIndex-1):
            answer.append(prev_answer[i] + prev_answer[i+1])
        answer.append(1)
        return answer