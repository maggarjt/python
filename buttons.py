import tkinter as tk
import webbrowser

def click_cp(event):
	webbrowser.open_new_tab('www.google.com')

def doorbell(event):
	print("You rang the doorbell!")



window = tk.Tk()

window.geometry("300x200")

alabel = tk.Label(text="Banana")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="Apple")
blabel.grid(column=1, row=0)

button = tk.Button(window, text="Doorbell")
button.grid(column=0)

button2 = tk.Button(window, text="Clever")
button2.grid(column=1, row=1)


button.bind("<Button-1>", doorbell)
button2.bind("<Button-1>", click_cp)


window.mainloop()
