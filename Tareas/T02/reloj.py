
# https://www.daniweb.com/programming/software-development/code/485072/count-seconds-in-the-background-python

import threading
import time

class Reloj(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/1000 of a second
    '''
    def __init__(self, interval):
        # init the thread
        threading.Thread.__init__(self)
        self.interval = interval  # seconds
        # initial value
        self.value = 0
        # controls the while loop in method run
        self.alive = False
    def run(self):
        '''
        this will run in its own thread via self.start()
        '''
        self.pausa = False
        self.alive = True
        while self.alive:
            if not self.pausa:
                time.sleep(self.interval)
                # update count value
                self.value += self.interval
    def peek(self):
        '''
        return the current value
        '''
        return self.value

    def pausar(self):
        if not self.pausa:
            self.pausa = True
        else:
            self.pausa = False

    def finish(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.value

