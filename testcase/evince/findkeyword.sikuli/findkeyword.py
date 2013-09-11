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

def testEvinceFind(file_name, keyword):

    ret = False

    evince = ApplicationFactory.create("evince", "opensuse123", "gnome")

    # old snippet
    # app = loadApp()
    # openFile(app, file_name)

    # reg = app.window()

    # click(Evince.MENU_EDIT)
    # click("1377160293615.png")
    # type(keyword)
    
    # isVanish = waitVanish("1377160477858.png",10)

    # if isVanish:
    #     if exists("1377161046584.png"):
    #         ret = Evince.PASS

    # app.close()

    return ret

def run():

    keyword = 'motivating comments'

    file_name = settings.TESTDATAPATH + os.sep + "evince" + os.sep + "test.pdf" # script directory
    
    return testEvinceFind(file_name, keyword)


if __name__ == "__main__":
    print "RESULT: " + ("PASS" if run() else "FAIL")
