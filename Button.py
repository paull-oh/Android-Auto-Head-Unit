

import RPi.GPIO as GPIO
import time
import subprocess, os
import signal
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
RearView_Switch = 14 
Brightness_Switch = 15
GPIO.setup(RearView_Switch,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(Brightness_Switch,GPIO.IN, pull_up_down=GPIO.PUD_UP)

print "  Press Ctrl & C to Quit"

try:
    
   push = 0
   level = 0
   while True :
      	time.sleep(0.1)
	#different camera angles
      	if GPIO.input(RearView_Switch)==0 and run == 0:
         	print "  Started Full Screen"
         	rpistr = "raspivid -t 0 -vf -h 480 -w 800"
         	p=subprocess.Popen(rpistr,shell=True, preexec_fn=os.setsid)
         	run = 1
         	while GPIO.input(RearView_Switch)==0:
             		time.sleep(0.1)

      	if GPIO.input(RearView_Switch)==0 and push == 1:
         	os.killpg(p.pid, signal.SIGTERM)
		print "  Started Full Screen Transparent"
         	rpistr = "raspivid -t 0 -vf -op 128 -h 480 -w 800"
         	p=subprocess.Popen(rpistr,shell=True, preexec_fn=os.setsid)
         	run = 2
         	while GPIO.input(RearView_Switch)==0:
             		time.sleep(0.1)

      	if GPIO.input(RearView_Switch)==0 and push == 2:
         	os.killpg(p.pid, signal.SIGTERM)
		print "  Started PIP Right side"
         	rpistr = "raspivid -t 0 -vf -p 350,1,480,320"
         	p=subprocess.Popen(rpistr,shell=True, preexec_fn=os.setsid)
         	run = push
         	while GPIO.input(RearView_Switch)==0:
             		time.sleep(0.1)

      	if GPIO.input(RearView_Switch)==0 and push == 3:
         	print "  Stopped " 
         	push = 0
         	os.killpg(p.pid, signal.SIGTERM)
         	while GPIO.input(RearView_Switch)==0:
            		time.sleep(0.1)

	#Brightness settings
      	if GPIO.input(Brightness_Switch)==0 and level == 0:
         	#os.killpg(p.pid, signal.SIGTERM)
		print "Setting Brightness to high"
         	subprocess.call ("/usr/local/bin/backlight.sh 255", shell=True)
         	#p=subprocess.Popen(rpistr,shell=True, preexec_fn=os.setsid)
         	level = 1
         	while GPIO.input(Brightness_Switch)==0:
             		time.sleep(0.1)

      	if GPIO.input(Brightness_Switch)==0 and level == 1:
         	#os.killpg(p.pid, signal.SIGTERM)
		print "Setting Brightness to low"
         	subprocess.call ("/usr/local/bin/backlight.sh 128", shell=True)
         	#p=subprocess.Popen(rpistr,shell=True, preexec_fn=os.setsid)
         	bright = 2
         	while GPIO.input(Brightness_Switch)==0:
             		time.sleep(0.1)

      	if GPIO.input(Brightness_Switch)==0 and level == 2:
         	#os.killpg(p.pid, signal.SIGTERM)
		print "Setting Brightness to 20"
         	subprocess.call ("/usr/local/bin/backlight.sh 20", shell=True)
         	#p=subprocess.Popen(rpistr,shell=True, preexec_fn=os.setsid)
         	level = 0
         	while GPIO.input(Brightness_Switch)==0:
             		time.sleep(0.1)

       
	
except KeyboardInterrupt:
  print "  Quit"
  GPIO.cleanup() 
