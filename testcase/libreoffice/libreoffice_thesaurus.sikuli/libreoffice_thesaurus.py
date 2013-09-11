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

    DOC = settings.TESTDATAPATH + os.sep + "libreoffice" + os.sep + "test-fr.odt" # script directory
    
    lo.loLaunchMax(DOC)

    type(Key.HOME, Key.CTRL)
    type(Key.F7, Key.CTRL)

    try:
        find(Pattern("1377508139965.png").similar(0.90))
        type(Key.ENTER)
        find("1377566544897.png")        
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
