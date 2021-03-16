# This class should store a number of states related to the
# current pomodoro run, which should be examinable from the main process
# The class itself should be a Thread/Process in itself as it should not
# be blocked by user interaction, unless specified by said interaction

import time
import datetime as dt
import tkinter
from tkinter import messagebox
from threading import Thread


class Pomodoro(Thread):
    def __init__(self):
        super(Pomodoro, self).__init__()
        self.pomodoro_duration = dt.timedelta(0, 10)
        self.small_break_duration = dt.timedelta(0, 10)
        self.long_break_duration = dt.timedelta(0, 10)
        self.pomodoro_number = 4                            # Number of pomodoros
        self.to_break = 3                                   # Pomodoros before big break
        self.sleep_time = 1

    # When and how does it stop?
    def run(self):
        pom_counter = 0
        while pom_counter < self.pomodoro_number:
            pom_end = dt.datetime.now()+self.pomodoro_duration
            while dt.datetime.now() < pom_end:
                print("Pomodoro: "+dt.datetime.now().strftime("%H:%M"))
                time.sleep(self.sleep_time)
            pom_counter += 1
            if (pom_counter % self.to_break) == 0:
                break_end = dt.datetime.now() + self.long_break_duration
                while dt.datetime.now() < break_end:
                    print("Big break: " + dt.datetime.now().strftime("%H:%M"))
                    time.sleep(self.sleep_time)
            else:
                break_end = dt.datetime.now() + self.small_break_duration
                while dt.datetime.now() < break_end:
                    print("Small break: " + dt.datetime.now().strftime("%H:%M"))
                    time.sleep(self.sleep_time)


    # Follow a number of getters?
