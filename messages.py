"""
messages.py - control macos messages app using pyautogui
By: Matt Conforti
05/15/21
"""


# imports -------
import os
import time
import pyautogui


# main code -------
# get our text to write
file = open("message_text.txt", "r")
content = file.read()

# open Messages app
command = "open /System/Applications/Messages.app"
os.system(command)

time.sleep(2)

# click on compose message...
# screenshot needed for locateOnScreen sample
# image = pyautogui.screenshot('screen.png')
# HAVE TO TAKE SCREENSHOT THIS WAY!
# MAC SCREENSHOT DOES NOT WORK - then crop the image to select what you want

location = pyautogui.locateOnScreen('compose.png', confidence=0.9)  # color matches pixels
# confidence param uses opencv, numpy - NEED THESE DEPENDENCIES TO WORK
xYcoordinates = pyautogui.center(location)
xcoord, ycoord = xYcoordinates  # split them into own variables

# click on the images coordinates
pyautogui.moveTo(600, 125)
pyautogui.click()

# **********************
recipient = '6319051127'
# **********************

# who are we sending to?
pyautogui.write(recipient)
pyautogui.press('enter')

counter = 0
# write & send messages
for word in content.split():
    pyautogui.write(word)
    pyautogui.press("enter")
    counter+=1 # update count of successful sends, not just count of words read

print(str(counter) + " messages sent to " + recipient)
    
