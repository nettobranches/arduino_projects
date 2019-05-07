import tkinter

top = tkinter.Tk()
top.title("hello gui")
top.minsize(200,30)
helloLabel = tkinter.Label(top, text = "hola")
helloLabel.pack()

top.mainloop()