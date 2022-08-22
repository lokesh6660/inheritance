class student:
    
    def sum(self,a=0,b=0,c=0):
        s=a+b+c
        return s
class b(student):
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def show(self):
        ptint('hello')
s1=b(12,12)
print(s1.sum(12,12,13))
