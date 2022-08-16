try:
    i=int(input("enter a number"))
    c=1/i
except Exception as e:
    print(e)
    exit()
else:
    print("we are successful")
    


y=[12,13]
x=[1,2]
print(x.append(y))





if __name__=="__main__":
    while(True):
        print("enter q to exit" )
        a= input("enter any number:")
        if (a=='q'):
            break;
        try:
            a=int(a)
            if(a>6):
                print("number is greater than 6")
        except Exception as e:
            print("your input produce an error:" )
            print(e)
    

        
        


        
        
        
    
