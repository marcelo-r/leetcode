class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fb = []                                                                                      
        for num in range(1,n+1):
            div_3 = num % 3 == 0
            div_5 = num % 5 == 0                                                                     
            if div_3 and div_5:                                                                      
                fb.append("FizzBuzz")                                                                
            elif div_3:                                                                              
                fb.append("Fizz")                                                                    
            elif div_5:                                                                              
                fb.append("Buzz")                                                                    
            else:                                                                                    
                fb.append(str(num))                                                                  
        return fb 
