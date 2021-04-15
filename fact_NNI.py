f=input("f:")
def factorial(f):
    if(f==0 or f==1):
        return 1
    else:
        f * factorial(f-1)
    
print("the factorial is:", f)