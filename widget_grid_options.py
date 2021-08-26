import tkinter as tk


root = tk.Tk()

tk.Label(root, text="Username").grid(row=0, sticky="w")
tk.Label(root, text="Password").grid(row=1, sticky="w")
tk.Entry(root).grid(row=0, column=1, sticky="e")
tk.Entry(root).grid(row=1, column=1, sticky="e")
tk.Button(root, text="Login").grid(row=2, column=1, sticky="e")


root.mainloop()
