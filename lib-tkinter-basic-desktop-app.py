from tkinter import *


def button_clicked():
    # print("I got clicked")
    km = int(input.get())
    miles = km * 1.609344
    km_label.config(text=str(miles))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=100, pady=100)

#Entry
input = Entry(width=10)
input.insert(END, string="0")
# print(input.get())
input.grid(column=1, row=0)

#Label
my_label = Label(text="Miles", font=("Arial", 12, "normal"))
my_label.grid(column=2, row=0)

#Label
my_label = Label(text="is equal to", font=("Arial", 12, "normal"))
my_label.grid(column=0, row=1)

#Label
km_label = Label(text="0", font=("Arial", 12, "normal"))
km_label.grid(column=1, row=1)

#Label
my_label = Label(text="Km", font=("Arial", 12, "normal"))
my_label.grid(column=2, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


window.mainloop()
