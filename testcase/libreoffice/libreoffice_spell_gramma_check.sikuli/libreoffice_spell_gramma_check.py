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

    sleep(1)

    DOC = settings.TESTDATAPATH + os.sep + "libreoffice" + os.sep + "test-fr.odt" # script directory
    
    lo.loLaunchMax(DOC)

    wait(2)
    
    try:
        find(Pattern("1377573392284.png").similar(0.90))
        find(Pattern("1378882555224.png").similar(0.90))
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
