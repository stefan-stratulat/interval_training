from tkinter import *
import math

#------------------CONSTANTS--------------------------#
ORANGE = "#ECDBBA"
RED = "#C84B31"
GREEN = "#346751"
BLACK = "#161616"
FONT_NAME = "Courier"


#---------------------UI-----------------------------#

window = Tk()
window.title("Interval Training")
window.config(padx=50,pady=50,bg=ORANGE)

#---canvas---#
canvas = Canvas(width=200, height=224,bg=ORANGE, highlightthickness=0)
timer_text = canvas.create_text(100,130,text="00:00",fill=BLACK, font = (FONT_NAME,40,'bold'))

#----Labels----#
timer_label= Label(text="Timer",bg=ORANGE, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
training_time_label = Label(text="Training time",bg=ORANGE, fg=RED, font=(FONT_NAME, 15, 'bold'))
rest_time_label = Label(text="Rest time",bg=ORANGE, fg=RED, font=(FONT_NAME, 15, 'bold'))
interval_num_label = Label(text="Intervals",bg=ORANGE, fg=RED, font=(FONT_NAME, 15, 'bold'))
training_min_label = Label(text="Minutes",bg=ORANGE, fg=BLACK, font=(FONT_NAME, 10, 'bold'))
training_sec_label = Label(text="Seconds",bg=ORANGE, fg=BLACK, font=(FONT_NAME, 10, 'bold'))
rest_min_label = Label(text="Minutes",bg=ORANGE, fg=BLACK, font=(FONT_NAME, 10, 'bold'))
rest_sec_label= Label(text="Seconds",bg=ORANGE, fg=BLACK, font=(FONT_NAME, 10, 'bold'))

#---buttons---#
start_button = Button(text="Start",font=(FONT_NAME, 10, 'bold'),width=10)

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

canvas.grid(row=1,column=2)

#row 2

start_button.grid(row=2,column=2,columnspan=2,ipadx=20)

#row 3
interval_num_label.grid(row=3,column=2,sticky=W)
interval_num_input.grid(row=3,column=2,sticky=E,padx=30)

#row 4
training_time_label.grid(row=4,column=0,columnspan=2)
rest_time_label.grid(row=4,column=4,columnspan=2)

#row 5
training_min_label.grid(row=5,column=0,sticky=E)
training_min_input.grid(row=5,column=1,sticky=W)

rest_min_label.grid(row=5,column=4,sticky=E)
rest_min_input.grid(row=5,column=5,sticky=W)

#row 6

training_sec_label.grid(row=6,column=0,sticky=E)
training_sec_input.grid(row=6,column=1,sticky=W)

rest_sec_label.grid(row=6,column=4,sticky=E)
rest_sec_input.grid(row=6,column=5,sticky=W)


window.mainloop()
