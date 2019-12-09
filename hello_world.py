from tkinter import *

def plusAction(event):
    f_n = int(first_number.get())
    s_n = int(second_number.get())
    l["text"] = str(f_n + s_n)

def minusAction(event):
    f_n = int(first_number.get())
    s_n = int(second_number.get())
    l["text"] = str(f_n - s_n)


def divAction(event):
    f_n = int(first_number.get())
    s_n = int(second_number.get())
    l["text"] = str(f_n / s_n)

def manyAddsAction(event):
    f_n = int(first_number.get())
    s_n = int(second_number.get())
    l["text"] = str(f_n * s_n)

root = Tk()
first_number = Entry(width=30)
second_number = Entry(width=30)
plus = Button(text="+", width=30)
minus = Button(text="-", width=30)
div = Button(text="/", width=30)
many_adds = Button(text="*", width=30)
l = Label(bg='grey', fg='white', width=20)

plus.bind('<Button-1>', plusAction)
minus.bind('<Button-1>', minusAction)
div.bind('<Button-1>', divAction)
many_adds.bind('<Button-1>', manyAddsAction)



first_number.pack()
second_number.pack()
plus.pack()
minus.pack()
div.pack()
many_adds.pack()
l.pack()
root.mainloop()