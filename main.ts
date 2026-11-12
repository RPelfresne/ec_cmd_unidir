radio.onReceivedString(function (receivedString) {
    if (receivedString == "B") {
        basic.showString("montée Bleue")
    } else if (receivedString == "R") {
        basic.showString("Rouge")
    } else if (receivedString == "S") {
        basic.showString("Strobo")
    } else if (receivedString == "A") {
        basic.showString("Arret")
    } else {
    	
    }
})
radio.setGroup(1)
radio.setTransmitPower(7)
basic.forever(function () {
	
})
