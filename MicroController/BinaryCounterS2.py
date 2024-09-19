from gpiozero import LED
from time import sleep

#      BCM Schema   Physcal Pin
LED0 = LED(17)      # 11
LED1 = LED(18)      # 12
LED2 = LED(27)      # 13
LED3 = LED(22)      # 15
LED4 = LED(23)      # 16
LEDArray = [LED0, LED1, LED2, LED3, LED4]
Decimal = 0
IntervalSeconds = 1

# LOOP
# Counter = 9
# i = 4 : [(9 >> 4) & 1] 
# i = 3 : [(9 >> 3) & 1]
# i = 2 : [(9 >> 2) & 1]
# i = 1 : [(9 >> 1) & 1]
# i = 0 : [(9 >> 2) & 1]
# Counter = 10...

def count():
    print("Run")
    global Decimal
    while Decimal < 32:
                                              # Decrementing loop starts at 4 (first bit in array (least sigfig))
        BitArray = [(Decimal >> i) & 1 for i in range(4, -1, -1)]
        for element in BitArray:
            if BitArray[element] == 1 :
                LEDArray[element] = 1
            else : LEDArray[element] = 0
        Decimal += 1
        sleep(IntervalSeconds) 
count()



