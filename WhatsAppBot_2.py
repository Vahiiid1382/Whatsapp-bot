'''
Code : WP Bot
by : vahid
'''

import pywhatkit
import time
# pip3 install pywhatkit

phone = ""

def sendMessageByTime():
	# Send a WhatsApp Message to a Contact at 1:30 PM
	pywhatkit.sendwhatmsg(phone, "َI Love You", 14, 20)
	
def SM_AndClose():
	# Same as above but Closes the Tab in 2 Seconds after Sending the Message
	pywhatkit.sendwhatmsg(phone, "WOW!", 12, 30, 15, True, 2)

def SendImage():
	# Send an Image to a Group with the Caption as Hello
	pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

def SendImageNoCaption():
	# Send an Image to a Contact with the no Caption
	pywhatkit.sendwhats_image(phone, "Images/Hello.png")

def SM_At00():
	# Send a WhatsApp Message to a Group at 12:00 AM
	pywhatkit.sendwhatmsg_to_group("Test py", "Hey All!", 14, 0)

def PlayVideo():
	# Play a Video on YouTube
	pywhatkit.playonyt("PyWhatKit")

if __name__=="__main__":
	CNT = 100
	#minute = time.strftime("%M", time.localtime())
	#Hour = time.strftime("%H", time.localtime())
	
	while CNT>1:
		tt = time.strftime("%I:%M:%S %p", time.localtime())

		CNT -= 1
		text = f" Time: {tt} I Love You!!!"
		minute = int(time.strftime("%M", time.localtime()))
		Hour = int(time.strftime("%H", time.localtime()))
		
		pywhatkit.sendwhatmsg(phone, text, Hour, minute)
		minute +=1