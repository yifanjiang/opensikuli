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

def testEvinceView(file_name):

    ret = False

    evince = ApplicationFactory.create("evince", "opensuse123", "gnome")

    # implement test case here
    
    return ret

def run():

    file_name = settings.TESTDATAPATH + os.sep + "evince" + os.sep + "test.pdf" # script directory
    
    return testEvinceView(file_name)


if __name__ == "__main__":
    print "RESULT: " + ("PASS" if run() else "FAIL")



# import Evince
# reload(Evince)
# from Evince import *

# def test_EvinceView(file_name):
#     ret = Evince.FAILED

#     app = loadApp()
#     openFile(app, file_name)

#     wait(2)

#     old_size = (app.window().getW(), app.window().getH())

#     click(Evince.MENU_VIEW)
#     click("1377759415590.png")
#     wait(2)

#     screen = Screen()

#     #Check if the window size equals to the screen size after press fullscreen
#     if (app.window().getW(), app.window().getH()) == (screen.getW(), screen.getH()):
#         type(Key.ESC)
#         wait(2)
#         #After press ESC, check if the window size restores to the stored old size
#         if (app.window().getW(), app.window().getH()) == old_size:
#             ret = Evince.PASS

#     app.close()
#     return ret

# def run():
#     file_name = Evince.FILE_NAME
#     return test_EvinceView(file_name)

# if __name__ == "__main__":
#     print "RESULT: " + ("PASS" if run() else "FAIL")
