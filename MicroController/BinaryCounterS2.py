#White  (BROADCOMM 5)  = LED0
#Purple (BROADCOMM 6)  = LED1
#Blue   (BROADCOMM 13) = LED2
#Yellow (BROADCOMM 19) = LED3
#Green  (BROADCOMM 26) = LED4
#Orange (Ground)

from gpiozero import LED
from time import sleep

#      BROADCOMM   BOARD
LED0 = LED(5)       # 29
LED1 = LED(6)       # 31
LED2 = LED(13)      # 33
LED3 = LED(19)      # 35
LED4 = LED(26)      # 37
#GROUND	  	        # 39	
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
        # At "range", decrementing loop starts at 4 least sigfig)
        BitArray = [(Decimal >> i) & 1 for i in range(4, -1, -1)]
        for element in BitArray:
            if BitArray[element] == 1 :
                LEDArray[element] = 1
            else : LEDArray[element] = 0
        Decimal += 1
        sleep(IntervalSeconds) 
count()