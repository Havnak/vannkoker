from machine import ADC
from time import sleep

thermometer = ADC(28)

def read_thermometer():
    conversion_factor = 3.3/65535
    voltage = thermometer.read_u16()*conversion_factor
    return voltage*100

def main():
    for _ in range(20):
        temperature = read_thermometer()
        print(f'Temperaturen er {temperature} grader Celcius, V: {temperature/100}')
        sleep(1)
    return 1

main()