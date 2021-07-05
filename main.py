from tkinter import *
import math

#------------------CONSTANTS--------------------------#
ORANGE = "#ECDBBA"
RED = "#C84B31"
GREEN = "#346751"
BLACK = "#161616"
FONT_NAME = "Courier"

reps=0
timer=None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text = "Timer")


#-----------------TIMER--------------------------------#
def start_timer():
    global reps
    reps +=1
    training_min = int(training_min_input.get())
    training_sec = int(training_sec_input.get())
    rest_min = int(rest_min_input.get())
    rest_sec = int(rest_sec_input.get())

    training_time=training_min*60+training_sec
    rest_time=rest_min*60+rest_sec

    interval_num = int(interval_num_input.get())

    if (math.floor(reps/2)) == interval_num:
        count_down(rest_time)
        timer_label.config(text = "LAST ONE", fg=RED)
    elif reps % 2 == 0:
        count_down(rest_time)
        timer_label.config(text = "Break", fg=RED)
    else:
        count_down(training_time)
        timer_label.config(text = "Training", fg=GREEN)


def count_down(count):
    count_min = math.floor(count/ 60)
    count_sec = count % 60
    interval_num = int(interval_num_input.get())

    if count_sec < 10:
        count_sec = "0"+str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if interval_num != (math.floor(reps/2)):
        if count > 0:
            global timer
            timer = window.after(1000, count_down, count-1)
        else:
            start_timer()
            marks = " "
            for _ in range(math.floor(reps/2)):
                marks += "✔"
            checkmark_label.config(text = marks, fg=GREEN, bg=ORANGE, font=(FONT_NAME,20,'bold'))
    else:
        if count > 0:
            timer = window.after(1000, count_down, count-1)

#---------------------UI-----------------------------#

window = Tk()
window.title("Interval Training")
window.config(padx=50,pady=50,bg=ORANGE)

#---canvas---#
canvas = Canvas(width=200, height=112,bg=ORANGE, highlightthickness=0)
timer_text = canvas.create_text(100,70,text="00:00",fill=BLACK, font = (FONT_NAME,40,'bold'))

#----Labels----#
timer_label= Label(text="Timer",bg=ORANGE, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
checkmark_label= Label(text="",bg=ORANGE, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
training_time_label = Label(text="Training time",bg=ORANGE, fg=RED, font=(FONT_NAME, 15, 'bold'))
rest_time_label = Label(text="Rest time",bg=ORANGE, fg=RED, font=(FONT_NAME, 15, 'bold'))
interval_num_label = Label(text="Intervals",bg=ORANGE, fg=RED, font=(FONT_NAME, 15, 'bold'))
training_min_label = Label(text="Minutes",bg=ORANGE, fg=BLACK, font=(FONT_NAME, 10, 'bold'))
training_sec_label = Label(text="Seconds",bg=ORANGE, fg=BLACK, font=(FONT_NAME, 10, 'bold'))
rest_min_label = Label(text="Minutes",bg=ORANGE, fg=BLACK, font=(FONT_NAME, 10, 'bold'))
rest_sec_label= Label(text="Seconds",bg=ORANGE, fg=BLACK, font=(FONT_NAME, 10, 'bold'))

#---buttons---#
start_button = Button(text="Start",font=(FONT_NAME, 10, 'bold'),width=10,command=start_timer)

#--input--#
interval_num_input = Entry(width=5)

training_min_input = Entry(width=5)
training_sec_input = Entry(width=5)

rest_min_input = Entry(width=5)
rest_sec_input = Entry(width=5)

#---- grid----#

#row 0

timer_label.grid(row=0,column=2)

#row 1
checkmark_label.grid(row=1,column=2)
#row 2
canvas.grid(row=2,column=2)
#row 3
start_button.grid(row=3,column=2,columnspan=2,ipadx=20)

#row 4
interval_num_label.grid(row=4,column=2,sticky=W)
interval_num_input.grid(row=4,column=2,sticky=E,padx=30)

#row 5
training_time_label.grid(row=5,column=0,columnspan=2)
rest_time_label.grid(row=5,column=4,columnspan=2)

#row 6
training_min_label.grid(row=6,column=0,sticky=E)
training_min_input.grid(row=6,column=1,sticky=W)

rest_min_label.grid(row=6,column=4,sticky=E)
rest_min_input.grid(row=6,column=5,sticky=W)

#row 7

training_sec_label.grid(row=7,column=0,sticky=E)
training_sec_input.grid(row=7,column=1,sticky=W)

rest_sec_label.grid(row=7,column=4,sticky=E)
rest_sec_input.grid(row=7,column=5,sticky=W)


window.mainloop()
