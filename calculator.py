from tkinter import *
window = Tk()
window.title("Simple Calculator")
window.geometry("410x455")
window.config(bg = "black")
equation = ""
def show(value):
    global equation
    equation += value
    label1.config(text = equation)
def clear():
    global equation
    equation = ""
    label1.config(text = equation)
def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "Error"
            equation = ""
        label1.config(text = result)
        
            
            
    

label1 = Label(window,width = 26,height= 3,
               font = ("courier",20,"bold"))
label1.place(x=0,y=0)


Button(window,text = "C",bg = "blue",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = clear).place(x=10,y=110)
Button(window,text = "/",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('/')).place(x=110,y=110)
Button(window,text = "%",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('%')).place(x=210,y=110)
Button(window,text = "*",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('*')).place(x=310,y=110)

Button(window,text = "7",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('7')).place(x=10,y=180)
Button(window,text = "8",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('8')).place(x=110,y=180)
Button(window,text = "9",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('9')).place(x=210,y=180)
Button(window,text = "-",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('-')).place(x=310,y=180)

Button(window,text = "4",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('4')).place(x=10,y=250)
Button(window,text = "5",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('5')).place(x=110,y=250)
Button(window,text = "6",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('6')).place(x=210,y=250)
Button(window,text = "+",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('+')).place(x=310,y=250)

Button(window,text = "1",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('1')).place(x=10,y=320)
Button(window,text = "2",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('2')).place(x=110,y=320)
Button(window,text = "3",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('3')).place(x=210,y=320)
Button(window,text = "=",bg = "orange",fg = "white",font=("arial",20,"bold"),width = 5,height = 3,relief = RAISED,bd = 2,command = calculate).place(x=310,y=323)

Button(window,text = "0",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 11,height = 1,relief = RAISED,bd = 2,command = lambda : show('0')).place(x=10,y=390)
Button(window,text = ".",bg = "#2a2d36",fg = "white",font=("arial",20,"bold"),width = 5,height = 1,relief = RAISED,bd = 2,command = lambda : show('.')).place(x=210,y=390)









window.mainloop()
