""" def fib(n):
 first=0
 second=1
 print(first,second,end=" ")
 for i in range(n-2):
    next_no=first+second
    print(next_no,end=" ")
    first=second
    second=next_no
 """
def leapyear (x):
 if x%4==0 or x%100==0:
    print(x,"is leap year")
 else:
    print(x,"Not a leap year.")
