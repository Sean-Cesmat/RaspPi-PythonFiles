import RPi.GPIO as GPIO
import time
import board
import neopixel

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
buttonLoop = 0
modes = 20

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 150

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRBW

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)


def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos*3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos*3)
        g = 0
        b = int(pos*3)
    else:
        pos -= 170
        r = 0
        g = int(pos*3)
        b = int(255 - pos*3)
    return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)


def rainbow(wait):
    for colorValue in range(255):
        for pixelNum in range(num_pixels):
            pixel_index = (pixelNum * 256 // num_pixels) + colorValue
            pixels[pixelNum] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

colors = [(0, 0, 0), (248, 12, 18), (238, 17, 0), (255, 51, 17), (255, 68, 34), (255, 102, 68), (255, 153, 51), (254, 174, 45), (204, 187, 51), (208, 195, 16), (170, 204, 34), (105, 208, 37), (34, 204, 170), (18, 189, 185), (17, 170, 187), (68, 68, 221), (51, 17, 187), (59, 12, 189), (68, 34, 153), rainbow(0.0001)]
def whatColor():
    i = 0
    while i < len(colors):
        if i == len(colors):
            colors[i]
        elif buttonLoop == i:
            pixels.fill(colors[i])
            pixels.show()
        i += 1


def whatMode():
    if buttonLoop == 0:
        pixels.fill((0,0,0,0))
        pixels.show()
    elif buttonLoop == 1:
        rainbow(0.0001)
    elif buttonLoop == 2:
        pixels.fill((255, 255, 255, 255))
        pixels.show()
    elif buttonLoop == 3:
        pixels.fill((141, 0, 114, 0))
        pixels.show()
    elif buttonLoop == 4:
        pixels.fill((168, 0, 87, 0))
        pixels.show()
    elif buttonLoop == 5:
        pixels.fill((192, 0, 63, 0))
        pixels.show()
    elif buttonLoop == 6:
        pixels.fill((219, 0, 36, 0))
        pixels.show()
    elif buttonLoop == 7:
        pixels.fill((243, 0, 12, 0))
        pixels.show()
    elif buttonLoop == 8:
        pixels.fill((240, 15, 0, 0))
        pixels.show()
    elif buttonLoop == 9:
        pixels.fill((216, 39, 0, 0))
        pixels.show()
    elif buttonLoop == 10:
        pixels.fill((189, 66, 0, 0))
        pixels.show()
    elif buttonLoop == 11:
        pixels.fill((165, 90, 0, 0))
        pixels.show()
    elif buttonLoop == 12:
        pixels.fill((138, 117, 0, 0))
        pixels.show()
    elif buttonLoop == 13:
        pixels.fill((114, 141, 0, 0))
        pixels.show()
    elif buttonLoop == 14:
        pixels.fill((87, 168, 0, 0))
        pixels.show()
    elif buttonLoop == 15:
        pixels.fill((63, 192, 0, 0))
        pixels.show()
    elif buttonLoop == 16:
        pixels.fill((36, 219, 0, 0))
        pixels.show()
    elif buttonLoop == 17:
        pixels.fill((12, 243, 0, 0))
        pixels.show()
    elif buttonLoop == 18:
        pixels.fill((0, 243, 12, 0))
        pixels.show()
    elif buttonLoop == 19:
        pixels.fill((0, 216, 39, 0))
        pixels.show()
    elif buttonLoop == 20:
        pixels.fill((0, 192, 0, 0))
        pixels.show()

while True:
    input_state12 = GPIO.input(12)
    input_state = GPIO.input(23)
    input_state2 = GPIO.input(24)
    if input_state == False:
        print('FButton Pressed')
        buttonLoop = buttonLoop + 1
        time.sleep(0.5)
        whatColor()
        print(buttonLoop)
    if input_state2 == False:
        print('BButton Pressed')
        buttonLoop = buttonLoop - 1
        if buttonLoop < 0:
            buttonLoop = modes
        time.sleep(0.5)
        whatColor()
        print(buttonLoop)
    if input_state12 == False:
        print('Off Button Pressed')
        time.sleep(0.5)
        buttonLoop = 0
        whatColor()
        print(buttonLoop)
    if buttonLoop == (modes + 1):
        buttonLoop = 0
        whatColor()
        print(buttonLoop)