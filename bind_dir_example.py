import tkinter as tk


def callback(event):
    print(dir(event))
    print(f"You clicked at {event.x}, {event.y}")


root = tk.Tk()

tk.Label(root, text="Click at different\n locations in the frame below").pack()
frame = tk.Frame(root, bg="khaki", width=130, height=80)
frame.bind("<Button-1>", callback)
frame.pack()

root.mainloop()
