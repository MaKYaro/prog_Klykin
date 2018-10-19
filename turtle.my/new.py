from tkinter import *

root = Tk()
root.geometry('800x600')        # размер окна 800x600


entry = Entry(width=20)
button = Button(text="Do thing")
label = Label(bg="black", fg="white", width=20)

entry.pack()
button.pack()
label.pack()


def srt_to_sort_str(event) :
    s = entry.get()
    s.split()
    s.sort()
    label['text'] = ' '.join(s)
button.bind('<Button>', srt_to_sort_str)


mainloop()