from machine import Pin
from utime import sleep

#Designate Pins
data = Pin(10, Pin.OUT, value=0) #Shiftregister pin 14 SER
clock = Pin(11, Pin.OUT, value=0) #Shiftregister pin 11 SRCLK
latch = Pin(12, Pin.OUT, value=0) #Shiftregister pin 12 RCLK
#Shiftregister pin 10 (SRCLR) to +ve
#Shiftregister pin 13 (OE to Gnd
pot = machine.ADC(26) #10K ohm linear pot wiper on pin 26 of pico

#Assign Variables
conversion_factor = 3.3 / 65335
delay = 0.2
small_delay = 0.05

"""
Voltage     Lit     Value to
Pin 26      LEDs  Shiftregister
===============================
0.0 - 0.5    1     00000001
0.6 - 1.0    2     00000011
1.1 - 1.5    3     00000111
1.6 - 2.0    4     00001111
2.1 - 2.5    5     00011111
2.6 - 3.0    6     00111111
3.1 - 3.5    7     01111111
================================
"""
#Read and round voltage
while True:
    voltage = pot.read_u16() * conversion_factor
    display = int((voltage * 2) +  1)
    print(round(voltage,2),"V","\t",display)
    sleep(0.5)
    
    #Send correct number of 1 bits to shiftregister
    for num in range(0, display):
        data.value(1)
        clock.value(1)
        sleep(0.5)
        clock.value(0)
    latcch.value(1)
    latch.value(0)
    
    #Turn off lit LEDs by sending 8 0 bits to shiftregister
    #Alternatively you could use a Pico pin to Gnd the SRCLR pin on the shiftregister
    for i in range(0, 8 ):
        data.value(0)
        clock.value(1)
        sleep(0.5)
        clock.value(0)
    latch.value(1)
    latch.value(0)
