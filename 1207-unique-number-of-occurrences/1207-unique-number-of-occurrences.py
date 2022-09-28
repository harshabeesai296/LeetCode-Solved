from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        counts = Counter(arr)
        vals = []
                
        for key,val in counts.items():
            
            vals.append(val)
            
        
        if len(vals) == len(set(vals)):
            
            return True
        
        else:
            
            return False