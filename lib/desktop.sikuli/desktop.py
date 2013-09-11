from sikuli import *

class Desktop(object):
    
    def getDesktopScreenResolution(self):
        raise NotImplementedError("Method not implemented.")

    def showDesktop(self):
        raise NotImplementedError("Method not implemented.")

    def closeDesktopWindow(self):
        raise NotImplementedError("Method not implemented.")

    def maximizeDesktopWindow(self):
        raise NotImplementedError("Method not implemented.")        

    def minimizeDesktopWindow(self):
        raise NotImplementedError("Method not implemented.")

class Sled11Gnome(Desktop):
    def __init__(self):

        self.GTK_BUTTON_WINDOW_CLOSE = "1377162298145.png"
        self.GTK_BUTTON_WINDOW_MAXIMUM = "1377162308128.png"
        self.GTK_BUTTON_WINDOW_MINIMUM = "1377162316368.png"
        self.GTK_BUTTON_OK = "1377243541260.png"
        self.GTK_BUTTON_CANCEL = "1377243553300.png"

        self.GTK_SCROLL_BAR_VERTICAL = "1377162387472.png"
        self.GTK_SCROLL_BAR_HORIZONTAL = "1377162407224.png"

        self.GTK_MENU_ITEM_MINIMIZE = "1377241539435.png"
        self.GTK_MENU_ITEM_MAXIMIZE = "1377241526491.png"

    def getDesktopScreenResolution():
        scr = Screen()
        return [scr.getW(), scr.getH()]

    def showDesktop(self):
        pass

    def closeDesktopWindow(self):
        pass

    def maximizeDesktopWindow(self):
        if exists(Pattern(self.GTK_BUTTON_WINDOW_MAXIMUM).exact()):
            click(self.GTK_BUTTON_WINDOW_MAXIMUM)
        else:
            return

    def minimizeDesktopWindow(self):
        if exists(Pattern(self.GTK_BUTTON_WINDOW_MINIMUM).exact()):
            click(self.GTK_MENU_ITEM_MINIMIZE)
        else:
            return
        
    def openGnomeAppPanel(self):
        pass

    def openGnomeControlCenter(self):
        pass

class Sled11Kde(Desktop):
    pass

class Opensuse13Gnome(Desktop):
    pass

class Opensuse13Kde(Desktop):
    pass
