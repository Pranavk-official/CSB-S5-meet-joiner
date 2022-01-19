import webbrowser #openwebbrowser
from datetime import datetime
import time
import pyautogui #controls keyboard and mouse


#Out of class hours- code---------------------------------------------------------------------

def noclasstime():
	now=datetime.now()
	if now.strftime("%H%M%S")<"085500" or now.strftime("%H%M%S")>"120000":
		print("There are no class at this time. Please start the bot after 08:55 AM")
		time.sleep(5)
		quit()


#Out of class code end-------------------------------------------------------------------------

#Idle time code-------------------------------------------------------------------------

def idletime():
	join() #Supposed to be after meet links! But this serves the purpose!
	print("Program going idle until next class")
	time.sleep(2640)
	print("This class has ended checking for availability of next class")
	lineseprator()
	return


#Print Line to seprate code-------------------------------------------------------------------------
def lineseprator():
	print("------------------------------------------------------------------")

#Print Line to seprate code-------------------------------------------------------------------------
def endclass():
	print("Classes have ended for today.Have a good day")
	quit()

# Join Class Code-------------------------------------------------------------------------

def join():
	time.sleep(10)
	pyautogui.hotkey('ctrl','d') #mutes mic
	pyautogui.hotkey('ctrl','e') #Camera Off
	joinnowbutton()#Activates and Clicks the join now button.joinnowbutton() function is below this

def joinnowbutton():
    time.sleep(2)   
    pyautogui.hotkey('ctrl','shift','j')
    time.sleep(2)
    classid='document.getElementsByClassName("l4V7wb Fxmcue")[0].click()'	
    pyautogui.write(classid)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('ctrl','shift','j')

# SUbjects and Subject Code-------------------------------------------------------------------

# '''
# ss      dur-ogbt-zdy
# flat    pfs-cpqc-fmq
# cn      mwz-acxx-apm
# mm      dqp-muhy-fde
# mss     isf-nnjj-joj
# dm      nec-ycwt-ymn
# '''

def ss():
	linkco="https://meet.google.com/lookup/dur-ogbt-zdy?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering System Software By Sajitha Ma'am")
	idletime()

def flat():
	linkco="https://meet.google.com/lookup/pfs-cpqc-fmq?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Formal Languages and Automata Theory By Reshma Ma'am")
	idletime()

def cn():
	linkco="https://meet.google.com/lookup/mwz-acxx-apm?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Computer Networks By Thomas Sir")
	idletime()

def mm():
	linkco="https://meet.google.com/lookup/dqp-muhy-fde?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Microprocessors And Microcontrollers By Aswathy Ma'am")
	idletime()

def mss():
	linkco="https://meet.google.com/lookup/isf-nnjj-joj?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Management of Syste, By Lufiya Ma'am")
	idletime()

def dm():
	linkco="https://meet.google.com/lookup/nec-ycwt-ymn?authuser="+str(authuser)
	webbrowser.open_new(linkco)
	print("Entering Management of Syste, By Kastro Sir")
	idletime()


#The time function in timetable---------------------------------------
def classtime(hr1,hr2,hr3,hr4):
	now=datetime.now()
	noclasstime()
	if "085501"<now.strftime("%H%M%S")<"125000":
		while True:
			now=datetime.now()
			#hour1
			if "090000"<=now.strftime("%H%M%S")<"090500":
				#print(datetime.today().weekday()+" - Hour 1")
				hr1()
			#hour2
			if "100000"<=now.strftime("%H%M%S")<"100500":
				#print(datetime.today().weekday()+" - Hour 2")
				hr2()
			#break
			if now.strftime("%H%M%S")=="095000" or now.strftime("%H%M%S")=="105000" or now.strftime("%H%M%S")=="115000" or now.strftime("%H%M%S")=="125000":
				print("Break for 10 min - Program idle for 10 minutes")
				print("Do not turn off the PC , if turning off, restart the program before next class")
				time.sleep(500)
			#hour3
			if "110000"<=now.strftime("%H%M%S")<"110500":
				#print(datetime.today().weekday()+" - Hour 3")
				hr3()
			#hour4
			if "120000"<=now.strftime("%H%M%S")<"120500":
				#print(datetime.today().weekday()+" - Hour 4")
				hr4()
				endclass()


# Driver programming checking time and joining class--------------------------------------	

def timetable():
	

#Monday-----------------------------------------------------------

	if(datetime.today().weekday()==0):
		classtime(cn,ss,dm,flat)

#Tuesday-----------------------------------------------------------

	if(datetime.today().weekday()==1):
		classtime(ss,cn,flat,mm)

#Wednesday-----------------------------------------------------------

	if(datetime.today().weekday()==2):
		classtime(mm,flat,cn,lab)

#Thursday-----------------------------------------------------------

	if(datetime.today().weekday()==3):
		classtime(ss,cn,mss,flat)

#Friday-----------------------------------------------------------

	if(datetime.today().weekday()==4):
		classtime(flat,cn,ss,mm)
#Saturday and Sunday----------------------------------------------
	else:
		print("No Classes on Saturday and Sunday")
		quit()



# Bot Banner
if __name__ == "__main__":
	print("""
  ╔═╗╔═╗╔═╗  ╔╗            
  ║  ╚═╗║╣   ╠╩╗   |S|5|         
  ╚═╝╚═╝╚═╝  ╚═╝                    
  ╔╦╗┌─┐┌─┐┌┬┐  ╔╗ ┌─┐┌┬┐  
  ║║║├┤ ├┤  │   ╠╩╗│ │ │   
  ╩ ╩└─┘└─┘ ┴   ╚═╝└─┘ ┴            
                                                                
 Dev : "https://github.com/Pranavk-official"
 Starting the bot.............. 

 ***********************************************
 This BOT is created for S5 CSB Students - JECC
 ***********************************************   
    
 Instructions
 -------------
 1. If you see multiple error messages during the bot's operation , Dont worry the bot is working fine. Bug removal is on the way.
 2. Do not engage with the meeet window while joining a new class is in progress :)
          
"""
       )
	authuser = input("Enter Authuser Count : ")  # Authuser Number
	lineseprator()
	print("!!!!!! BOT IS WORKING DO NOT CLOSE THE WINDOW/TERMINAL !!!!!!! ")
	lineseprator()
	meet = timetable()
