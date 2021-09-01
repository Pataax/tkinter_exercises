import tkinter as tk


def show_event_details(event):
    print("=" * 50)
    print(f"EventKeySymbol = {str(event.keysym)}")
    print(f"EventKeyType = {str(event.type)}")
    print(f"EventWidgetID = {str(event.widget)}")
    print(f"EventCoordinate (x,y) = {str(event.x), {event.y}}")
    print(f"Time: {str(event.time)}")


root = tk.Tk()
button = tk.Button(
    root, text="Button Bound to: \n Keyboard Enter & Mouse click")
button.pack(pady=5, padx=4)
button.focus_force()
button.bind("<Button-1>", show_event_details)
button.bind("<Return>", show_event_details)

tk.Label(text="Entry is bound to Mouseclick, \nFocusIn and Keypress event").pack()
entry = tk.Entry(root)
entry.pack()
entry.bind("<Button-1>", show_event_details)
entry.bind("<Button-2>", show_event_details)
entry.bind("<FocusIn>", show_event_details)

alpha_num_keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456789"

for key in alpha_num_keys:
    entry.bind("<KeyPress-%s>" % key, show_event_details)

keysyms = [
    "Alt_L",
    "Alt_R",
    "BackSpace",
    "Cancel",
    "Caps_Lock",
    "Control_L",
    "Control_R",
    "Shift_L",
    "Shift_R",
    "Delete",
    "Down",
    "End",
    "Escape",
    "Execute",
    "F1",
    "F2",
    "Home",
    "Insert",
    "Left",
    "Right",
    "Linefeed",
    "KP_0",
    "KP_1",
    "KP_2",
    "KP_3",
    "KP_4",
    "KP_5",
    "KP_6",
    "KP_7",
    "KP_8",
    "KP_9",
    "KP_Add",
    "KP_Decimal",
    "KP_Divide",
]

for i in keysyms:
    entry.bind("<KeyPress-%s>" % i, show_event_details)

tk.Label(
    text="Canvas bound to motion event\n(hover over the area\nto see motion event)"
).pack()
canvas = tk.Canvas(root, background="white", width=100, height=30)
canvas.pack()
canvas.bind("<Motion>", show_event_details)

tk.Label(text="Entry widget bound to\n<Any KeyPress>").pack()
entry_1 = tk.Entry(root)
entry_1.pack(pady=7)
entry_1.bind("<Any KeyPress>", show_event_details)


root.mainloop()
