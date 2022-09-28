class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        
        answer = []
        for i in range(len(nums)):
            
            if i%10 == nums[i]:
                
                answer.append(i)
                
        if answer:
            
            return min(answer) 
        
        else:
            
            return -1
        