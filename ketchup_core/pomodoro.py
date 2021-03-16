# This class should store a number of states related to the
# current pomodoro run, which should be examinable from the main process
# The class itself should be a Thread/Process in itself as it should not
# be blocked by user interaction, unless specified by said interaction

import time
import datetime as dt
import tkinter
from tkinter import messagebox
import winsound

class Pomodoro:
    def __init__(self):
        # Configure the parameters from above
        self.t_now = dt.datetime.now()                           # current time for reference
        self.t_pom = 25*60                                       # Pomodoro time
        self.t_delta = dt.timedelta(0,t_pom)                     # time delta in mins
        self.t_fut = t_now + t_delta                             # future time, ending pomodoro
        self.delta_sec = 5*50                                    # Break time, after pomodoro
        self.t_fin = t_now + dt.timedelta(0, t_pom+delta_sec)    # Final time (w/ 5 mins break)
        pass

    # When and how does it stop?
    def run(self):
        # hide tkinter's main function window. We only need the alert message box
        root = tkinter.Tk()
        root.withdraw()
        #show alert message - Started
        messagebox.showinfo("Pomodoro Started!", "\nIt is now " +t_now.strftime("%H:%M") + " hrs. \nTimer set for 25 mins.")

        #initialize pomodoro counters
        total_pomodoros = 0
        breaks = 0
        
        # main script
        while True:
        # Pomodoro time!
        if t_now < t_fut:
            print ('pomodoro')
        # it is now past working pomodoro, within the break
        elif t_fut <= t_now <= t_fin:
            # check if is first time here, if so ring a bell
            print('in break')
            if breaks == 0:
                print('if break')
                # Annoy!
                for i in range(5):
                    winsound.Beep((i+100), 700)
                print('Break time!')
                breaks += 1

            else:
                print('finished')
                # Pomodoro finished. Reset breaks
                breaks = 0
                # Annoy! -> Let user know that break is over :'(
                for i in range(10):
                    winsound.Beep((i+100), 500)
                # Ask if user wants to start again
                usr_ans = messagebox.askyesno("Pomodoro Finished!", "Would you like to start another Pomodoro?")
                total_pomodoros += 1
                if usr_ans == True:
                    # user wants another pomodoro! Update values to indicate new timeset
                    t_now = dt.datetime.now()
                    t_fut = t_now + dt.timedelta(0, t_pom)
                    t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)
                    continue
                elif usr_ans == False:
                    # user is done, display achievements for now
                    messagebox.showinfo("Pomodoro Finished!", "\nYou completed              "+str(total_pomodoros)+" pomodoros today!")
                    break
            # check every 20 seconds and update current time
            print('sleeping')
            time.sleep(20)
            t_now = dt.datetime.now()
            timenow = t_now.strftime("%H:%M")
        pass

    # Follow a number of getters?
