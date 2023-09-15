import tkinter as Tk
from tkinter import *
from tkinter import messagebox

def calculate():
    dis = (price_field.get() * discount_field.get()) / 100
    disprice = price_field.get() - dis
    Output.insert(END, disprice)
    messagebox.showinfo("showinfo", "Discounted Price is Rs. ", disprice)
    
if __name__ == "__main__":
    # create a GUI window 
    root = Tk()
    # set the background colour of GUI window 
    root.configure(background='light green') 

    # set the title of GUI window 
    root.title("Discounted Price Calculator") 

    # set the configuration of GUI window 
    root.geometry("500x300")
    heading = Label(root, text="Discounted Price Calculator", bg="light green").grid(row=0, column=1)

    price = Label(root, text="Price of your product:", bg="light green").grid(row=1, column=0)
    
    price_field = Entry(root).grid(row=1, column=1, ipadx="100")

    discount = Label(root, text="Discounted price of your product(in percentage):", bg="light green").grid(row=2, column=0)

    discount_field = Entry(root).grid(row=2, column=1, ipadx="100")
    
    submit = Button(root, text="Submit", fg="Black", bg="Red", command=calculate).grid(row=8, column=1)

    Output = Text(root, height = 5, width = 25, bg = "light cyan")

    root.mainloop()
