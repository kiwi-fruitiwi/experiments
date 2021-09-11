"""
 Countdown Class (v1.2.5)
 GoToLoop (2017/Aug/26)
 https://Forum.Processing.org/two/discussion/27733/
 countdown-class-library-for-java-js-python#Item_2
 https://Forum.Processing.org/two/discussion/23846/
 time-delay-in-python-mode#Item_14
 https://Gist.GitHub.com/GoToLoop/a476ac6a01d18700240853fed33c0e57
"""

from java.util import Timer, TimerTask

class Countdown:
    _t = Timer('Countdown')

    def __init__(self, waitTime=0): # milliseconds
        self.delay = abs(int(waitTime))
        self.done = True

        class Job(TimerTask):
            def run(_): self.done = True

        self._Timeout = Job
        self.task = None


    def __str__(self, STR='Delay: %d  -  Done: %s'):
        return STR % (self.delay, self.done)


    def start(self):
        self.task and self.task.cancel()
        self.task = self._Timeout()
        self.done = False
        self._t.schedule(self.task, self.delay)
        return self
