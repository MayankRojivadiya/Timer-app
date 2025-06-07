from tkinter import *
import math

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
timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_min_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps <= 8:
        if reps == 1 or reps == 3 or reps == 5 or reps == 7:
            label.config(text="Work", fg=GREEN)
            count_down(work_min_sec)
        elif reps == 2 or reps == 4 or reps == 6:
            label.config(text="Break", fg=PINK)
            count_down(short_break_sec)
        else:
            label.config(text="Break", fg=RED)
            count_down(long_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_second = count % 60  
    if count_second < 10:
        count_second = f"0{count_second}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        check_mark.config(text=mark)

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("work Effecient")
window.config(padx=100, pady=50, bg=YELLOW)


label = Label(text="Timer",bg=YELLOW, font=(FONT_NAME, 45, "bold"), fg=GREEN)
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./src/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME,25,"bold"), fill="white")
canvas.grid(column=1,row=1) 

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME,25,"bold"))
check_mark.grid(column=1, row=3)

window.mainloop()