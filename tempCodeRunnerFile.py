def fun(n):
    try:
        if (n<=0):
            raise ValueError
        else:
            print(n)
    except ValueError:
        print(" U entered the -ve value\n Pls Enter the positive value")       
a=int(input("Enter a:"))      
print(fun(a))
