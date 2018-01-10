# ---------------------------------------------------------------------
# Last Modified:
#   8-1-2018
# Description:
#   This program is the camera master. It responds to a pushbutton input
#   to start and stop camera recording.
# ---------------------------------------------------------------------

import subprocess
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

convert = False
rec_num = 0
recording = 0

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("")
    while True:
        print("Ready!\n")
	while True:
            button_state = GPIO.input(24)
            if button_state == False:
                print("Starting Camera Recording...\n")
                recording = 1
                break
            sleep(0.2)

        p1 = subprocess.Popen(["python", "/home/pi/Documents/MHP_raspicam/Camera/Camera.py"])
        sleep(1)

        while True:
            button_state = GPIO.input(24)
            if button_state == False:
                print("\nStopping Camera Recording...\n\n")
                subprocess.Popen.kill(p1)
                recording = 0
		if convert == True:
			subprocess.call(["bash","/home/pi/Documents/MHP_raspicam/Camera/convert.sh",str(rec_num)])
                	rec_num = rec_num + 1
			print("")
		print("Wait....\n")
		sleep(1)
                break
            sleep(0.2)
except KeyboardInterrupt:
    if recording == 1:
        subprocess.Popen.kill(p1)
    print("\n\nProgram Ended.\n")
    GPIO.cleanup()