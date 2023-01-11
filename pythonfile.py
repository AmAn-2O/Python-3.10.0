"""
file=str(input("File Name with extension:"))
with open(r"pythonfile1.txt", 'r') as file:
 length = len(file.readlines())
print('Lines:', length)

file=open("pythonfile1.txt","w")
file.write('1234567890')
file=open("pythonfile1.txt","r")

#WAP to find what percentage of char 'a' vowel in a text file
file=input("Enter The File_Name:")
file=open(file,"r")
file=file.read()
print(file)
vowel="aA"
word=len(file)
alphabet=""
for i in file:
    if i in vowel:
        alphabet=i+alphabet     
y=len(alphabet)
percent=((y/word)*100)
print("% of Vowel 'a' in File:",round(percent,2))

#39WAP that takes a text file as input and return the no. of word of a given text file
file=input("Enter The File_Name:")
file=open(file+".txt","r")
file=file.read()
file=file.split()
words=len(file)
print("Total Words File:",words)

#40 wap to print the no. of lines in the file
file=open("pythonfile1.txt","r")
file=file.read()
print(file)
file=open("pythonfile1.txt")
length=len(file.readlines())
print(length)

#41wap to count the occurance of each word in a given text file(using dict)
file=open("file3.txt","w")
file.write("the quick brown dog jumps over the lazy dog the hello quick over lazy the over the")
file=open("file3.txt","r")
file1=file.read()
file2=dict()
file3=file1.split()
for i in file3:
    if i in file2:
        file2[i]+=1
    else:
        file2[i]=1
print(file2)

#42WAP eliminating repeating lines from the files (create another file and store unique
# lines in that file)
file=open("file4.txt","r")
file1=open("file5.txt","w+")
unique_lines=set()
for i in file:
 if i not in unique_lines:
     file1.write(i)
     unique_lines.add(i)
file1=open("file5.txt","r")
for i in file1:
    print(i)
    
#43 wap to print the extracts the digits from the file &
# find the sum of that extract digits
file=open("pythonfile1.txt","r+")
file=file.read()
print(file)
sum=0
digit=0
for i in file:
    if i.isdigit():
        digit=digit*10+int(i)
    else:
        sum=sum+digit
        y=0
print("RESULT:",sum+digit)

# 44WAP given a integer value return a string with equivalent english text of each digit 
# 44=four-four
y=int(input("Enter digit:"))
dict={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
for i in range(y):
 x=y%10
 z=y//10
if y>0 and y<10:
 print(dict[y])
elif y>9:
    print(dict[z]+"-"+dict[x])
y=input("Enter digit:")
dict= {"0":"Zero","1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine"}
for i in y:
    print(dict[i],end="-")

#45wap to count the percentage of words start with vowel a in the file.txt
file=input("Enter The File_Name:")
file=open(file,"r")
file=file.read()
print(file)
count=0
file=file.split(" ")
print("Words Beg With Alphabet 'aA':")
for i in file:
    if i[0]=='a'and 'A':
        print(i.title())
        count=count+1
x=len(file)
percent=count/x*100
print("% oF Words Beg With Alphabet 'aA' in File:",round(percent,2))

#46Wap to print all seven letters that starts with th and ends with ly  
file=open("file.txt","w")
file.write("thalkly thhello who thklly are thyouly")
file=open("file.txt","r")
file1=file.read()
file1=file1.split()
for i in file1:
    if len(i)==7 and i[0:2]=="th" and i[-2:]=="ly":
        print(i)

#47wap to read from file and print all words that starts and ends with same three letters.
file=open("file.txt","w")
file.write("my name is amandeepama education and i am from rajasthanraj")
file=open("file.txt","r")
f1=file.read()
#file="my name is amandeepama education and i am from rajasthanraj"
f1=f1.split()
for i in f1:
    if len(i)>=6 and i[0:3]==i[-3:]:
        print(i)

#48Wap to read from the file and print the longest words that starts and ends with same letter
file=open("file3.txt","w")
file.write("helooolooleh mom dad  hohlohohohodsoh hiooooooih radar racecarra ")
file=open("file3.txt","r")
file1=file.read()
file1=file1.split()
longest_word=len(file1[0])
for i in file1:
    word_length=len(i)
    if i[0]==i[-1] and word_length>longest_word:
        print(i)

#49Wap to read from the file and print all the words 
# that contains 4 alphabetically consecutive letters
list = ['abbot', 'alone', 'abcefghid', 'strabcdt', 'abcdiam','education', 'python']
for w in list:
    for j in range(len(w)-1):
     if ord(w[j])+1==ord(w[j+1]) and ord(w[j+1])+1==ord(w[j+2]) and ord(w[j+2])+1==ord(w[j+3]):
            print(w) 

# 50)Write a function that uses the input dialog to prompt the user for a positive integer 
# and then checks the input to confirm that it meets the requirements. 
def fun(n):
    try:
        if (n<0):
            raise ValueError
        else:
            print(n)
    except ValueError:
        print(" U entered the -ve value\n Pls Enter the positive value")       
a=int(input("Enter a:"))      
print(fun(a))

# 51)Write a program that gets two command line arguments and checks that 
# the first  argument represents a valid int number and second argument represents 
#a float number  and display sum of those. Make useful feedback if they are not.
def sum(n,k):
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
print(sum(a,b))

#16WAP The content of the first file should be input and written to the second file
file1=input("Enter The File_Name:")
file2=input("Enter The File_Name:")
f1=open(file1,"r")
f2=open(file2,"w")
z=f1.readlines()
for i in range(0,len(z)):
    f2.write(z[i])
f2.close()
f3=open(f2,"r")
print(f3)

#17WAP in python find unique words or in sorted order
file=open("file.txt","w")
file.write("hello what are you doing hello are here")
file=open("file.txt","r")
f1=file.read()
res=set(f1.split(" "))
for i in sorted(res):
    print(i)

#WAP in python to extract digit from string and find sum of that digits
import re
s="hello34 who56 my49"
l=re.findall('\d',s)
sum=0
for i in l:
    sum=sum+int(i)
print(sum)
 
 #52)Write a Python program to find all words which are at least 4 characters long in a string.
import re
s="hello who are you this is cse 5th python class!"
match=re.findall(r'\b\w{4,}\b',s)
print(" ".join(match))   


#53)Write a Python program to remove everything from a string  except alphanumeric characters .
import re
s="hello\who45are#you78-?"
match=re.findall(r'\d*[A-Za-z]*',s)
print(" ".join(match))

#54Write a Python program to check a string containing decimal with a precision of at most 2.
# (e.g. 34.89(TRUE), 12.789(FALSE), 12(TRUE))
def decimal(deci):
    import re
    match=re.search(r'\A\d+(\.\d{,2})?\Z',deci)
    return bool(match)
x=input("Enter number:")
print(decimal(x))

 # 55)Create Regular Expression for following” 
# Match for stings  that start with From and  characters (if any)
#  followed by a two digit number between 00 and 50
import re
Str =input("string:")
match=re.search('^From.+([0-4][0-9]:)$',Str)
print(match)

 
#--------------------------Python Assignment 2----------------------------------------------
#01(a) Consider a strings s= “You have a class on 2020-12-20 at 11:30:20 hrs”.
#Write a regular expression to extract date and time from above string.
import re
s="You have a class on 2020-12-20 at 11:30:20 hrs"
match1=re.findall(r'\d{4}-\d{2}-\d{2}',s)
match=re.findall(r'\d{2}:\d{2}:\d{2}',s)
print("".join(match1),"".join(match))

#01(b)Write a Python program to remove everything from a string  
# except alphanumeric characters
import re
s="hello?who1234-\\|are234YOU}["
match=re.findall(r'\w',s)
print(" ".join(match))

#02(a)Write a Python program to find all words which are at least 4 characters long in a string.
# (Using "re" module)
import re
s="hello this is cse 5th class of python"
match=re.findall(r'\b\w{4,}',s)
print(" ".join(match))

#02(b)Match first name and last name of a person,with a restricted 
# first name (must start with uppercase; lowercase only for remaining letters, if any),
# the full name prepended by an optional title of “Mr.,” “Mrs.,” “Ms.,” or “M.,”
# and a flexible last name, allowing for multiple  dashes, lowercase and uppercase letters   
import re
s=input("Enter the name:")
match=re.search(r'\b(Mr\.|Mrs\|Ms\.|M\.)([A-Z].+)',s)
print(match)

#03Write a Python program to find all words starting with 'a' or 'e' in a given string.
# using 're' module
import re
s="aeroplane solo apple tub alice gym anger colin education dog"
match=re.findall(r'\b[ae]\w{,}',s)
print(" ".join(match))

#extra WAP that email enter by the user is valid or not
import re
s=input("Enter the email:")
match=re.search(r'^\w+@\w+\.(edu|com|org)$',s)
if match:
    print("valid")
else:
    print("invalid")



 #zero division error
try:
    a=int(input("Enter no. a:"))
    b=int(input("Enter no. b:"))
    print(a/b)
except:
    print("Can't divided by zero")
    print("pls enter the valid no.")
 
import re
s=input("String:")
match=re.search(r'([a-z]\w{,3}\d{,2})',s)
print(match) 

import re
s="color colour liecense liecence this is the color and colour"
match=re.findall(r"colo[ur]r*",s)
print(match)

try:
    a=int(input("Enter no. a:"))
    b=int(input("Enter no. b:"))
    print(a/b)
except:
    print("Can't divided by zero")
    print("Enter the denominator greater than zero!")
"""
#19 WTH of Class implement the pow(x,n) function
def pow(x,n):
    if n==0 or x==0 or x==1:
     return n;
    elif n>0:
        x=1
        for i in range(n):
            x=x*2
        return x
            
print(pow(2,5))

#20 WTH of Class reverse the string word by word
x=input("String:").split()
y=x[::-1]
print(" ".join())

#54Write a Python program to check a string containing decimal with a precision of at most 2.
# (e.g. 34.89(TRUE), 12.789(FALSE), 12(TRUE))
def decimal(deci):
    import re
    match=re.search(r'\A\d+(\.\d{,2})?\Z',deci)
    return bool(match)
x=input("Enter number:")
print(decimal(x))

 # 55)Create Regular Expression for following” 
# Match for stings  that start with From and  characters (if any)
#  followed by a two digit number between 00 and 50
import re
Str =input("string:")
match=re.search('^From.+([0-4][0-9]:)$',Str)
print(match)