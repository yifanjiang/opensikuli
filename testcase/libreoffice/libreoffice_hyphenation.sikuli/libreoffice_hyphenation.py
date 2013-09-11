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
   
    try:
        # open the Hyphenation Dialog
        type(Key.HOME, Key.CTRL)
        type("T", Key.ALT)
        type(Key.DOWN)
        type(Key.RIGHT)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.ENTER)

        wait(1)

        # Hyphenate all
        type("A", Key.ALT)
        find("1377568829826.png")
        type(Key.ENTER)
        find(Pattern("1377568871362.png").similar(0.90))
        find(Pattern("1377568881786.png").similar(0.90))
        type(Key.END, Key.CTRL)
        find(Pattern("1377568924058.png").similar(0.90))
        find(Pattern("1377568932274.png").similar(0.90))

        # open the Hyphenation dialog
        type(Key.HOME, Key.CTRL)
        type("T", Key.ALT)
        type(Key.DOWN)
        type(Key.RIGHT)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.ENTER)

        for i in range(10):
            type("R", Key.ALT)

        find("1377568829826.png")
        type(Key.ENTER)

        type(Key.HOME, Key.CTRL)           

        find(Pattern("1377570689899.png").similar(0.90))        
        find(Pattern("1377569447674.png").similar(0.90))
        find(Pattern("1377569414898.png").similar(0.90))
        
        type(Key.END, Key.CTRL)
        find(Pattern("1377570277402.png").similar(0.90))
       
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
