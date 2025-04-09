class Poly:
    def __init__(self,*values):
        self.values=list(values)
        
    def __add__(self,other):
        a=self.values[:]
        b=other.values[:]
        if  len(a)<len(b):
            a=[0]*(len(b)-len(a))+a
        elif len(a)>len(b):
            b=[0]*(len(a)-len(b))+b
            
        result=[]
        for i in range(len(a)):
            result.append(a[i]+b[i])  

        return Poly(*result)
    def __str__(self):
        return str(tuple(self.values))
        
        
a = Poly(1,2,3)  
b = Poly(1,0,1,1,2,3)
c = a+b 
print(c)
            
    
            
          
            