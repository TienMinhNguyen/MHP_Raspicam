# Written by: Minh T Nguyen
# Last modified: 17/7/2018
# Softwares: Python 3.4.2, picamera 1.13, PIL 1.1.7
# Hardwares: Camera Module V2.1, Official 7" touchscreen monitor

# Descriptions: A camera preview with the data overlay of time, speed, heart rate,
# power, cadence and distance. This is a demo therefore only the time is working.
# All other entries are just dummy data and is used for display purpose.

from picamera import PiCamera, Color
from PIL import Image, ImageDraw, ImageFont
from time import sleep
import datetime as dt

# The resolution of the camera preview. Current system using 800x480.
WIDTH = 800
HEIGHT = 480

# Initiate camera preview
camera = PiCamera(resolution=(WIDTH, HEIGHT))
camera.start_preview()

# Create a transparent image to attach text
img = Image.new('RGBA', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

"""
Text display for speed.
"""
# Text height in pixel
speed_height = 50
speed_font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',speed_height)
speed = 'SP: {}'.format(0)
draw.text((WIDTH/2 - 65, HEIGHT-speed_height), speed, font=speed_font, fill='black')
"""
unit_height = 25
unit_font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',unit_height)
unit = ' km/h'
draw.text((WIDTH/2, HEIGHT-unit_height), unit, font=unit_font, fill='black')
"""


"""
Text display for power, cadence (pedalling rate), distance, heart rate. As mentionaed
above, these are dummy text for displaying purpose only.
"""
#display_text = ['Pwr: {} W'.format(0),'Cad: {} rpm'.format(0.0), 'Dist: {} km'.format(0.0), 'Heart rate: {} bpm'.format(0)]
display_text = ['Pwr: {}'.format(0),'Cad: {}'.format(0.0), 'Dist: {}'.format(0.0), 'H/r: {}'.format(0)]
text_height = 20
text_font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSans.ttf',text_height)
for i in range(len(display_text)):
    draw.text((10, 10 + text_height*i), display_text[i], font=text_font, fill='black')


# Add the image to the preview overlay
overlay = camera.add_overlay(img.tostring(), format='rgba', size=img.size)
overlay.layer = 3
overlay.fullscreen = True


"""
Text display for time. "annotate_text" is used instead of "draw.text" because by default,
(1) the text generated by "annotate_text" is centrally aligned in the middle of the screen,
and (2) the text is saved toghether with the recorded video while "draw.text" will not be saved.
"""
camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
camera.annotate_text_size = 26
camera.annotate_foreground = Color('black')

# Update the time after 1 second
while True:
    sleep(1)
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
