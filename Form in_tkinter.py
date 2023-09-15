from tkinter import*
import pandas as pd
import xlwt

form = Tk()
form.title("Form")
Input = StringVar()
Class = StringVar()
Roll = StringVar()

name_d

name = Entry(form,font=('calibri', 10,'bold'), textvariable = Input, bd = 30,
             insertwidth = 4, justify = 'left').grid(columnspan = 4)

clas = Entry(form,font=('calibri', 10,'bold'), textvariable = Class, bd = 30,
             insertwidth = 4, justify = 'left').grid(columnspan = 4)

rollno = Entry(form,font=('calibri', 10,'bold'), textvariable = Roll, bd = 30,
             insertwidth = 4, justify = 'left').grid(columnspan = 4)

re = pd.DataFrame(name, clas, rollno)
Ex = pd.ExcelWriter('Info.xlsx', engine = 'xlsxwriter')
re.to_excel(Ex, sheet_name = 'Sheet1')
Ex.save()
