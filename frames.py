from tkinter import *
root=Tk()
root.title("Learn To Code")
frame=LabelFrame(root,text="This Is My Frame......!",padx=50,pady=50)
frame.pack(padx=100,pady=100)
b=Button(frame,text="Don't Click Here!")
b2=Button(frame,text="Click Here!")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)
root.mainloop()