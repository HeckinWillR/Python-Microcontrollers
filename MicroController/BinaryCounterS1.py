from gpiozero import LED
from time import sleep

counter = 0
LED0 = LED(17) #BCM Schema
LED1 = LED(17)
LED2 = LED(17)
LED3 = LED(17)
LED4 = LED(17)

LEDArray = [LED0, LED1, LED2, LED3, LED4]
BitArray = [0, 0, 0, 0, 0]

def count():
    global counter
    global BitArray

    while counter < 32:  
        toAdd = counter
        BitArray = [0, 0, 0, 0, 0]
        if toAdd >= 16 :
            BitArray[0] = 1
            toAdd -= 16
        if toAdd >= 8 :
            BitArray[1] = 1
            toAdd -= 8
        if toAdd >= 4 :
            BitArray[2] = 1
            toAdd -= 4
        if toAdd >= 2 :
            BitArray[3] = 1
            toAdd -= 2
        if toAdd >= 1 :
            BitArray[4] = 1
            toAdd -= 1
        print(f"Counter: {counter}, BitArray: {BitArray}")
        for element in BitArray:
            if BitArray[element] == 1 :
                LEDArray[element] = 1
            else : LEDArray[element] = 0
        counter += 1
        sleep(1)
count()
