import RPi.GPIO as GPIO
import spidev

water_level = 0

global case
case=None


def waterlevelmeasure(lock):
    
    global case
    
    spi = spidev.SpiDev()
    spi.open(0,0)

    data = 0
    adc = spi.xfer2([1, (8 + water_level) << 4, 0])
    data=((adc[1] & 3) << 8) + adc[2]
    
    print(data)
    
    with lock:
        if data > 10000:  # Check water level against high threshold
            case = 1  # High water level condition
        elif data > 5000 and data <= 10000:  # Check water level against medium threshold
            case = 2  # Medium water level condition
        else :  # Check water level against low threshold
            case = 3  # Low water level condition