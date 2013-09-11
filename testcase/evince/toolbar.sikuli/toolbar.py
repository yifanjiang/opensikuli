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

def testEvinceToolbar():

    ret = False

    evince = ApplicationFactory.create("evince", "opensuse13", "gnome")

    # implement test case here
    
    return ret

def run():
    
    return testEvinceToolbar()

if __name__ == "__main__":
    print "RESULT: " + ("PASS" if run() else "FAIL")


# import settings
# import Evince
# reload(Evince)
# from Evince import *

# IMG_DRAG = "1377227915302.png"

# def dragToToolBar(reg):
#     return dragDrop(IMG_DRAG, Location(reg.getX() + reg.getW()/2, reg.getY() +30 ))

# def dragFromToolBar(reg):
#     return dragDrop(IMG_DRAG, reg.getCenter())
    

# def doToolBarOperation( reg, func ):
#     click(Evince.MENU_EDIT)
#     click("1377227625883.png")
#     func(reg)
#     click(Evince.BUTTON_CLOSE)
#     wait(1)
    

# def test_EvinceToolbar():
#     ret = Evince.FAILED

#     app = loadApp()
#     reg = app.window()


#     if exists(IMG_DRAG):
#         doToolBarOperation(reg, dragFromToolBar)
#         if not exists(IMG_DRAG):
#             doToolBarOperation(reg, dragToToolBar)
#             if exists(IMG_DRAG):
#                 ret = Evince.PASS
        
#     else:
#         doToolBarOperation(reg, dragToToolBar)
#         if exists(IMG_DRAG):
#             doToolBarOperation(reg, dragFromToolBar)
#             if not exists(IMG_DRAG):
#                 ret = Evince.PASS

#     app.close()

#     return ret

# def run():
#     return test_EvinceToolbar()

# if __name__ == "__main__":
#     print "RESULT: " + ("PASS" if run() else "FAIL")
