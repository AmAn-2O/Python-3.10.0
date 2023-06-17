""" b=1
while b!=5:
    inpt=int(input('''Enter your choice :
    Enter 1 to create a dictionary.
    Enter 2 to display key value pairs. 
    Enter 3 to display keys and values saperately.
    Enter 4 to removing elements.
    Enter 5 to exit.'''))
    if inpt==1:
        key=[]
        value=[]
        n=int(input('Enter no of Elements : '))
        for i in range(n):
            ele=input('Enter key ')
            key.append(ele)
        key1=tuple(key)
        for i in range(n):
            ele=input('Enter value ')
            value.append(ele)
        value1=tuple(value)
        dict1=dict(zip(key1,value1))
        print('you created a dictionary successfully : \n The dictionary is : \n',dict1)
    elif inpt==2:
        it=dict1.items()
        for i in it:
            print(i)
    elif inpt==3:
        k=dict1.keys()
        v=dict1.values()
        print('keys of the dictionary are :\n')
        for i in k:
            print(i) 
        print('values of the dictionary are :\n')
        for i in v:
            print(i)
    elif inpt==4:
        print(dict1.keys())
        r=input('Enter key of that element which you want to remove : ')
        p=dict1.pop(r)
        print(p,'is removed.')
    if inpt >=5:
        break
        b=b+1
    a=input("do you want to continue (y/n): ")
    if a!='y':
        break    """
""" b=1
while b!=5:
    inpt=int(input('''Enter your choice :
    Enter 1 to create a list.
    Enter 2 to append in a list. 
    Enter 3 to remove element from a list.
    Enter 4 to show list.
    Enter 5 to exit.'''))
    if inpt==1:
        li=[]
        n=int(input('Enter number of elements : '))
        for i in range(n):
            ele=int(input('Enter element '))
            li.append(ele)
        print('list created sucessfully')
    elif inpt==2:
        a=input('Enter element which you want to append : ')
        li.append(a)
        print('element appended sucessfully')  
    elif inpt==3:
        a=input('Enter element which you want to remove : ')
        li.remove(a)
        print('element removed sucessfully')
    elif inpt ==4:
         print("your list is : ",li)
    elif inpt >=5:
        break
        b=b+1
    a=input("do you want to continue (y/n): ")
    if a!='y':
        break
 """
""" class convert:
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90,'XC'),(50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')] 
    def roman(self,n):
        roman = ''
        while n> 0:
            for i, r in self.num_map:
                while n >= i:
                    roman += r
                    n -= i
        return roman
n=int(input("Number :"))
print("Roman Number is : ",convert().roman(n))
 """""" 
class py_pow:
   def pow(self,x,n):
    if n==0 or x==0 or x==1:
     return n;
    elif n>0:
        x=1
        for i in range(n):
            x=x*n
        return x            
x=int(input("Enter x value :"))
n=int(input("Enter n value :"))
print("pow(x,n) value is :",py_pow().pow(x,n)); """

""" class py_reverse:
   def revr(self, x):
       x=x.split()
       x.reverse()
       y=" ".join(x)
       return y
x=input("String:")
print("Reverse string:\n",py_reverse().revr(x)) """

""" def fun(n):
    try:
        if (n<0):
            raise ValueError
        else:
            print(n)
    except ValueError:
        print(" U entered the -ve value\n Pls Enter the positive value")       
a=int(input("Enter a:"))      
print(fun(a)) """

""" def sum(n,k):
    try:
        val=int(n)
        val1=float(k)
        if (n==val and k==val1):
            raise ValueError
        else:
            print(val+val1)
    except ValueError:
        print(" Pls Enter [num1==integer] value")
a=input("Enter num_1:")
b=input("Enter num_2:")
print(sum(a,b)) """

""" import re
Str =input("string:")
match=re.search('^From.+([0-4][0-9]:)$',Str)
print(match) """
