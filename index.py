#Import the library
from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer
import random
#intilize root as outer messagebox using Tkinter
root = Tk()
#giving dimensions to outer messagebox and backgroung colour 
root.geometry("500x500")
root.configure (bg="Black")
#intilize display as inner messagebox using tkinter

display = Tk()
#giving dimensions to inner messagebox and backgroung colour
display.geometry("550x500")
#we are hiding the display messagebox where all the typing appears before the main display that is root
display.withdraw()
#giving title as speed typing test to root and display
root.title("Speed Typing Test!!")
display.title("Speed Typing Test")
#create a highscore.txt file and save it same directory and give both read and write mode.
hs_file = open('highscore.txt', 'r+')
a = 0
#creating function name game
def game():
    global a
    if a == 0:
        root.withdraw()
        a = a+1
    display.deiconify()
    def check_result():
        
        answer=entry.get("1.0", 'end-1c')
        end = timer()
        time_taken=end-start
        #formula to calculate WPM 
        wpm = len(answer)/5
        
        wpm = int(wpm/(time_taken/60))
        hs_file.seek(0)
        line = int(hs_file.readline())
        error = len(words[word])-len(answer)
        error1 = len(answer)-len(words[word])
        if error1>error:
            error = error1
        
        if wpm>line:
            hs_file.seek(0)
            hs_file.write(str(wpm))
            result="Amazing! Your new highscore is: "+str(wpm)+" WPM \n You made " +str(error)+ " errors" 
            messagebox.showinfo("Score", result)
        else:
            result="Your score is: "+str(wpm)+" WPM\nBetter luck next time! \n You made " +str(error)+ " errors" 
            messagebox.showinfo("Score", result)
    #if user close down the then create function done which close textfile and detroy display and exits the program.        
    def done():
        hs_file.close()
        display.destroy()
        root.destroy()
        #creating list of all the sentences for typing
    words = ["Things aren't going well at all with mom today. She is just a limp noodle and wants to sleep all the time. I sure hope that things get better soon.","They rushed out the door, grabbing anything and everything they could think of they might need." , "There was no time to double-check to make sure they weren't leaving something important behind. Everything was thrown into the car and they sped off. ","Thirty minutes later they were safe and that was when it dawned on them that they had forgotten the most important thing of all.","There are different types of secrets. She had held onto plenty of them during her life, but this one was different. She found herself holding onto the worst type. It was the type of secret that could gnaw away at your insides if you didn't tell someone about it, but it could end up getting you killed if you did.","He took a sip of the drink. He wasn't sure whether he liked it or not, but at this moment it didn't matter. ","She had made it especially for him so he would have forced it down even if he had absolutely hated it."," That's simply the way things worked. She made him a new-fangled drink each day and he took a sip of it and smiled, saying it was excellent."]    
   # randomly collecting lists one by one and displaying different sentence at every time
   #Intialise variable word to store sentences from first element to last one which is multiline box and type (Text)
    word = random.randint(0, (len(words)-1))
    entry=Text(display)
    #widgets
    #putting label in display messagebox like words,submit!,another one?,etc and giving background ,size ,width etc
    #giving size of sentences in words list with height,width,font and wraplength
    x2 = Label(display, text=words[word], bg="black", fg="white", height=7, width=47, font="times 15", wraplength=500)
    x2.place(x=15, y=10)
    
    x3 = Button (display, text="Submit!", font="times 20", bg="#fc2828", command=check_result)
    x3.place(x=220, y=350)
    #intialize entry )
    entry.place(x=100, y=180, height=150, width=350)
    
    b2 = Button(display, text="Done", font="times 13", bg='#ffc003', width=12, command=done)
    b2.place(x=155, y=420)
    
    b3 = Button (display, text="Another One ?", font="times 13", bg='#ffc003', width=12, command=game)
    b3.place(x=265, y=420)

    start = timer()
    #looping the display mainloop
    #It is basically an infinite loop to run the  display so that application can run
    display.mainloop()
    
#putting label in root messagebox like Let's test your typing speed!,Go!,Highscore etc and giving background ,size ,width etc
x1 = Label(root, text="Let's test your typing speed!", bg="black", fg="white", font='times 20')
x1.place(x=100, y=50)

b1 = Button (root, text="Go!", width=12, bg='#fcba03', font="times 20", command=game)
b1.place(x=150, y=120)

hs_text = Label(root, text="Highscore", width=12, bg='#03fcf8', font="times 35")
hs_text.place(x=90, y=240)
#for reading value of highscore hs from hs_file which is textfile(which is in string format and we typecast into integer form)
hs =int(hs_file.readline())
hs_val = Label(root, text=str(hs)+" WPM", width=12, fg="#03fcf8", bg='black', font= 'times 20')
hs_val.place(x=110, y=320)
#It is basically an infinite loop to run the root display so that application can run.
root.mainloop()
