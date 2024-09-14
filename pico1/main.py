from machine import Pin, PWM
from pid import PID
from kettle import Kettle
import time

def init():
    global pid
    global kettle
    pid = PID(setpoint=0, sample_time_ms=10000)
    kettle = Kettle(physical_output_pin='LED')

def loop():
    pid.set_setpoint(30)
    while 1:
        if kettle.update_temperature():
            pid.update(kettle.temperature)
            kettle.set_power_level(pid.output)
   


def main():
    init()
    loop()
    return 1

if __name__ == "__main__":  
    main()