"""
def main():
    number=get_number()
    aman(number)
    

def get_number():
    while True:
        n=int(input("what is the value of x ?") )
        if n>0:
            return n

def aman(n):
    for _ in range(n):
        print("aman")      

main()

#lists
students=["hermonie","harry potter","ron"]
print(students)
print(students[0])
print(students[1])
print(students[2])

for student in students:
    print(student)

for i in range(len(students)):
   # print(students[i])
   # print(i,students[i])
    print(i+1,students[i])
   #print([i]) 

students=["hermione","harry potter","ron","draco"]
houses=["gryfindor","gryfindor","gryfindor","slytherine"]
print(students[0],houses[0])
print(students[1],houses[1])
print(students[2],houses[2])
print(students[3],houses[3])

students={"hermione":"gryfingor","harry potter":"gryfingor","ron":"gryfingor","draco":"slytherine"}
print(students["hermione"])
print(students["ron"])
print(students["harry potter"])
print(students["draco"])

for student in students:
    print(student,students[student])


students=[
    {"name":"hermione","house":"gryfindor","patronous":"otter"},
{"name":"harry potter","house":"gryfindor","patronous":"sch"},
{"name":"ron","house":"gryfindor","patronous":"jack rume"},
{"name":"draco","house":"slytherine","patronous":"none"}
]
 
for _ in students:
    print(_["name"],_["house"],_["patronous"],sep=",")


def main():
    x=int(input("what is the value of column?"))
    print_column(x)

def print_column(height):
    for i in range(height):
        print("hello")
        print("#")


def print_column(height):
    print("hello")
    print("#\n" *height,end="")     

main()


def main():

    x=int(input("what is the value of rows?"))
    print_rows(x)

def print_rows(width):
    for i in range(width):
        print("?" *(width+i))

main()

def main():
    print_square(5)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            print("#",end="")
        print()
            
            
main()            

for i  in range(1,6):
    for j in range(1,i+1):
        print(i, end="")
    print("\n")

x,y,z=7,10,5
if x+y>z and y+z>x and x+z>y:
    print("triangle is valid")
else:
    print("triangle is not valid")
    


for num in range(1,23):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
                print(num)

num=9
for i in range(2,num):
    if num%i==0:
        print("not a prime no.")
        break
else:
    print("prime no.")


num=[2,3,4,5,5,6]

for i in range(len(num)):
    print(num[i],i)

num=9
for i in range(2,num):
    print(num)

ch=input("enter a character?")
if ch>='a' and ch<="z":
    print("the letter is lowercase")
elif ch>='A' and ch<="Z":
    print("the letter is uppercase")
else:
    print("the letter is numeric")
    
x=int(input("enter the number "))
sum=0
for i in range(x):
    sum=sum+i

print(sum)    
    
x=int(input("enter the number "))
sum=0
for i in range(11):
    if i%2==0:
        sum=sum+i
print(sum)

x=int(input("enter the number "))
i=2
sum=0
while(i<=x):
    sum=sum+i
    i=i+2


print(sum)

f=int(input("enter the fahrenheit"))
c=5/9*(f-32)
d=c
print(d)

#***
#***
#***
x=int(input("enter the value?"))
for i in range(x):
    for j in range(x):
        print("*",end="")
    print("\n")


#111
#222
#333
x=int(input("enter the value?"))
for i in range(x):
    for j in range(x):
        print(i+1,end="")
    print("\n")    
    
    
#123
#123
#123
x=int(input("enter the value?"))
for i in range(x):
    for j in range(x):
        print(j+1,end="")
    print("\n")    

#321
#321
#321
x=int(input("enter the no."))
for i in range(x):
    for j in range(x):
        print(x-j+1, end="")
    print("\n")    

    
#123
#456
#789
x=int(input("enter the no."))
count=1
for i in range(x):
    for j in range(x):
        print(count, end=" ")
        count+=1
    print("\n")    
    
    
#*
#**
#***
x=int(input("enter the no."))
for i in range(x):
    for j in range(i):
        print("*", end=" ")
        
    print("\n")    
    
#1
#12
#123
x=int(input("enter the no."))
for i in range(x):
    for j in range(i):
        print(j+1, end=" ")
        
    print("\n")    

    
#1
#22
#333

x=int(input("enter the no."))
for i in range(x):
    for j in range(i):
        print(i, end=" ")
        
    print("\n")


#1
#21
#321
x=int(input("enter the no."))
for i in range(x):
    count=i
    for j in range(i):
        print(count, end=" ")
        count-=1
    print("\n")

#1
#23
#456
x=int(input("enter the no."))
count=1
for i in range(x):
    
    for j in range(i):
        print(count, end=" ")
        count+=1
    print("\n")
    
    
#1
#23
#345
x=int(input("enter the no."))
for i in range(x):
    count=i
    for j in range(i):
        print(count, end=" ")
        count+=1
    print("\n")
   
    
#AAA
#BBB
#CCC
#ord function is used for finding the ASCII value of the alphabet's
#chr funtion is ued for converting int --> string
x=int(input("enter the no."))
k=ord("A")
print(k)
for i in range(x):
    #str=k+i-1
    for j in range(x):
        print(chr(str),end=" ")
    print("\n")


#ABC
#DEF
#GHI
x=int(input("enter the no."))
k=ord("A")
print(k)
for i in range(x):
    for j in range(x):

        print(chr(k),end=" ")
        k=k+1
    print("\n")


#A
#BC
#CDE
#DEFF
x=int(input("enter the no."))
k=ord("A")
for i in range(x):
    for j in range(i):
      str=k+i+j-2
      print(chr(str),end=" ")
    
    print("\n")


#    *
#   **
#  ***
# ****
x=int(input("enter the no. of rows?"))
for i in range(x+1):
    for j in range(x+1):
        if j<=x-i:
        print(" ",end=" ")
        else:
            print("*",end=" ")

    
    print("")

    
# ****
#  ***
#   **
#    *
x=int(input("enter the no. of rows?"))
for i in range(x):
    for j in range(x):
        if j<=i-1:
         print(" ",end=" ")
        else:
            print("*",end=" ")

    
    print("")
    

# ****
# ***
# **
# *
x=int(input("enter the no. of rows?"))
for i in range(x):
    for j in range(x-i):
         print("*",end=" ")
         
    
    
    print("")

# 1111
#  222
#   33
#    4
x=int(input("enter the no. of rows?"))
for i in range(1,x+1):
    for j in range(1,x+1):
        if j<=i-1:
         print(" ",end=" ")
        else:
            print(i,end=" ")

    print("")


# 1234
#  234
#   34
#    4
x=int(input("enter the no. of rows?"))
for i in range(1,x+1):
    for j in range(1,x+1):
        if j<=i-1:
         print(" ",end=" ")
        else:
            print(j,end=" ")

    print("")


#    1
#   22
#  333
# 4444
x=int(input("enter the no. of rows?"))
for i in range(1,x+1):
    for j in range(1,x+1):
        if j<=x-i:
         print(" ",end=" ")
        else:
            print(i,end=" ")

    print("")


#    1
#   23
#  456
# 78910
x=int(input("enter the no. of rows?"))
count=1
for i in range(1,x+1):
    for j in range(1,x+1):
        if j<=x-i:
         print(" ",end=" ")
        else:
            print(count,end=" ")
            count+=1
    print("")
    
    #    *
    #   * *
    #  * * *
    # * * * *
x=int(input("enter the no. of rows?"))
for i in range(x):
    for j in range(i,x):
         print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")    
    
    print("")

#pascal's left traingle
    #*
    #* *
    #* * *
    #* *
    #*
    
x=int(input("enter the no. of rows?"))
for i in range(x-1):
    for j in range(i+1):
        print("*",end=" ")
    print("")    
    
for i in range(x):
    for j in range(i,x):
         print("*",end=" ")
 
    print("")


#1
#21
#321
x=int(input("enter the no."))
for i in range(x+1):
    count=i
    for j in range(i):
        print(count, end=" ")
        count-=1
    print("\n")



#1
#12
#123

x=int(input("enter the no."))
for i in range(x):
    for j in range(i):
        print(j+1 ,end=" ")
        
    print("\n")


lower_range=int(input("Enter the lower range ?"))
upper_range=int(input("Enter the upper range ?"))
for num in range(lower_range,upper_range):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
                print(num,end="  ")




#print the sum of the sum of the no.
x=int(input("enter the no."))
sum=0
for i in range(x):
    first=x%10
    sum=sum+first
    x=x//10
print(sum)

#dabbang pattern
#1 2 3 4 5 * * 1 2 3 4 5 
#1 2 3 4 * * * * 1 2 3 4
#1 2 3 * * * * * * 1 2 3
#1 2 * * * * * * * * 1 2
#1 * * * * * * * * * * 1

x=int(input("enter the no. of rows?"))
p=x
for i in range(x):
    
    for j in range(x-i):
        print(j+1,end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(x-i):
     
        print(j+1,end=" ")
        
        
    print("")    

#print the bitwise opertor &,|,^,~
a=int(input("enter the first no.?"))
b=int(input("enter the second no.?"))
print("a&b",a&b)
print("a|b",a|b)
print("a^b",a^b)
print("~a",~a)
print("a<<b",a<<b)
print("a>>b",a>>+b)

#print fibonacci series 
x=int(input("enter the no.?"))
first=0
second=1
print(first,second,end=" ")
for i in range(x-2):
    next_no=first+second
    print(next_no,end=" ")
    first=second
    second=next_no

#find the greater from the 3 no.s
x=int(input("enter the first no.?"))
y=int(input("enter the second no.?"))
z=int(input("enter the third no.?"))

if x>y and x>z:
    print("x is greater",x)
elif y>z and y>x:
    print("y is greater",y)
else:
    print("z is the greater",z)    
 

    #find the even length of string 
s=input("enter your name?")
v=s.split(" ")
for word in v:
    if (len(word)%2==0):
        print(word,len(word))
        
   #reverse a integer or find whether the no. is palindrome or not
x=int(input("Enter the no.?")) 
reverse=0 
#we store the value of x in i because after the execution of the loop there will value 
#stored in the var x is 0
i=x
while(x!=0):
    remainder=x%10
    reverse=reverse*10+remainder
    x=x//10

if i==reverse:
    print("palindrome")

    
else:
    print("not a palindrome")    

print(reverse)

        
 
#8program to reverse words of string
x=int(input("Enter the first no."))
y=int(input("Enter the second no."))
z=int(input("Enter the third no."))

if x>y and x>z:
    print("x is greater",x)
elif y>x and y>z:
    print("y is greater",y)
else:
    print("z is greater",z)

#convert fahrenheit to celcius or vice versa
f=float(input("Enter the Temperature Fahrenheit:"))
c=5/9*(f-32)
d=c
print(d)

c=float(input("Enter the Temperature in Celcius:"))
f=c*9/5+32
e=f
print(e) 

#26find the even length of string 
s=input("enter your name?")
v=s.split(" ")
for word in v:
    if (len(word)%2==0):
        print(word,len(word))

#25program to find the sub string in a string
x=input("Enter the string:")
y=input("Enter the substring:")

if y in x:
    print("substring is present.")  
else: 
    print("substring is not present")    

#program to reverse the string
x=input("Enter the string:")
x=x.split()
x=list(reversed(x))
x=(" ".join(x))
print(x)


#CONVERSION FROM DECIMAL TO BINARY
x=int(input("Enter the decimal no.?"))
answer=0
i=0
while(x!=0):
    bit=x&1
   # answer=(bit*pow(10,i))+answer #this is for printing the no. in reverse flow
    answer=answer*10+bit #this is for printing the no. in same flow
    x=x>>1
    i=i+1

print(answer)

#conversion from binary to decimal (in this we have to work on the digit on the on the bits)
x=int(input("Enter the binary no.?"))
answer=0
i=0
while x!=0:
   # bit=x&1
    digit=x%10
    if digit==1:
        answer=answer+pow(2,i)
    x=x//10  
    i+=1   

print(answer)

#conversion from decimal to binary  (negative number)

x=int(input("Enter the no.?"))
answer=0
i=0
#Taking as a not operator we take 1's complement 
#& by adding 1 in 1's complement we take 2's complement
y=~x+1
while y!=0:
    bit=y&1
    answer=bit*pow(10,i)+answer
    y=y>>1
    i=+1

print(answer)
#print true if the input no. is in the pow of 2
x=int(input("Enter the no.?"))
for i in range(0,30):
    ans=pow(2,i)
    if ans==x:
        print("true")
        break

print("")

#27program to swap all dot with commas in the string
s=input("Enter the string:")
s=s.replace(',','temp') 
s=s.replace('.',',')
s=s.replace('temp','.')
print(s)

#28program a given string "F.R.I.E.N.D.S",change the strings to "friends"
x=input("Enter the string:")
x=x.lower()
x=x.replace(".","")
print(x)

#29WAP to extract digit string from a given string
x=input("Enter the string:")
for i in x:
    if i.isdigit():
        print(i,end=" ")
         


#31WAP to delete all the consonents from the string
x=input("Enter the string:") 

vowels="aeiouAEIOU"
for i in x:
    if i not in vowels:
      x=x.replace(i," ")    
print(x)

#30 WAP to insert in a list before an element
x=int(input("Length of List:"))
list=[]
for i in range(x):
    print("Enter the elements of List:",i+1)
    element=int(input())
    list.append(element)
    
y=int(input("Enter the Element U Insert:"))
z=int(input("Insert before Element ?: "))
index=list.index(z)
list.insert(index,y)
print(list)

#3Write a program to create, concatenate and print a string &
# accessing substring from a given string!
print("---------------Menu:----------------------")
while True:
 print("Press 1:Enter the string")
 print("Press 2:Concatenate the string")
 print("Press 3:Enter the substring:")
 print("Press 0:For Exit ")
 
 choice=int(input("Enter the Choice:"))
 if choice==1:
    s1=input("Enter the string:")
    print(s1)
 elif choice==2:
    #s1=input(("Enter the String 1:"))
    s2=input(("Enter the String 2:"))
    s3=s1+s2
    print(s3)
    
 elif choice==3:
    sub=input("Enter the substring U want to access:")
    if sub in s3:
        print("founded",sub)
    else:
        print("not founded")
 elif choice==0:
     break
    
print("Execution of the Program is Finished !")

#5Write a program to create, append, and remove lists in python
print("---------------Menu:----------------------")
while True:
 print("Press 1:Create List:")
 print("Press 2:Append the List:")
 print("Press 3:Remove the Elements List:")
 print("Press 4:Remove the List:")
 print("Press 0:For Exit ")
 
 choice=int(input("Enter the Choice:"))
 if choice==1:
     x=int(input("Length of List:"))
     list=[]
 elif choice==2:
     for i in range(x):
      print("Enter the elements of List:",i+1)
      element=int(input())
      list.append(element)

 elif choice==3:
     y=int(input("Enter Element U Remove:")) 
     list.remove(y)
 
 elif choice==4:
     list.clear()
 print(list)    
 if choice==0:
     break
print("Execution Program Is Done !")

#2Write a program to perform different Arithmetic Operations on numbers!
print("---------------Menu:----------------------")
while True:
 print("Press '+':Addition:")
 print("Press '-':Subtraction:")
 print("Press '*':Multiplication:")
 print("Press '/':Division:")
 print("Press '%':Modulus:")
 print("Press '^':Exponentiation:")
 print("Press '//':Floor Division:")
 print("Press 0:Exit:")
 
 print("---------------------Enter The Symbols:----------------------------------")
 #choice=int(input("Enter the choice:"))
 choice=input("Choice:")
 
 if choice=='+':
     first_no=int(input("Enter First No:"))
     second_no=int(input("Enter Second No:"))
     print("------------------RESULT:",first_no+second_no)
 elif choice=='-':
     print("------------------RESULT:",first_no-second_no)
 elif choice=='*':
     print("------------------RESULT:",first_no*second_no)
 elif choice=='/':
     print("------------------RESULT:",first_no/second_no)
 elif choice=='%':
     print("------------------RESULT:",first_no%second_no)
 elif choice=='^':
     print("------------------RESULT:",first_no**second_no)
 elif choice=='//':
     print("------------------RESULT:",first_no//second_no)
 elif choice=='0':
     break
print("The Execution Program Is Done!")

#32WAP to take input as a full name Adarsh Raj Pandey and display 
#A.R.Pandey
x=input("First Name:")
y=input("Middle Name:")
z=input("Last Name:")
x=x[0:1]
y=y[0:1]
z=z[::]
print(x,y,z,sep=".")

#WAP input of “Cse Python” will result in “cSE pYTHON” as the output 
def invert(line): 
 line=line.swapcase()
 return line

x=input("String:")
print("Result:",invert(x))


#WAP findchar(string,char)
#def findchar(string,char):
def findchar(string,char):
   for i in range(len(string)):
     if string[i]==char:
       return i
   return -1
        
s=input("String:")   
c=input("Char:")
print(findchar(s,c)
    
#29WAP to extract digit string from a given string
x=input("String:")
y="123456789"
for i in x:
    if i not in y:
        x=x.replace(i," ")    
print("Extract digits are:",x)
#x=re.findall(y,x)
#print(" ".join(x))
        
#30 WAP to insert in a list before an element
x=int(input("Length of List:"))
list=[]
for i in range(x):
    print("Enter the elements of List:",i+1)
    element=int(input())
    list.append(element)
    
y=int(input("Enter the Element U Insert:"))
z=int(input("Insert before Element ?: "))
index=list.index(z)
list.insert(index,y)
print(list)

#31WAP to delete all the consonents from the string
x=input("Enter the string:") 

vowels="aeiouAEIOU"
for i in x:
    if i not in vowels:
      x=x.replace(i," ")    
print(x)

#32WAP to take input as a full name Adarsh Raj Pandey and display 
#A.R.Pandey
x=input("First Name:")
y=input("Middle Name:")
z=input("Last Name:")
x=x[0:1]
y=y[0:1]
z=z[::]
print(x,y,z,sep=".")

#2Write a program to perform different Arithmetic Operations on numbers!
print("---------------Menu:----------------------")
while True:
 print("Press '+':Addition:")
 print("Press '-':Subtraction:")
 print("Press '*':Multiplication:")
 print("Press '/':Division:")   
 print("Press '%':Modulus:")
 print("Press '^':Exponentiation:")
 print("Press '//':Floor Division:")
 print("Press 0:Exit:")
 
 print("---------------------Enter The Symbols:----------------------------------")
 #choice=int(input("Enter the choice:"))
 choice=input("Choice:")
 
 if choice=='+':
     first_no=int(input("Enter First No:"))
     second_no=int(input("Enter Second No:"))
     print("------------------RESULT:",first_no+second_no)
 elif choice=='-':
     print("------------------RESULT:",first_no-second_no)
 elif choice=='*':
     print("------------------RESULT:",first_no*second_no)
 elif choice=='/':
     print("------------------RESULT:",first_no/second_no)
 elif choice=='%':
     print("------------------RESULT:",first_no%second_no)
 elif choice=='^':
     print("------------------RESULT:",first_no**second_no)
 elif choice=='//':
     print("------------------RESULT:",first_no//second_no)
 elif choice=='0':
     break
print("The Execution Program Is Done!")

#3Write a program to create, concatenate and print a string &
# accessing substring from a given string!
print("---------------Menu:----------------------")
while True:
 print("Press 1:Enter the string")
 print("Press 2:Concatenate the string")
 print("Press 3:Enter the substring:")
 print("Press 0:For Exit ")
 
 choice=int(input("Enter the Choice:"))
 if choice==1:
    s1=input("Enter the string:")
    print(s1)
 elif choice==2:
    #s1=input(("Enter the String 1:"))
    s2=input(("Enter the String 2:"))
    s3=s1+s2
    print(s3)
    
 elif choice==3:
    sub=input("Enter the substring U want to access:")
    if sub in s3:
        print("founded",sub)
    else:
        print("not founded")
 elif choice==0:
     break
    
print("Execution of the Program is Finished !")

#5Write a program to create, append, and remove lists in python
print("---------------Menu:----------------------")
while True:
 print("Press 1:Create List:")
 print("Press 2:Append the List:")
 print("Press 3:Remove the Elements List:")
 print("Press 4:Remove the List:")
 print("Press 0:For Exit ")
 
 choice=int(input("Enter the Choice:"))
 if choice==1:
     x=int(input("Length of List:"))
     list=[]
 elif choice==2:
     for i in range(x):
      print("Enter the elements of List:",i+1)
      element=int(input())
      list.append(element)

 elif choice==3:
     y=int(input("Enter Element U Remove:")) 
     list.remove(y)
 
 elif choice==4:
     list.clear()
 print(list)    
 if choice==0:
     break
print("Execution Program Is Done !")
 
 #WAP to demonstrate the use of Tuples
list=[]
x=int(input("Length Of Tuple:")) 
for i in range(x):
 
 element=(input("Element Of Tuple:"))
 list.append(element) 
 
tuple =tuple(list) 
print(tuple) 

 #Assignment02:WAP input of “Cse Python” will result in “cSE pYTHON” as the output 
def invert(line): 
 line=line.swapcase()
 return line

x=input("String:")
print("Result:",invert(x))

 #Assignment03(a)WAP to find a char in the string and return its index
def findchar(string,char):
   for i in range(len(string)):
     if string[i]==char:
       return i
   return -1
        
s=input("String:")   
c=input("Char:")
print("Index:",findchar(s,c))
      
 #Assignment03(b)WAP to find a chr in original string and when it founded replace it with newchar
def subchr(string,origchar,newchar):
    for i in range(len(string)):
      if string[i]==original:
        print(i,"founded")
        string=string.replace(original,newchar)
        return string
            
s=input("String:")   
original=input("Char:")
newchar=input("NewChar:")
print("Modified Str:",subchr(s,original,newchar))
  
#Assignment=4(a)W.A.P. to create a dictionary and  display both the keys and values sorted 
# in alphabetical order by the key
students={"Name":"Hermoine","House":"Gryfindor","Patronus":"Stag"}
y=sorted(students.items())
print(y)

 #Assignment=5W.A.P. to create a dictionary and  display keys as values & vice versa
x=int(input("Enter The No."))
students={}
for i in range(x):
    name=input("Enter Your name:")
    roll_no=int(input("Enter the roll_no:"))
    students[name]=roll_no
print(students)
swap = {roll_no:name for name,roll_no in students.items()}
print(swap)

#Assignement=6Implement a function called myPop(), which is similar to the list pop() method.
# Take a list as input, remove the last object from the list and return it.
def my_pop(list):
    list[:] = list[:-1]
    return list
list=[]
x=int(input("Length of List:"))
for i in range(x):
    print("List Elements:")
    element=int(input())
    list.append(element)
print(list)
choice=int(input("Choice:"))
for i in range(0,choice):
    x=my_pop(list)
print(x)

print("---------------Menu:----------------------")
while True:
 print("Press 1:Convert Celsius--->Fahrenheit:")
 print("Press 2:Convert Fahrenheit--->Celsius:")
 
 choice=int(input("Enter the Choice:"))
 if choice==1:
     c=float(input("Enter the Temperature in Celcius:"))
     f=c*9/5+32
     e=f
     print(e) 
 elif choice==2:
    f=float(input("Enter the Temperature Fahrenheit:"))
    c=5/9*(f-32)
    d=c
    print(d)
 else:
     print("",end="")
 y=True
 a=input("Do U Want to contiue Press 'y': ")
 if a!='y':
  break

 #WAP to demonstrate the use of Tuples
print("---------------Menu:----------------------")
while True:
 print("Press 1:Create List\Append the List:")
 print("Press 2:Remove the Elements List:")
 print("Press 3:Remove the List:")
 print("Press 0:For Exit ")
 
 choice=int(input("Enter the Choice:"))
 if choice==1:
    list=[]
    x=int(input("Length Of Tuple:")) 
    for i in range(x):
      element=(input("Element Of Tuple:"))
      list.append(element) 
    tuple =tuple(list)  
 elif choice==2:
    y=int(input("Enter Element U Remove:")) 
    list=list.pop(y)
    tuple=tuple(list)
 print(tuple)
 
#wap to find which is leap or which is not
x=int(input("Enter the Year:"))
#if(x%4==0 and x%100!=0) or (x%100==0):
if x%4==0 or x%100==0:
    print(x,"is leap year")
else:
    print(x,"Not a leap year.")
    
 #33(allias)wap to find the occurence of each alphabet in the string use of dict is prohibited
x="this is the string with the upper and lower case letters"
list=[]
for i in x:
    if i not in list:
        ele=list.append()
        z=x.count(i)
        print(i,":",z)
 
#33wap to find the occurence of each alphabet in the strings using dictionary!
x=input("String:")
dict={}
for i in x:
    dict[i]=dict.get(i,0)+1
for i,j in sorted( dict.items()):
        print(i,":",j)

#34Write a function scaler_mult(s,v) that takes a number 's' and a list 'v' and return the 
# scalar multiply of 'v' by 's'
def scaler_mult(s,v):
    l=[]
    for i in range(len(v)):
      j=s*list[i]
      l.append(j)
    return l
digit=int(input("Enter Number:"))
cap=int(input("Enter range of list:"))
list=[]
for i in range(cap):
      print("Enter the elements of List:",i+1)
      element=int(input())
      list.append(element)
print(scaler_mult(digit,list))

#35Given a tuple and a list as input,WAP to count the occurences
# of all items of the list in the tuples.
cap_L=int(input("Enter range of list:"))
list=[]
for i in range(cap_L):
    print("Enter the elements of list:",i+1)
    element=int(input())
    list.append(element)
print(list)
cap_T=int(input("Enter range of tuples:"))
l=[]
for i in range(cap_T):
    print("Enter the elements of list:",i+1)
    element=int(input())
    l.append(element)
tuple=tuple(l)
print(tuple)
for i in list:
    k=tuple.count(i)
    print(i,":",k)

#36 WAP Given a list of words in python the task is to remove the 
 # Nth occurence of the given words in the list
cap_L=int(input("Enter range of list:"))
list=[]
count=0
list1=[]
for i in range(cap_L):
    print("Enter the elements of list:",i+1)
    element=input()
    list.append(element)
print(list)
chr_del=input("what character U want to delete:")
occur=int(input("Enter the occurence:"))
for i in list:
    if i==chr_del:
       count+=1
       if count!=occur:
          list1.append(i)
    else:
     list1.append(i)      
print(list1)

#37 Given a string write a program to mirror the chr i.e change 'a' to 'z','b' to 'y' ......
x=input("Enter String:")
alphabets='abcdefghijklmnopqrstuvwxyz'
rev=alphabets[::-1]
dict=dict(zip(alphabets,rev))
result=""
for i in x:
    result=result+dict[i]
print(result)

#38WAP to merge the two dictionaries
dict1={1:'hello',2:'who',3:'are'}
dict2={4:'you',5:'I',6:'Am',7:'Aman'}
result=(dict1|dict2)
print(result)

#13wap to find whether the triangle is right triangle or not
x=int(input("First No:"))
y=int(input("Second No:"))
z=int(input("Third No:"))
x,y,z=pow(x,2),pow(y,2),pow(z,2)
if x==y+z and y==x-z and z==x-y:
    print("This is right angles triangle!")
else:
    print("It is not a right angled triangle!")

#01 WAP to print the type of all the data types used in the python
a,b,c,d,e=7,7.5,(2,3,),[2,3,4],{1:'Aman',2:'hello'}
print(type(a),type(b),type(c),type(d),type(e))

#04 the program to print thr format
import time
print(time.strftime("%a %b %d %H:%M:%S %Z %Y",time.localtime()))

#12wap to print the factorial of an number
def factorial(x):
    return x*(x-1)
x=int(input("Enter the value:"))
print("Factorial of",x,":",factorial(x))

#01 WAP to print the type of all the data types used in the python
a=7
print(type(a))
b=7.5
print(type(b))
c=(2,3)
print(type(c))
d=[2,3,4]
print(type(d))
e={1:'Aman',2:'hello'}
print(type(e))
bool=True
print(type(bool))
f=complex(2,5)
print(type(f))
"""
fact=1
top=100
n=int(input("Enter:"))
for i in range(n+1):
    fact=fact*2
    if (fact>top):
     break
print(fact//2)