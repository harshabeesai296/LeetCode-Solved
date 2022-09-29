class Solution:
    def minimumSum(self, num: int) -> int:
        
        intArray = []
        
        for integer in str(num):
            
            intArray.append(integer)
            
        intArray = sorted(intArray)   
        
        lastArray = []
        
        for i in range(0,len(intArray)-3):
            
            lastArray.append(intArray[i]+intArray[i+2])
            lastArray.append(intArray[i+1]+intArray[i+3])
                    
        lastuuu = []
        
        for ankels in lastArray:
            
            lastuuu.append(int(ankels))
            
        return sum(lastuuu)
            
            
            
        