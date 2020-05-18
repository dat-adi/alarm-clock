from tkinter import Frame, Canvas, Tk, Text, LEFT, INSERT, END, messagebox, Button, X
from alarming_service import time_diff

def GUI_present():
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

    alarm_set = Button(frame, text="Set and Deploy Alarm", command=time_diff)
    alarm_set.pack(fill=X)

    root.mainloop()

if __name__ == "__main__":
    GUI_present()