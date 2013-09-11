import sys, os, inspect

from sikuli import *

# To make runIDE happy when the module is updated
import desktop
reload(desktop)
from desktop import *

class Evince(object):

    def __init__(self):
        super(Evince, self).__init__()

        MENU_FILE = "1377158171882.png"
        MENU_EDIT = "1377227379772.png"
        MENU_VIEW = "1377759280301.png"

        BUTTON_CLOSE = "1377238658364.png"

    def evinceLaunch(self, filename=None):
        pass
        # if App(app_name).window():
        #     return App(app_name)
        # else:
        #     app = App(app_name)
        #     app.open()
        #     wait(wait_time)
        #     if app.window():
        #         return app
        #     else:
        #         return None

        # return None        
        # pass

class EvinceSled11Gnome(Evince, Sled11Gnome):
    def __init__(self):
        super(EvinceSled11Gnome, self).__init__()
        

class EvinceSled11Kde(Evince, Sled11Kde):
    def __init__(self):
        super(EvinceSled11Kde, self).__init__()    

class EvinceOpensuse13Gnome(Evince, Opensuse13Gnome):
    def __init__(self):
        super(EvinceOpensuse13Gnome, self).__init__()

class EvinceOpensuse13Kde(Evince, Opensuse13Kde):
    def __init__(self):
        super(EvinceOpensuse13Kde, self).__init__()
