def toptan():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n=n+1

value= toptan()
for i in value:
    print(i)
def toptan():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n=n+1

value= toptan()
for i in value:
    print(i)
        
x=int(input("enter the number:"))
class number():
    def sum(self,a=10,b=10):
        s=a+b
        return s
class new(number):
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def show(self):
        print("hello")

n1=new(20,20)
n1.show()
print(n1.sum())
