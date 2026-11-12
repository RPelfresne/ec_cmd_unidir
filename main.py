def on_received_string(receivedString):
    global msg
    msg = receivedString
radio.on_received_string(on_received_string)

PauseAlea = 0
msg = ""
msg_lu = ""
msg = ""
index2 = 0
index3 = 0
index4 = 0
radio.set_group(1)
radio.set_transmit_power(7)
nbLeds = 130
strip = neopixel.create(DigitalPin.P1, nbLeds, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
strip.set_brightness(40)
strip.show()
dureeMontee = 30000
montee_1 = 27
montee_1_1 = 60
montee_1bis = 5
descente_1 = 16
montee_2 = 54
pauseEntreLeds = dureeMontee / nbLeds

def on_forever():
    global msg_lu, index2, index3, index4, PauseAlea
    msg_lu = msg
    if msg_lu == "B":
        basic.show_string("montée Bleue")
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        for index in range(montee_1):
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
            strip.show()
            basic.pause(randint(200, 450))
            strip.shift(1)
        index2 = 0
        while index2 < montee_1_1:
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
            strip.show()
            basic.pause(randint(50, 150))
            strip.shift(1)
            index2 = index2 + 1
        index3 = 0
        while index3 < montee_1bis:
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
            strip.show()
            basic.pause(randint(1000, 2500))
            strip.shift(1)
            index3 += 1
        strip.shift(-1)
        index4 = 0
        while index4 <= descente_1:
            strip.set_pixel_color(100, neopixel.colors(NeoPixelColors.BLACK))
            basic.pause(randint(500, 1500))
            strip.show()
            strip.shift(-1)
            index4 += 1
        strip.shift(1)
        basic.pause(200)
        index5 = 0
        while index5 <= montee_2:
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
            strip.show()
            basic.pause(randint(100, 250))
            strip.shift(1)
            index5 += 1
        index2 = 0
        while index2 < 3:
            PauseAlea = randint(10, 100)
            strip.set_brightness(PauseAlea)
            PauseAlea = randint(50, 100)
            strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
            basic.pause(PauseAlea)
            strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
            PauseAlea = randint(100, 500)
            basic.pause(PauseAlea)
            index2 += 1
    elif msg_lu == "R":
        basic.show_string("Rouge")
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        strip.show()
    elif msg_lu == "S":
        basic.show_string("Strobo")
        index2 = 0
        while index2 < 3:
            PauseAlea = randint(20, 200)
            strip.set_brightness(PauseAlea)
            PauseAlea = randint(50, 100)
            strip.show_color(neopixel.colors(NeoPixelColors.WHITE))
            basic.pause(PauseAlea)
            strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
            PauseAlea = randint(100, 500)
            basic.pause(PauseAlea)
            index2 += 1
    elif msg_lu == "A":
        basic.show_string("Arret")
        strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        basic.pause(2000)
basic.forever(on_forever)
