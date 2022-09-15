
import math

class vec:
    def __init__(self,x=0.0,y=0.0):
        self.x=x
        self.y=y
    
    def __add__(self,other):
        if isinstance(self,vec) and isinstance(other,vec):
            return(vec(self.x+other.x,self.y+other.y))
    def __sub__(self,other):
        return(self+(-other))
    def __neg__(self): 
        return(vec(-self.x,-self.y,))
    def __pos__(self):
        return(self)
    def __invert__(self):
        return(vec(~self.x,~self.y))
    def __mul__(self,other):
        if isinstance(other,int)or isinstance(other,float) and isinstance(self,vec):
            return(vec(self.x*other,self.y*other,))
        if isinstance(self,int)or isinstance(self,float) and isinstance(other,vec):
            return(vec(other.x*self,other.y*self))
    def __truediv__(self,other):
        if isinstance(other,int)or isinstance(other,float):
            return self*(1/other)
    def __str__(self):
        return str((self.x,self.y))

    def length(self)->float:
        """
        return the length of the vector
        """
        return(math.sqrt(self.x**2+self.y**2))
    def squareLength(self)->float:
        """
        return the squared length of the vector
        """
        return(self.x*self.x+self.y*self.y)
    
    
    
print(vec(1,3)/2)

