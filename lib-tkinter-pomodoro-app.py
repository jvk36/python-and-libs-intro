import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    reps = 0
    label.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        seconds_to_work = LONG_BREAK_MIN # * 60
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        seconds_to_work = SHORT_BREAK_MIN # * 60
        timer_label.config(text="Break", fg=PINK)
    else:
        seconds_to_work = WORK_MIN # * 60
        timer_label.config(text="Work", fg=GREEN)
    countdown(seconds_to_work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global reps
    global timer
    minutes = math.floor(count/60)
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            current_ticks = label.cget("text")
            current_ticks = current_ticks + "✓"
            label.config(text=current_ticks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW)  # , highlightthickness = 0)
tomato_img = PhotoImage(file="./images/tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
label.grid(row=3, column=1)

window.mainloop()
