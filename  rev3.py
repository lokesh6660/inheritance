
def count(lis):
    even=0
    odd=0
    for i in lis:
        if i%2==0:
            even+=1
        else:
            odd+=1
            
    return even, odd

lis=[12,13,14,15,16,17,18]
even,odd= count(lis)

print("even: () and odd: ()".format(even,odd))

from abc import ABC,abstractmethod



class computer(ABC):
    @abstractmethod    
    def process(self):
       pass


class laptop(computer):
    def process(self):
        print("it's running")

class programmer:
    def work(self):
        print("solveing bugs")

comp1=laptop()
#it create an object 
pog1=programmer()
pog1.work()
comp1.process()
