import sys, os, inspect

from sikuli import *

# To make runIDE happy when the module is updated
import desktop
reload(desktop)
from desktop import *

class Libreoffice(object):

    def __init__(self):
        super(Libreoffice, self).__init__()

        self.LO_ICON_LIBREOFFICE_WINDOW = ""
        self.LO_STARTUP_SCREEN = ""
        self.LO_STARTUP_SCREEN_WRITER = ""
        
        self.LO_BUTTON_RECOVERY = ""

        self.LO_BUTTON_CANCEL = ""

        self.LO_BUTTON_YES = ""
        self.LO_BUTTON_NO =  ""
        self.LO_BUTTON_REPLACE = ""

        self.LO_MENU_FILE = ""
        self.LO_MENU_EDIT = ""
        self.LO_MENU_VIEW = ""
        self.LO_MENU_TOOLS = ""
        self.LO_MENU_HELP = ""

        self.LO_GENERAL_DIALOG_ZOOM = ""

    def loLaunch(self, filename=None):
        if not filename:
            App.open(r"libreoffice")
        else:
            App.open(r"libreoffice " + filename)
        wait(5)
        if exists(self.LO_BUTTON_RECOVERY) and exists(self.LO_BUTTON_CANCEL):
           click(self.LO_BUTTON_CANCEL)
           click(self.LO_BUTTON_YES)

    def loLaunchMax(self, filename=None):
        if not filename:
            App.open(r"libreoffice")
        else:
            App.open(r"libreoffice " + filename)
        wait(5)
        if exists(self.LO_BUTTON_RECOVERY) and exists(self.LO_BUTTON_CANCEL):
           click(self.LO_BUTTON_CANCEL)
           click(self.LO_BUTTON_YES)
        self.maximizeDesktopWindow()

    def loCloseWindow(self):
        App.close("soffice.bin")

class LibreofficeSled11Gnome(Libreoffice, Sled11Gnome):
    def __init__(self):
        super(LibreofficeSled11Gnome, self).__init__()
        
        self.LO_ICON_LIBREOFFICE_WINDOW = "1377244144860.png"
        self.LO_STARTUP_SCREEN = Pattern("1377241162939.png").similar(0.50)
        self.LO_STARTUP_SCREEN_WRITER = "1377241341637.png"
        
        self.LO_BUTTON_RECOVERY = "1377243289068.png"        

        self.LO_BUTTON_CANCEL = "1377243707004.png"

        self.LO_BUTTON_YES = "1377243782396.png"
        self.LO_BUTTON_NO =  "1377243794180.png"
        self.LO_BUTTON_REPLACE = "1377566475505.png"

        self.LO_BUTTON_SAVE = "1378374521420.png"
        self.LO_BUTTON_DELETE = "1378449431020.png"
        self.LO_BUTTON_FINISH = "1378449750460.png"
        

        self.LO_MENU_FILE = "1377163667217.png"
        self.LO_MENU_EDIT = "1377163675617.png"
        self.LO_MENU_VIEW = "1377163685081.png"
        self.LO_MENU_TOOLS = "1377568508242.png"        
        self.LO_MENU_HELP = "1377163693600.png"

        self.LO_GENERAL_DIALOG_ZOOM = "1377500865988.png"

class LibreofficeSled11Kde(Libreoffice, Sled11Kde):
    pass

class LibreofficeOpensuse13Gnome(Libreoffice, Opensuse13Gnome):
    pass

class LibreofficeOpensuse13Kde(Libreoffice, Opensuse13Kde):
    pass
