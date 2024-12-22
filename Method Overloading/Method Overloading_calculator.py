class calculator:
    def add(self,a,b=None,c=None):
        if b is None and c is None:
            return a*a
        elif c is None:
            return a+b
        else:
            return (a+b)*c
        
    
calc= calculator()
print(calc.add(9))
print(calc.add(9,8))
print(calc.add(6,8,5))
        

