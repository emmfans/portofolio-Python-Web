from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
c=""
mytimer=0

def reset():
    window.after_cancel(mytimer)
    reps=1
    c=""
    labelT.config(text="Timer",fg=GREEN)
    labelC.config(text="")
    canvas.itemconfig(timertext,text="00:00")

def start():
    global reps
    countS=SHORT_BREAK_MIN*60
    countL=LONG_BREAK_MIN*60
    countW=WORK_MIN*60

    if reps%8==0:
        countdown(countL)
        labelT.config(text="Break",fg=PINK)
    elif reps%2==1 or reps==1:
        countdown(countW)
        labelT.config(text="Work", fg=RED)
    elif reps%2==0:
        countdown(countS)
        labelT.config(text="Break", fg=GREEN)


def countdown(count):
    global reps,c,mytimer
    count_min=math.floor(count/60)
    if count_min <10:
        count_min="0"+str(count_min)
    count_sec=count%60
    if count_sec <10:
        count_sec="0"+str(count_sec)
    canvas.itemconfig(timertext,text=f"{count_min}:{count_sec}")
    if count>0:
        mytimer=window.after(1000,countdown,count-1)
    else:
        reps+=1
        if reps%2==0:
            c = c + "✔"
            labelC.config(text=f"{c}")
        start()



def action():
    pass

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
image_t=PhotoImage(file="tomato.png")

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=image_t)
timertext=canvas.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)

labelT = Label(text="Timer")
labelT.config(bg=YELLOW,font=(FONT_NAME,50,'bold'),fg=GREEN)
labelT.grid(column=1,row=0)

labelC = Label(text="This is old text")
labelC.config(text="",bg=YELLOW,font=(FONT_NAME,15,'bold'),fg=GREEN)
labelC.grid(column=1,row=5)

button = Button(text="Start", command=start)
button.config(highlightthickness=0)
button.grid(column=0,row=4)

buttonR = Button(text="Reset", command=reset)
buttonR.config(highlightthickness=0)
buttonR.grid(column=3,row=4)











window.mainloop()