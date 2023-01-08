from tkinter import *
root= Tk()
e1=Entry(width=24)
e1.grid(row=0,column=0,columnspan=4)

b1=Button(root,text='1',border=1,width=3,height=1)
b1.grid(row=3,column=0)
b2=Button(root,text='2',border=1,width=3,height=1)
b2.grid(row=3,column=1)
b3=Button(root,text='3',border=1,width=3,height=1)
b3.grid(row=3,column=2)

b4=Button(root,text='4',border=1,width=3,height=1)
b4.grid(row=2,column=0)
b5=Button(root,text='5',border=1,width=3,height=1)
b5.grid(row=2,column=1)
b6=Button(root,text='6',border=1,width=3,height=1)
b6.grid(row=2,column=2)

b7=Button(root,text='7',border=1,width=3,height=1)
b7.grid(row=1,column=0)
b8=Button(root,text='8',border=1,width=3,height=1)
b8.grid(row=1,column=1)
b9=Button(root,text='9',border=1,width=3,height=1)
b9.grid(row=1,column=2)

b9=Button(root,text='0',border=1,width=3,height=1)
b9.grid(row=4,column=1)

b_add=Button(root,text='+',border=1,width=3,height=1)
b_add.grid(row=4,column=0)
b_eq=Button(root,text='=',border=1,width=3,height=1)
b_eq.grid(row=4,column=2)
b_clr=Button(root,text='clear',border=2)
b_clr.grid(row=4,column=1)

root.mainloop()
