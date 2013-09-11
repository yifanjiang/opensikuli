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

def testEvinceOpenFile(app_name, file_name):

    ret = False

    evince = ApplicationFactory.create("evince", "opensuse123", "gnome")    
    # old snippet
    # openFile(app, file_name)
    # reg = app.window()

    # if reg.exists("1377762212876.png"):
    #     ret = Evince.PASS
    # app.close()
    return ret

def run():
    app_name = "evince"
    file_name = settings.TESTDATAPATH + os.sep + "evince" + os.sep + "test.pdf" # script directory
    
    return testEvinceOpenFile(app_name, file_name)


if __name__ == "__main__":
    print "RESULT: " + ("PASS" if run() else "FAIL")
