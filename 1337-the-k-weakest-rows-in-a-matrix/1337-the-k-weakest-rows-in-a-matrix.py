class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        mapper = {}
        order = []
        
        for i,row in enumerate(mat):
            
            mapper[i] = sum(row)
        
        print(mapper)
        
        
        sortedMapper = {k: v for k, v in sorted(mapper.items(), key=lambda item: item[1])}
        
        print(sortedMapper)
        
        for key,value in sortedMapper.items():
            
            if k>0:
                
                order.append(key)
                k-=1
                
            else:
                
                break
                
        return order