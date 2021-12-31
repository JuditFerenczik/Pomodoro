from tkinter import *
import time
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.3
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 0.25
reps = 0
timer = None


def reset_timer():
    global reps
    window.after_cancel(timer)
    timer_title.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_label["text"] = ""
    reps = 0


def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    print(reps)
    if reps % 8 == 7:
        counter(long_break_sec)
        timer_title.config(text="LONG BREAK", fg=PINK)
    elif reps % 2 == 0:
        timer_title.config(text="WORKING HOURS", fg=RED)
        if reps != 0:
            check_label["text"] += " 🗸"
        counter(work_sec)
    else:
        counter(short_break_sec)
        timer_title.config(text="SHORT BREAK", fg=PINK)

    reps += 1


def counter(count):
    print(count)
    global  timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, counter, count-1)
    else:
        start_timer()


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=206, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1, row=1)

#counter(5)

timer_title = Label()
timer_title.config(text="TIMER",bg =YELLOW, fg=GREEN, font=(FONT_NAME,26,"bold"))
timer_title.grid(row=0,column=1)

start_button = Button(command=start_timer)
start_button.config(text="START", font=(FONT_NAME, 18, "bold"))
start_button.grid(row=2,column=0)

reset_button = Button(command=reset_timer)
reset_button.config(text="RESET", font=(FONT_NAME,18,"bold"))
reset_button.grid(row=2,column=2)

check_label = Label()
check_label.config(text="",bg=YELLOW, fg=GREEN, font=(FONT_NAME,30,"bold"))
check_label.grid(row=3, column=1)

window.mainloop()