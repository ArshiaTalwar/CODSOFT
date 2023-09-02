from tkinter import*
from tkinter import messagebox
win=Tk()
win.geometry("500x500")
win.title("To do list")
win.config(background="pink3")
frame=Frame(win,bg="pink3")
frame.pack()
label=Label(frame,text="ENTER YOUR TASKS 3>",font=(" calibri 20 bold"))
label.pack(padx=10,pady=10)
list=[]
def task():
    task=entry.get()
    if task=="":
        messagebox.showwarning("input error")
    else:
        list.append(task)
        display.insert(END,task)
        entry.delete(0,END)
def delete():
    selected_item= display.curselection()
    for item in selected_item[::-1]:
      display.delete(item)
entry=Entry(frame,width=30,fg="black",font="Cambria 12")
entry.pack(padx=30,pady=20)
add=Button(frame,width=10,text="ADD",bd=4,bg="burlywood",activebackground="bisque",cursor="hand2",command=task)
add.pack()
display=Listbox(frame,width=70,height=10,bd=4,bg="pink",fg="maroon",font="arial 16",selectbackground="plum3",activestyle="none")
display.configure(selectmode=MULTIPLE,font="LucidaSansUnicodeRegular 16 italic")
scroll=Scrollbar(frame)
scroll.pack(side=RIGHT,fill=BOTH)
display.pack(side=LEFT,fill=BOTH)
display.configure(yscrollcommand=scroll.set)
scroll.configure(command=display.yview)
delete=Button(win,width=10,text="DELETE",bd=4,bg="burlywood",activebackground="bisque",cursor="hand2",command=delete)
delete.place(relx=0.4,rely=0.85)
win.mainloop()
