import tkinter as tk

# Dragging
def make_draggable(widget):
    widget.bind("<Button-1>", on_drag_start)
    widget.bind("<B1-Motion>", on_drag_motion)
    widget.bind("<ButtonRelease-1>", on_drag_finish)

def on_drag_start(event):
    widget = event.widget
    widget._drag_start_x = event.x
    widget._drag_start_y = event.y

def on_drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y

    x,y = snapToWidget(button, x, y)

    widget.place(x=x, y=y)


def on_drag_finish(event):
    widget = event.widget
    x = widget.winfo_x() - widget._drag_start_x + event.x
    y = widget.winfo_y() - widget._drag_start_y + event.y

    if ((x > button.winfo_x() - 50 and x < button.winfo_x() + 50)
        and (y > button.winfo_y() - 50 and y < button.winfo_y() + 50)):
        widget.destroy()

def snapToWidget(widget, x, y):
    if ((x > widget.winfo_x() - 50 and x < widget.winfo_x() + 50)
        and (y > widget.winfo_y() - 50 and y < widget.winfo_y() + 50)):
        
        x = button.winfo_x()
        y = button.winfo_y()

    return x,y

# Cloning
def clone(widget):
    parent = widget.nametowidget(widget.winfo_parent())
    widgetClass = widget.__class__

    clone = widgetClass(parent)
    # Copy configurations
    for key in widget.configure():
        clone.configure({key: widget.cget(key)})

    # Copy events
    for e in widget.bind():
        clone.bind(e, widget.bind(str(e)) )
    return clone


def cloneOnClick(event):
    widget = event.widget
    c = clone(widget)
    c.pack()

main = tk.Tk()


frame = tk.Frame()
msg = tk.Label(text="Hello World!")
msg.pack()
msg.bind("<Button-3>", cloneOnClick)
make_draggable(msg)
button = tk.Button(text = "testing...")
button.pack()
make_draggable(button)


msg2 = tk.Label(text="Hello World!")
msg.pack()








