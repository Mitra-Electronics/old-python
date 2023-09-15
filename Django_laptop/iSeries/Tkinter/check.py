from tkinter import *

var=0
def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

if __name__ == "__main__":
	root = Tk()

	root.configure(background='light green')

	# set the title of GUI window
	root.title("Ishan's Program")
	root.rowconfigure(0, minsize=50, weight=1)
	root.columnconfigure([0, 1, 2], minsize=50, weight=1)
	root.geometry("300x200")
	root.resizable(2,2)
	buttonm = Button(master=root, text="-", command=decrease)
	buttonm.grid(row=0, column=0, sticky="nsew")
	lbl_value = Label(master=root, text="0")
	lbl_value.grid(row=0, column=1, sticky="nsew")
	buttonp = Button(root, text='+', command=increase).grid(row=0, column=2, sticky="nsew")
	while True:
		lbl_value.update()
	root.mainloop()