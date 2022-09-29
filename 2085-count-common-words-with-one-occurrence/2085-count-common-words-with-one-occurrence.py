from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        
        counts1 = Counter(words1)
        counts2 = Counter(words2)
        res = 0
        
        for key1,val1 in counts1.items():
            
            for key2,val2 in counts2.items():
            
                if val1 == 1 and val2 == 1 and key1 == key2:
                    
                    res+=1
                    
        return res
        
                    
                    
                    
                    
                
                
        
        
        