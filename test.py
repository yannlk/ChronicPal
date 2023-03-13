from tkinter import Label, Button


def hello():
    label.config(text="Hello, dark world!")


label = Label(root, text="Hello, world!", font=("Helvetica", 20))
label.pack(padx=20, pady=20)

button = Button(root, text="Click me!", command=hello)
button.pack(padx=20, pady=10)

root.mainloop()