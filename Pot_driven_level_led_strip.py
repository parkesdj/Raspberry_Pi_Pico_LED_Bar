from machine import Pin
from utime import sleep

led7 = machine.Pin((8), Pin.OUT)
led6 = machine.Pin((2), Pin.OUT)
led5 = machine.Pin((3), Pin.OUT)
led4 = machine.Pin((4), Pin.OUT)
led3 = machine.Pin((5), Pin.OUT)
led2 = machine.Pin((6), Pin.OUT)
led1 = machine.Pin((7), Pin.OUT)

pot = machine.ADC(26)

conversion_factor = 3.3 / 65335


delay = 0.2
small_delay = 0.05

leds = [led1, led2, led3, led4, led5, led6, led7]

while True:
    voltage = pot.read_u16() * conversion_factor
    display = int((voltage * 2) +  1)
    print(round(voltage,2),"V","\t",display)
    sleep(0.5)
    for i in range (0, display):
        leds[i].value(1)
        sleep(small_delay)
    sleep(delay)
    for t in range (5, -1, -1):
        leds[t].value(0)
        sleep(small_delay)
    