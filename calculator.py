from tkinter import *


root= Tk()
root.configure(background="#81C784")
def click(event):
    global scValue
    text = event.widget.cget("text")
    if text == "=":
        if scValue.get().isdigit():
            value = int(scValue.get())
        else:
            value = eval(scValue.get())
        scValue.set(value)
        screen.update()
    elif text == "AC":
        scValue.set("")
        screen.update()
    elif text == "Del":
        a=scValue.get()
        scValue.set(a[0:-1])
        screen.update()

    else:
        scValue.set(scValue.get() + text)
        screen.update()


root.geometry("394x644")
root.maxsize(370,594)
root.title("Calculator")
scValue=StringVar()
screen = Entry(textvariable=scValue,font="airal 35 bold",bg="#B9F6CA")
screen.pack(fill="both",padx=12,pady=12)

# f=Frame(root,relief="ridge",height=630,width=320)

b=Button(text="AC",height=5,width=10,background="#00C853")
b.place(x=10, y=80)
b.bind("<Button-1>",click)

b=Button(text="Del",height=5,width=10,background="#00C853")
b.place(x=100, y=80)
b.bind("<Button-1>",click)

b=Button(text="/",height=5,width=10,background="#00C853")
b.place(x=190, y=80)
b.bind("<Button-1>",click)

b=Button(text="*",height=5,width=10,background="#00C853")
b.place(x=280, y=80)
# b.pack()
b.bind("<Button-1>",click)

b=Button(text="9",height=5,width=10,background="#00C853")
b.place(x=10, y=180)
b.bind("<Button-1>",click)

b=Button(text="8",height=5,width=10,background="#00C853")
b.place(x=100, y=180)
b.bind("<Button-1>",click)

b=Button(text="7",height=5,width=10,background="#00C853")
b.place(x=190, y=180)
b.bind("<Button-1>",click)

b=Button(text="-",height=5,width=10,background="#00C853")
b.place(x=280, y=180)
b.bind("<Button-1>",click)

b=Button(text="6",height=5,width=10,background="#00C853")
b.place(x=10, y=280)
b.bind("<Button-1>",click)

b=Button(text="5",height=5,width=10,background="#00C853")
b.place(x=100, y=280)
b.bind("<Button-1>",click)

b=Button(text="4",height=5,width=10,background="#00C853")
b.place(x=190, y=280)
b.bind("<Button-1>",click)

b=Button(text="+",height=5,width=10,background="#00C853")
b.place(x=280, y=280)
b.bind("<Button-1>",click)

b=Button(text="3",height=5,width=10,background="#00C853")
b.place(x=10, y=380)
b.bind("<Button-1>",click)

b=Button(text="2",height=5,width=10,background="#00C853")
b.place(x=100, y=380)
b.bind("<Button-1>",click)

b=Button(text="1",height=5,width=10,background="#00C853")
b.place(x=190, y=380)
b.bind("<Button-1>",click)

b=Button(text=".",height=5,width=10,background="#00C853")
b.place(x=280, y=380)
b.bind("<Button-1>",click)

b=Button(text="00",height=5,width=10,background="#00C853")
b.place(x=10, y=480)
b.bind("<Button-1>",click)

b=Button(text="0",height=5,width=10,background="#00C853")
b.place(x=100, y=480)
b.bind("<Button-1>",click)

b=Button(text="=",height=5,width=23,background="#00C853")
b.place(x=190, y=480)
b.bind("<Button-1>",click)

Label(text="cheUriBuddy",bg="#81C784",fg="purple").place(x=130,y=572)



root.mainloop()