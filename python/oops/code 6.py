# passing constructor to a paramter
class demo:
    x=0
    y=0
    def __init__(self,x,y):
       self.x=x
       self.y=y
    def check(self,other):
        if(self.x==other.x and self.y==other.y):
            return True
        else:
            return False

ob1=demo(50,10)
ob2=demo(50,10)
print(ob1.check(ob2))
