import sys, os
from sikuli import *

# Workaround to bug https://bugs.launchpad.net/sikuli/+bug/1216338
# The exception naming space has bugs, so we need to explicitly import 
# FindFailed
import org.sikuli.script.FindFailed as FindFailed

# every test case is to import the general settings module
import settings
reload(settings)

import applicationfactory
reload(applicationfactory)
from applicationfactory import ApplicationFactory

def run():

    result =  False

    lo = ApplicationFactory.create("libreoffice", "sled11", "gnome")

    lo.loCloseWindow()

    sleep(3)
    
    lo.loLaunchMax()
    
    if exists(lo.LO_STARTUP_SCREEN):
        click(lo.LO_STARTUP_SCREEN_WRITER)    

    sleep(1)
    
    type("T", Key.ALT )
    type("O", Key.ALT )
    sleep(1)    
    doubleClick("1377240557411.png")
    wait("1377240608259.png")
    
    for i in range(12):
        type(Key.DOWN)

    wait("1377240996427.png")
    
    for i in range(4):
        type(Key.TAB)
        
    type("smtp.gmail.com")
    
    for i in range(4):
        type(Key.TAB)
        
    type(Key.SPACE)

    wait(Pattern("1377500254667.png").similar(0.90))

    try: 
        find(Pattern("1377241409683.png").similar(0.90))
        result = True
    except FindFailed:
        result = False
    
    lo.loCloseWindow()
    return result

# Unit test
if __name__ == "__main__":
    print
    print "Running test case: " + sys.argv[0]
    print "Result: " + "Pass" if run() else "Fail"
    print
