import tkinter as tk


root = tk.Tk()
root.geometry("600x400")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)
root.rowconfigure((0, 1), weight=1)

rectangle_1 = tk.Label(root, text="Rectangle 1", bg="green", fg="white")
rectangle_1.grid(column=0, row=0, ipadx=10, ipady=10, sticky="nsew")

rectangle_2 = tk.Label(root, text="Rectangle 2", bg="red", fg="white")
rectangle_2.grid(column=1, row=0, ipadx=10, ipady=10, sticky="nsew")


root.mainloop()
