import tkinter as tk


PROGRAM_NAME = "Footprint Editor"

root = tk.Tk()
root.geometry("350x350")
root.title(PROGRAM_NAME)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

new_file_icon = tk.PhotoImage(file="icons/new_file.gif")
open_file_icon = tk.PhotoImage(file="icons/open_file.gif")
save_file_icon = tk.PhotoImage(file="icons/save.gif")
cut_file_icon = tk.PhotoImage(file="icons/cut.gif")
copy_file_icon = tk.PhotoImage(file="icons/copy.gif")
paste_file_icon = tk.PhotoImage(file="icons/paste.gif")
undo_file_icon = tk.PhotoImage(file="icons/undo.gif")
redo_file_icon = tk.PhotoImage(file="icons/redo.gif")

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", accelerator="Ctrl+N",
                      compound="left", image=new_file_icon, underline=0,)
menu_bar.add_cascade(label="File", menu=file_menu)

view_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)

about_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="About", menu=about_menu)


root.mainloop()
