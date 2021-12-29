%serialconnect to --port=/dev/ttyUSB2 --baud=115200

from machine import Pin # para usar o pino
from time import sleep # vai funcionar com um delay

ledBlue = Pin(0, Pin.OUT) # led azul

# ascender
# ledBlue.value(1)
ledBlue.on()

# apagar
# ledBlue.value(0)
ledBlue.off()

# vamos fazer um for?
for i in range(20):
    ledBlue.on()
    print("Led ligado")
    sleep(1)
    ledBlue.off()
    print("Led desligado")
    sleep(1)

# criando uma função BlinkOnce
# status variável para saber se
# o led liga ou desliga
def ledBlinkOnce(status):
    
    if(status): 
        ledBlue.on()
    else:
        ledBlue.off()

# criando uma função BlinkLoop
# number -> número de vezes que o led irá piscar
def ledBlinkLoop(number):
    
    for i in range(number):
        ledBlinkOnce(True)
        print("Led ligado")
        sleep(1)
        ledBlinkOnce(False)
        print("Led desligado")
        sleep(1)

ledBlinkLoop(4)


