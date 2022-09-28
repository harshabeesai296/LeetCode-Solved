class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squareNums = []
        
        for num in nums:
            
            squareNums.append(num * num)
            
        return sorted(squareNums)
        