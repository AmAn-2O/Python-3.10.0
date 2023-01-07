from tkinter import *
from PIL import ImageTk,Image
root=Tk()
#root.iconbitmap("C:\Users\amand\Documents\python\Tkinter.ico")
root.title('Learn To Code!')
my_img=ImageTk.PhotoImage(Image.open('C:/Users/amand/Documents/python/Tkinte/abc.png'))
my_label=Label (image=my_img)
my_label.pack()
Button_quit=Button(root,text="Exit Program",command=root.quit)
Button_quit.pack()

root.mainloop()