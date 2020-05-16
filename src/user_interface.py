from tkinter import Frame, Canvas, Tk, Text, LEFT, INSERT, END

root = Tk()

canvas = Canvas(root)
canvas.pack()

frame = Frame(canvas)
frame.pack()

top_text = Text(frame)
top_text.insert(
    INSERT,
    "Welcome to the Simple Alarming Service"
)
top_text.pack()

root.mainloop()