from tkinter import *
def add():
    listbox.insert(listbox.size(),entry.get())
    listbox.config(height = listbox.size())
    entry.delete(0,END)
def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height = listbox.size())
    
window = Tk()
window.geometry("700x700")
window.title("TO DO LIST")
label1 = Label(window,
              text = "To Do List",
              font = ("Courier",30,"bold"),
              fg = "black",
              bg = "green",
              width = 100,
              height = 3,
              relief = RAISED
              )
label1.pack()

label2 = Label(window,
               text = "Add Items :",
               font = ("Courier",30),
               fg = "blue"
               )
label2.place(x=10,y=150)

entry = Entry(window,
              font = ("Courier",25),
              fg = "black"
              )
entry.place(x=10,y=200)

addbutton = Button(window,
                   text = "Add",
                   bg = "orange",
                   fg="black",
                   font = ("Courier",14),
                   command = add,
                   relief = RAISED,
                   bd = 5
                      )
addbutton.place(x=430,y=200)

deletebutton = Button(window,
                      text = "Delete",
                      bg = "orange",
                      fg="black",
                      font = ("Courier",13),
                      command = delete,
                      relief = RAISED,
                      bd = 5
                      )
deletebutton.place(x=500,y=200)


label3 = Label(window,
               text = "Tasks !",
               font = ("Courier",30),
               fg = "blue"
               )
label3.place(x=10,y=250)


listbox = Listbox(window,
                  width = 100,
                  fg = "black",
                  font = ("Courier",30),
                  bg = "lightgreen"
                  )
listbox.place(x=10,y=320)
               

window.mainloop()
