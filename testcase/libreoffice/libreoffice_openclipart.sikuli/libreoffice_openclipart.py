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

import logging
reload(logging)

def run():

    result =  False

    logger = logging.getLogger("MyLogger")
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    lo = ApplicationFactory.create("libreoffice", "sled11", "gnome")

    lo.loCloseWindow()
    sleep(3)

    lo.loLaunchMax()

    #Test Case 1029917
    try:
        if exists(lo.LO_STARTUP_SCREEN):
            click(lo.LO_STARTUP_SCREEN_WRITER)

        wait(3)

        G_Button = "1378454718539.png"

        Thumb = "1378454775171.png"
        Image = "1378455608069.png"

        if not exists(Thumb):
            click(G_Button)
        rightClick(Thumb)
        wait(1)

        wait(Pattern("1378454993460.png").similar(0.50),10) #vp3
        logger.info('vp3 done')


        #insert copy
        type(Key.DOWN)
        type(Key.RIGHT)
        type(Key.ENTER)
        wait(1)
        click(Thumb)
        type(Key.F4, Key.ALT)
        wait(2)
        find(Image) 

        click(Image)
        type(Key.DELETE) #vp4 end
        logger.info('vp4 done')

        wait(1)

        if not exists(Thumb):
            click(G_Button)
        rightClick(Thumb) #vp5 begin
        wait(1)
        #insert link
        type(Key.DOWN)
        type(Key.RIGHT)
        type(Key.DOWN)
        type(Key.ENTER)
        wait(1)
        click(Thumb)
        type(Key.F4, Key.ALT)
        wait(2)
        find(Image)
        click(Image)
        type(Key.DELETE) 
        logger.info('vp5 done')

        #vp5 end
        
        wait(1)
        if not exists(Thumb):
            click(G_Button)
        rightClick(Thumb) #vp6 begin
        wait(1)
        #insert background page
        type(Key.DOWN)
        type(Key.RIGHT)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.RIGHT)
        type(Key.ENTER)
        wait(1)
        click(Thumb)
        type(Key.F4, Key.ALT)
        wait(2)
        find(Image)
        type("z", Key.CTRL)
        logger.info('vp6 done')

        #vp6 end
        
        wait(1)
        
        '''
        #vp7
        #insert background paragraph
        #first type a simple paragraph

        #issue here.  type(Key.SHIFT, Key.ENTER) can't input Shift + Enter
        for i in range(15):
            type('s')
            type(Key.SHIFT, Key.ENTER)

        if not exists(Thumb):
            click(G_Button)
        rightClick(Thumb)
        wait(1)
        #insert background page
        type(Key.DOWN)
        type(Key.RIGHT)
        type(Key.DOWN)
        type(Key.DOWN)
        type(Key.RIGHT)
        type(Key.DOWN)
        type(Key.ENTER)
        wait(1)
        click(Thumb)
        type(Key.F4, Key.ALT)
        wait(2)
        find(Image)
        '''

        result = True

    except FindFailed:
        pass

    lo.loCloseWindow()
    return result

if __name__ == "__main__":
    print "Result: " + ("PASS" if run() else "FAIL")