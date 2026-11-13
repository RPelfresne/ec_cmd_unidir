radio.onReceivedString(function (receivedString) {
    msg = receivedString
    if (msg_lu == "B") {
        msg = "BS"
    }
})
let PauseAlea = 0
let msg = ""
let msg_lu = ""
msg_lu = ""
msg = ""
let index2 = 0
let index3 = 0
let index4 = 0
radio.setGroup(1)
radio.setTransmitPower(7)
let nbLeds = 130
let strip = neopixel.create(DigitalPin.P1, nbLeds, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
strip.setBrightness(40)
strip.show()
let dureeMontee = 30000
let montee_1 = 27
let montee_1_1 = 60
let montee_1bis = 5
let descente_1 = 16
let montee_2 = 54
let pauseEntreLeds = dureeMontee / nbLeds
basic.forever(function () {
    msg_lu = msg
    if (msg_lu == "B") {
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        strip.show()
        for (let index = 0; index < montee_1; index++) {
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Blue))
            strip.show()
            basic.pause(randint(200, 450))
            strip.shift(1)
        }
        index2 = 0
        while (index2 < montee_1_1) {
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Blue))
            strip.show()
            basic.pause(randint(50, 150))
            strip.shift(1)
            index2 = index2 + 1
        }
        index3 = 0
        while (index3 < montee_1bis) {
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Blue))
            strip.show()
            basic.pause(randint(1000, 2500))
            strip.shift(1)
            index3 += 1
        }
        strip.shift(-1)
        index4 = 0
        while (index4 <= descente_1) {
            strip.setPixelColor(100, neopixel.colors(NeoPixelColors.Black))
            basic.pause(randint(500, 1500))
            strip.show()
            strip.shift(-1)
            index4 += 1
        }
        strip.shift(1)
        basic.pause(200)
        for (let index5 = 0; index5 <= montee_2; index5++) {
            strip.setPixelColor(0, neopixel.colors(NeoPixelColors.Blue))
            strip.show()
            basic.pause(randint(100, 250))
            strip.shift(1)
        }
    } else if (msg_lu == "R") {
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        strip.show()
    } else if (msg_lu == "S") {
        index2 = 0
        while (index2 < 3) {
            PauseAlea = randint(20, 200)
            strip.setBrightness(PauseAlea)
            PauseAlea = randint(50, 100)
            strip.showColor(neopixel.colors(NeoPixelColors.White))
            basic.pause(PauseAlea)
            strip.showColor(neopixel.colors(NeoPixelColors.Black))
            PauseAlea = randint(100, 500)
            basic.pause(PauseAlea)
            index2 += 1
        }
    } else if (msg_lu == "A") {
        strip.showColor(neopixel.colors(NeoPixelColors.Black))
        strip.show()
        basic.pause(2000)
    } else if (msg_lu == "BS") {
        PauseAlea = randint(10, 100)
        strip.setBrightness(PauseAlea)
        PauseAlea = randint(50, 100)
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        basic.pause(PauseAlea)
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        PauseAlea = randint(100, 500)
        basic.pause(PauseAlea)
        index2 += 1
    } else {
    	
    }
})
