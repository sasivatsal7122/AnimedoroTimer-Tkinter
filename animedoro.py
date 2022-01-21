'''' written by B.SASI VATSAL on 21st jan,2022 '''

# IGNORE ALL THE TYPOS #

# importing all the required modules and methods 
from tkinter import *
from tkinter import ttk
import time
from cv2 import FONT_HERSHEY_COMPLEX
import math
import pygame


# adding fonts and other common variables throught the program as global variables
blue = '#BD1616'
light_red ='#49FF00'
fire_orange ='#FF8E00'
pomo_init_timer = 25
pomo_break = 5
pomo_longbreak = 20
repetition = 0
starts_timer = NONE
streaks = NONE
''' making buttons functional'''

'''RESET BUTTON'''
def reset_timer():
    pomodoro.after_cancel(starts_timer)
    global repetition
    repetition = 0
    canvas.itemconfig(disp_heading,text="So finally you've decided to \n          study huh?!")
    canvas.itemconfig(timer_text,text="00:00")
    global streaks
    canvas.itemconfig(streaks,text='')
    
'''START BUTTON'''
def start_timer():
    pomodoro.after_cancel(starts_timer)
    global repetition
    repetition+=1
    productive_time = pomo_init_timer * 60
    smol_break = pomo_break * 60
    biyug_break = pomo_longbreak * 60
    ''' making intitial timer, short break ,long break work dynamically using if conditions'''
    if repetition%8==0:
        pygame.mixer.music.load("src/emergency_sound.mp3")
        pygame.mixer.music.play(loops=0)
        canvas.itemconfig(disp_heading,text="        Great job mate! \nhere is you're long break")
        time.sleep(1.3)
        count_down_clock(biyug_break)
    elif repetition%2==0:
        pygame.mixer.music.load("src/emergency_sound.mp3")
        pygame.mixer.music.play(loops=0)
        canvas.itemconfig(disp_heading,text="              Good job! \n Take a break, walk around")
        time.sleep(1.3)
        count_down_clock(smol_break)
    else:
        pygame.mixer.music.load("src/emergency_sound.mp3")
        pygame.mixer.music.play(loops=0)
        disp_head = canvas.itemconfig(disp_heading,text="Get back to work BIXCH!\n  i'll alert when it's time")
        time.sleep(1.3)
        count_down_clock(productive_time)
    
'''making clock to function using functions'''
def count_down_clock(count):
    '''formmating countdown to look good'''
    mins_count = math.floor(count/60)
    secs_count = count%60
    # comment this 2 lines you'll understand its functionality ( hard to xplain)
    if secs_count<10:
        secs_count=f"0{secs_count}"
    # itemconfig() is used to change text on on the canvas
    # here is is used to chagne the timer from 25:00 to 00:00 dynamically
    canvas.itemconfig(timer_text,text=f"{mins_count}:{secs_count}")
    if count>0:
        global starts_timer
        starts_timer = pomodoro.after(1000,count_down_clock,count-1)
    else:
        start_timer()
        ''' adding streak functionality '''
        streak = ""
        streak_counter = math.floor(repetition/2)
        for i in range(streak_counter):
            streak+="🔥"
        canvas.itemconfig(streak_text,text="your'e streak count: ")
        canvas.itemconfig(streaks,text=streak)
 
'''---------------------------------------------------------------------------------'''
 
''' DRIVER CODE '''
        
'''Tk() is class in tkinter module
by initiating pomodoro to Tk() we are creating an object of that class'''
pomodoro = Tk()
pomodoro.title("Animedoro Timer        ✨ HUSTLE TODAY FOR BETTER TOMORROW ✨")
'''adding padding to the UI window so that it doesn't look congested
   it can implemented by using config() method which takes arguments like
   adx and pady
    assigning name to our pomodoro timer windows'''
pomodoro.config(padx=25,pady=15,bg=blue)
# making app window non-resizable
pomodoro.resizable(False,False)
# intialzing the pygame mixer for sound output
pygame.mixer.init()

'''to put/load images into the window we need something call CANVAS
    CANVAS WIDGET is like real life canvas on which u can layer things up
    CANVAS WIDGET helps us to add images, texts etc into our UI
'''
# creating canvas and changing its background
canvas = Canvas(width=500,height=500,bg=blue, highlightthickness=False)
# adding image to the canvas using create method
# create_image takes inputs like x and y co-rd of image and path of img as well
# storing image read using PhotoImage method into the variable
# pomodoro_tomato
pomodoro_tomato= PhotoImage(file="src/test3.png")
canvas.create_image(250,250,image=pomodoro_tomato)
disp_heading = canvas.create_text(245,90,text="So finally you've decided to \n          study huh?!",fill=light_red,font=(FONT_HERSHEY_COMPLEX,20,'bold'))
# creating text using create_text method which takes 1st 2 args x and y co-ords
timer_text = canvas.create_text(229,200,text="00:00", fill='white',font=(FONT_HERSHEY_COMPLEX,95,'bold'))
# creating start and reset buttons for controlling timer (bd is for border)
start_btn= Button(canvas,text=" START ",width=12,height=2,bd='3', command=start_timer)
# placing the btn on canvas using place() method
start_btn.place(x=80,y=380)
reset_btn = Button(canvas,text=" RESET ",width=12,height=2,bd='3',command=reset_timer)
reset_btn.place(x=300,y=380)
streak_text = canvas.create_text(110,470,text="your'e streak count: 0 ",fill='white',font=(FONT_HERSHEY_COMPLEX,10,'bold'))
streaks = canvas.create_text(250,470,text=" ",font=10,fill=fire_orange)
# pack() is used to combine all the elements that has been added to the canvas
# pack basically packs the contents of the canvas together
canvas.pack()
pomodoro.mainloop()