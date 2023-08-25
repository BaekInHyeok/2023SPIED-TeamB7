import RPi.GPIO as GPIO
import spidev

water_level = 0 #물높이 센서를 ADC 0번 채널에 연결한다.

global case
case=None


def waterlevelmeasure(lock):
    
    global case
    
    # MCP3208 SPI 버스 및 디바이스 설정
    spi = spidev.SpiDev()
    spi.open(0,0)

    
    # MCP3208에서 아날로그 값을 읽어와 반환
    data = 0
    adc = spi.xfer2([1, (8 + water_level) << 4, 0])
    data=((adc[1] & 3) << 8) + adc[2]
    
    print(data)
    
    with lock:
        if data > high_threshold:  # Check water level against high threshold
            case = 1  # High water level condition
        elif data > medium_threshold and data <= high_threshold:  # Check water level against medium threshold
            case = 2  # Medium water level condition
        else :  # Check water level against low threshold
            case = 3  # Low water level condition