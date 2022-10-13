class Solution:
    def interpret(self, command: str) -> str:
        
        charArray = []
        
        for char in command:
            
            charArray.append(char)
        
        print(charArray)
        returnStr = ""
        
        for i in range(len(charArray)):
            
            if charArray[i] == "G":
                
                returnStr+="G"
                
                
            elif charArray[i] == "(" and charArray[i+1] == ")":
                
                returnStr+="o"
                
            elif charArray[i] == "(" and charArray[i+1] == "a":
                
                returnStr+="al"
                
            else:
                
                continue
                
        return returnStr
                
            
        
                
                
            
            