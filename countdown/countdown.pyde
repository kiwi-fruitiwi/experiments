"""
Apparently this is a wrapper for Java's Timer class.

 Countdown Class (v1.2.5)
 GoToLoop (2017/Aug/28)
 Forum.Processing.org/two/discussion/27733/
 countdown-class-library-for-java-js-python#Item_2
 Forum.Processing.org/two/discussion/23846/
 time-delay-in-python-mode#Item_14
 Gist.GitHub.com/GoToLoop/a476ac6a01d18700240853fed33c0e57
"""

from countdown import Countdown

SECS = 2.5
WAIT_TIME = (SECS * 1000)

WAITING_BG = PImage.BLUE_MASK | PImage.ALPHA_MASK
DONE_BG = PImage.RED_MASK | PImage.ALPHA_MASK

countdown = Countdown(WAIT_TIME)

def setup():
    size(300, 180)
    smooth(3)
    frameRate(10)

    colorMode(RGB)
    fill(0xffFFFF00)

    textSize(0100)
    textAlign(CENTER, CENTER)

    m = millis()
    t = m + WAIT_TIME
    countdown.start()
    print m, t, t - m, TAB, countdown


def draw(AWAIT='Awaiting ' + `SECS`, END='Finished'):
    this.surface.title = countdown.done and END or AWAIT
    background(DONE_BG if countdown.done else WAITING_BG)

    txt = `millis()` + ENTER + `frameCount`
    text(txt, width>>1, height>>1)
