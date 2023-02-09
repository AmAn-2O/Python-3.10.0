unit=float(input("Enter the Units:"))
if unit<=100:
    print(unit*4.5)
elif unit >100 and unit<=200:
    print((100*4.5)+(unit-100)*6)
elif unit>200 and unit<=300:
    print((100*4.5)+(100*6)+(unit-200)*10)
elif unit>300 and unit<=400:
     print((100*4.5)+(100*6)+(100*10)+(unit-300)*20)

list=[1,2,3,4,5,6,7,8,9]
cube=[]
for i in list:
    if((i*i*i)%4==0):
        cube.append(i*i*i)
print(cube)