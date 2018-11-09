from tkinter import *
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

x = y = 300
r = r1 = 130
color = 'green'

# ваш код здесь

canv.create_oval(x, y, r,r1, fill=color)


# конец вашего кода

mainloop()