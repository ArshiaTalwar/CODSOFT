from tkinter import *
import random
import pyperclip
win=Tk()
win.geometry("400x300")
win.configure(background="khaki")
win.title("Pasword Generator")
def generate():
    characters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
             'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
             '9', '0'' ', '!', '@', '#', '$', '&','*']
    password = ""
    for i in range(len.get()):
        password=password+random.choice(characters)
    new_pass.set(password)
def copy():
    pass1=new_pass.get()
    pyperclip.copy(pass1)
len=IntVar()
new_pass=StringVar()
label=Label(win,text="Password Generator",font="calibri 18 bold")
label.pack()
len_text=Label(win,text="Length :",font="arial 12").place(relx=0.1,rely=0.2)
length=Entry(win,textvariable=len,font="calibri 12").place(relx=0.3,rely=0.2)
gen=Button(win,text="Generate",width=10,bd=3,bg="yellowgreen",command=generate).place(relx=0.37,rely=0.3)
pass_label = Label(win, text = 'Random Generated Password',font="calibri 12 bold").place(relx=0.22,rely=0.45) 
result=Entry(win,textvariable=new_pass,font="calibri ").place(relx=0.27,rely=0.6)
copy=Button(win,text="copy to clipboard",width=15,bg="yellowgreen",bd=3,command=copy).place(relx=0.32,rely=0.7)
win.mainloop()
