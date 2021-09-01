"""
A demonstration of tkinter Variable Class
IntVar, StringVar & BooleanVar
"""

import tkinter as tk


root = tk.Tk()


def show():
    print("You entered:")
    print(f"Employee Number: {empolyee_number.get()}")
    print(f"Login Password: {password.get()}")
    print(f"Remember Me: {remember_me.get()}")
    print("*" * 30)


empolyee_number = tk.IntVar()
tk.Label(root, text="Employee Number:").grid(row=1, column=1)
tk.Entry(root, width=40, textvariable=empolyee_number).grid(
    row=1, column=2, columnspan=2
)

password = tk.StringVar()
tk.Label(root, text="Login Password").grid(row=2, column=1, sticky="w")
tk.Entry(root, width=40, show="*", textvariable=password).grid(
    row=2, column=2, columnspan=2
)
password.set("mysecretpassword")

tk.Button(root, text="Login", command=show).grid(row=3, column=3)

remember_me = tk.BooleanVar()
tk.Checkbutton(root, text="Remember Me", variable=remember_me).grid(row=3, column=2)
remember_me.set(True)


root.mainloop()
