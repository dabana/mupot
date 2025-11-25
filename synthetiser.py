from microbit import *
import speech
import music
import math

def mapInteger(anInteger, from1, to1, from2, to2):
    span1 = to1 - from1a
    span2 = to2 - from2
    scaling_factor = span1 / span2
    return math.floor(anInteger / scaling_factor)

display.show(Image.HAPPY)
while True:
    while button_a.is_pressed():
        pin0.set_analog_period_microseconds(256)
        pin2value = mapInteger(pin2.read_analog(), 0, 1023, 100, 1000)
        pin1value = mapInteger(pin1.read_analog(), 0, 1023, 25, 250)
        music.pitch(pin2value, pin1value)
        sleep(pin1value)
    while button_b.is_pressed():
        pin2value = pin2.read_analog()
        pin2value = math.floor(pin2value / 4)
        pin1value = pin1.read_analog()
        pin1value = math.floor(pin1value / 4)
        string = speech.translate("Sup Paputo!")
        speech.pronounce(string,speed=120, pitch=pin2value, throat=100, mouth=pin1value)