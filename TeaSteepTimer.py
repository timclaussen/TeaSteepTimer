#Tea Steep Timer, buttons to add 1 or 2 minutes, and to clear the countdown
#ALSO useful as an interactive background countdown timer
import time
from tkinter import *
import threading
import traceback
import sys

class Application(Frame):
    """GUI application with 3 seperate timer buttons"""
    def __init__(self, master):
        """Initialize the frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.countdown_timer_time = 0 #countdown timer time
        self.end_time = 0
        self.total_lbl = StringVar()
        self.create_widgets()
    def labeler(self, row_num, col_num, in_text):
        """refactored from create widgets to reduce lines creating labels"""
        self.lbl = Label(self, text = in_text,  font=("Helvetica", 14)) #font family and size modified
        self.lbl.grid(row = row_num, column = col_num, sticky = W)
        # sticky W means west (left justified)
        return self.lbl
    def var_labeler(self, row_num, col_num, in_text, text_var):
        """refactored from create widgets to reduce lines creating labels that can change"""
        text_var.set(in_text) #sets the text variable test to the input
        self.lbl = Label(self, textvariable = text_var, font=("Helvetica", 16))
        self.lbl.grid(row = row_num, column = col_num, columnspan=3, sticky = W)
        return self.lbl
    def create_widgets(self):
        """Create 1 label, 3 buttons (add 1 min, add 2 min, stop)"""
        self.lbl_1 = self.labeler(0, 0, "Time Left (seconds)")
        self.lbl_total = self.var_labeler(1, 0, "0", self.total_lbl)
        self.bttn1 =  Button(self, text = "Add 1 Min", \
                             command=self.add_1_min)
        self.bttn1.grid(row = 1, column = 1, sticky = W)
        self.bttn2 =  Button(self, text = "Add 2 Min", \
                             command=self.add_2_min)
        self.bttn2.grid(row = 1, column = 2, sticky = W)
        self.bttn_stop =  Button(self, text = "Stop Timer", \
                             command=self.stop_timer)
        self.bttn_stop.grid(row = 1, column = 3, sticky = W)
    def add_1_min(self):
        """Add a minute to the timer"""
        self.countdown_timer_time = int(time.time()) 
        self.end_time = self.countdown_timer_time + 60
        #self.end_time = self.countdown_timer_time + 6 #6 seconds for qucik debug
        self.total_lbl.set(str(int(self.end_time - self.countdown_timer_time)))
        #self.t1.start()
        self.countdown()
    def add_2_min(self):
        """Add 2 minutes to timer"""
        self.countdown_timer_time = int(time.time()) 
        self.end_time = self.countdown_timer_time + 120
        self.total_lbl.set(str(int(self.end_time - self.countdown_timer_time)))
        #self.t1.start()
        self.countdown()
    def stop_timer(self):
        """Stop and clear the timer uses class variables instead of """
        self.countdown_timer_time = 0
        self.end_time = 0
        self.total_lbl.set("0")
    def countdown(self): #background countdown
        """Threading timer to tick the countdown every couple of seconds"""
        self.t1 = threading.Timer(2.0, self.countdown)
        self.countdown_timer_time = int(time.time())
        self.total_lbl.set(str(int(self.end_time - self.countdown_timer_time)))
        if self.countdown_timer_time > self.end_time:
            self.t1.cancel
            self.notification_Frame()
        else:
            self.t1.start()
            
    def notification_Frame(self):
        for x in range (0,10):
            if x % 2 == 0:
                #config frame bg as red #FF0000
                self.configure(background="#ff0000")
                time.sleep(1)
            else:
                #config frame bg as yellow #FFFF00
                self.configure(background="#008fff")
                time.sleep(1)
        
            

#create a root window
root = Tk()
root.title("Tea Steeping Timer")
root.geometry("380x70")

#create a frame in the window to hold other widgets (old)
app = Frame(root)
app.grid()

#create a frame in the window to hold other widgets
app = Application(root)

#enter root event loop
root.mainloop()
