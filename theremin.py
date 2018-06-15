from microbit import *
import music

speed = 300

while True:
    if button_a.was_pressed():
        speed -= 100
        if speed == 0:
            speed = 100
        display.show(str(speed // 100 - 1))
    if button_b.was_pressed():
        speed += 100
        if speed == 1100:
            speed = 1000
        display.show(str(speed // 100 - 1))
    music.pitch(compass.get_field_strength() // 1024)
    sleep(speed)