from tkinter import *


def sel():
   selection = "You selected the option " + str(var)
   label.config(text = selection)
var=0

if __name__ == "__main__":
	root = Tk()

	root.configure(background='light green')

	# set the title of GUI window
	root.title("Ishan's Program")
	root.geometry("500x300")
	root.resizable(2,2)

	rad1 = Radiobutton(root, text='Python', value=1, variable=var, command=sel)
	rad1.pack(anchor=W)
	rad2 = Radiobutton(root, text='Java   ', value=2, variable=var, command=sel)
	rad2.pack(anchor=W)
	rad3 = Radiobutton(root, text='HTML', value=3, variable=var, command=sel)
	rad3.pack(anchor=W)
	button = Button(root, text='Enter').pack()
	label = Label(root)
	label.pack()

	root.mainloop()