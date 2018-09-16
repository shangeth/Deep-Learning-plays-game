#imports the library
from pykeyboard import PyKeyboard
#import the sleep function
from time import sleep
#initialize the keyboard simulator
keyboard = PyKeyboard()
#presses the key
keyboard.press_key('Up')
#waits five seconds before releasing the key
sleep(3)
#releases the key
keyboard.release_key('Up')

keyboard.press_key('Down')
#waits five seconds before releasing the key
sleep(3)
#releases the key
keyboard.release_key('Down')