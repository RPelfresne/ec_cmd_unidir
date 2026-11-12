def on_received_string(receivedString):
    if receivedString == "B":
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
        while index2 < montee_1_1:
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
            strip.show()
            basic.pause(randint(1000, 2500))
            strip.shift(1)
            index2 += 1
        strip.shift(-1)
        for index4 in range(descente_1):
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
            strip.show()
            basic.pause(randint(500, 1500))
            strip.shift(1)
            index4 += 1
            strip.shift(-1)
        strip.shift(1)
        basic.pause(200)
        for index5 in range(montee_2):
            strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
            strip.show()
            basic.pause(randint(100, 250))
            strip.shift(1)
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLUE))
        strip.show()
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
    elif receivedString == "R":
        basic.show_string("Rouge")
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.RED))
        strip.show()
    elif receivedString == "S":
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
    elif receivedString == "A":
        basic.show_string("Arret")
        strip.set_pixel_color(0, neopixel.colors(NeoPixelColors.BLACK))
        strip.show()
        basic.pause(2000)
    else:
        pass
        
radio.on_received_string(on_received_string)

strip: neopixel.Strip = None
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
    pass
basic.forever(on_forever)
