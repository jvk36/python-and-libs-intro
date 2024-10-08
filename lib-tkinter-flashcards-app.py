from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
try:
    df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
to_learn = df.to_dict(orient="records")
# print(to_learn)
current_card = {}


def next_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_img_id, image=card_front_img)
    timer = window.after(3000, flip_card)


def next_card_and_remove():
    to_learn.remove(current_card)
    next_card()
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img_id, image=card_back_img)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_img_id = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
card_back_img = PhotoImage(file="images/card_back.png")
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_image, highlightthickness=0, command=next_card_and_remove)
tick_button.grid(row=1, column=1)

next_card()

window.mainloop()

df_save = pandas.DataFrame(data=to_learn)
df_save.to_csv("data/words_to_learn.csv", index=False)
