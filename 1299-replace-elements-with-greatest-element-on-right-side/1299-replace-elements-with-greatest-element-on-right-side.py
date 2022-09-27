class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        newArr = arr
        
        if len(arr) == 1:
            
            return [-1]
        
        if len(arr) == 2:
            
            if arr[0] > arr[1]:
                
                return [-1]
            else:
                
                return arr[1]
            
        for i in range(len(arr)-1):
            
            newArr[i] = max(arr[i+1:])
        
        newArr[-1] = -1
        
        return newArr
        
            
            
        