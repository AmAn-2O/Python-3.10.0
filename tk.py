from tkinter import *
root = Tk()
root.title("Simple Calculator")
e=Entry(root,width=50,borderwidt=5)
e.insert(1,"Enter Your Name:")
e.pack()
def myclick():
    hello="Hello! "+e.get()
    mylabel=Label(root,text=hello)
    mylabel.pack()
    
""" def myclick():
    mylabel=Label(root,text="Look ! I Clicked a Button")
    mylabel.pack() """
""" mylabel=Label(root,text="May I Come In!").grid(row=0,column=0)
mylabel1=Label(root,text="I Am The Best!").grid(row=1,column=1)
mybutton=Button(root,text="Click Me!",padx=50,state=DISABLED) """
mybutton=Button(root,text="Your Name:",padx=50,command=myclick,fg="blue",bg="silver")
mybutton.pack()
root.mainloop()