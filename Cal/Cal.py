from tkinter import*

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    Input.set(operator)

def ClearD():
    global operator
    operator = ""
    Input.set("")

def Equalto():
    global operator
    res = str(eval(operator))
    Input.set(res)
    operator = ""

cal = Tk()
cal.title("Calculator")
operator = ""
Input = StringVar()

txtDisplay = Entry(cal,font=('arial', 20,'bold'), textvariable = Input, bd = 30, insertwidth = 4,
                   bg = "powder blue", justify = 'right').grid(columnspan = 4)

btn1 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "7", bg = "powder blue",command = lambda:btnClick(7)).grid(row = 1, column = 0)

btn2 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "8", bg = "powder blue",command = lambda:btnClick(8)).grid(row = 1, column = 1)

btn3 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "9", bg = "powder blue",command = lambda:btnClick(9)).grid(row = 1, column = 2)

btn4 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "X",command = lambda:btnClick("*")).grid(row = 1, column = 3)

btn5 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "4", bg = "powder blue",command = lambda:btnClick(4)).grid(row = 2, column = 0)

btn6 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "5", bg = "powder blue",command = lambda:btnClick(5)).grid(row = 2, column = 1)

btn7 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "6", bg = "powder blue",command = lambda:btnClick(6)).grid(row = 2, column = 2)

btn8 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "-",command = lambda:btnClick("-")).grid(row = 2, column = 3)

btn9 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "3", bg = "powder blue",command = lambda:btnClick(3)).grid(row = 3, column = 0)

btn0 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "2", bg = "powder blue",command = lambda:btnClick(2)).grid(row = 3, column = 1)

btn11 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "1", bg = "powder blue",command = lambda:btnClick(1)).grid(row = 3, column = 2)

btn12 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "+",command = lambda:btnClick("+")).grid(row = 3, column = 3)

btn13 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "0", bg = "powder blue",command = Equalto).grid(row = 4, column = 0)

btn14 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "C", command = ClearD).grid(row = 4, column = 1)

btn15 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "=", command = Equalto).grid(row = 4, column = 2)

btn16 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "/", command = lambda:btnClick("/")).grid(row = 4, column = 3)

btn17 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = "CE", command = ClearD).grid(row = 5, column = 0)

btn18 = Button(cal,padx = 16,  bd = 8, fg = "black", font = ('arial', 20,'bold'),
              text = ".", bg = "powder blue",command = lambda:btnClick(".")).grid(row = 5, column = 1)
