import tkinter as tk


root = tk.Tk()
# root.geometry("500x500+200+200")

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Pack demo of side and fill").pack()
tk.Button(frame, text="A").pack(side="left", fill="y")
tk.Button(frame, text="B").pack(side="top", fill="x")
tk.Button(frame, text="C").pack(side="right", fill=None)
tk.Button(frame, text="D").pack(side="top", fill="both")

new_frame = tk.Frame(root)
new_frame.pack()
tk.Button(new_frame, text="left").pack(side="left")
tk.Button(new_frame, text="center").pack(side="left")
tk.Button(new_frame, text="right").pack(side="left")

tk.Label(root, text="Pack demo of expand").pack()
tk.Button(root, text="I do not expand").pack()
tk.Button(root, text="I do not fill x but i expand").pack(expand=1)
tk.Button(root, text="I fill x and expand").pack(fill="x", expand=1)

root.mainloop()
