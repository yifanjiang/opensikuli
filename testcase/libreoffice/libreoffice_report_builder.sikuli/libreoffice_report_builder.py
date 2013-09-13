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
    
    DOC = settings.TESTDATAPATH + os.sep + "libreoffice" + os.sep + "data0.odb" # script directory
    lo.loLaunchMax(DOC)

    try:
        click("1378372781588.png")
        doubleClick("1378372843380.png")

        wait("1378372980533.png", 10)


        type(Key.F4, Key.ALT)
        wait(2)
        lo.loCloseWindow()

        wait(5)

        lo.loLaunchMax(DOC)

        click("1378372781588.png")

        #create a new report by using Design View
        click("1378373516997.png")

        wait("1378373557102.png")

        doubleClick("1378373787308.png")
        doubleClick("1378373810164.png")
        type(Key.F4, Key.ALT)
        wait(1)
        type("s", Key.CTRL)
        wait(1)
        click(lo.LO_BUTTON_SAVE)
        wait(1)
        type(Key.F4, Key.ALT)
        wait(1)
        
        #reg acts as an image for result computing and a button to click
        reg = "1378449304604.png"
        find(reg)
        performDelete(reg)
        #end

        #use Wizard to create a new report
        click("1378449600484.png")
        wait("1378449675902.png")
        click("1378449705861.png")
        click(lo.LO_BUTTON_FINISH)

        wait("1378449823380.png", 10)
        type(Key.F4,Key.ALT)
        wait(1)

        #reg acts as an image for result computing and a button to click
        reg = "1378449993668.png"
        find(reg)
        performDelete(reg)
        #end

        result = True

    except FindFailed:
        result = False


    lo.loCloseWindow()

    return result

def performDelete(Image):
    rightClick(Image)
    wait(1)
    type(Key.DOWN)
    type(Key.DOWN)     
    type(Key.ENTER)
    type(Key.ENTER)        
    waitVanish(Image)

if __name__ == "__main__":
    print "Result: " + ("Pass" if run() else "Fail")

