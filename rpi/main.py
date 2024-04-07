from machine import Pin, PWM
from time import sleep_us
# import pid

import time

class PID:
    def __init__(self, P=1.0, I=0.0, D=0.0, setpoint=0.0):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.SetPoint = setpoint
        self.sample_time = 0.0
        self.current_time = time.ticks_ms()
        self.last_time = self.current_time
        self.clear()

    def clear(self):
        self.proportional = 0.0
        self.integral = 0.0
        self.derivative = 0.0
        self.last_error = 0.0
        self.output = 0.0

    def update(self, feedback_value):
        error = self.SetPoint - feedback_value
        self.current_time = time.ticks_ms()
        delta_time = self.current_time - self.last_time
        delta_error = error - self.last_error

        if delta_time >= self.sample_time:
            self.integral += error * delta_time
            self.derivative = 0

            if delta_time > 0:
                self.derivative = delta_error / delta_time

            self.last_time = self.current_time
            self.last_error = error
            self.output = (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * self.derivative)

        return self.output

    def set_setpoint(self, setpoint):
        self.SetPoint = setpoint

    def set_sampletime(self, sample_time):
        self.sample_time = sample_time



led = Pin("LED", Pin.OUT)
led_pwm = PWM(Pin(22))

def init():
    led.low()
    led_pwm.freq(8)
    return 0


def loop():
    DUTY_CYCLE = 0
    led_pwm.duty_u16(DUTY_CYCLE)
    pid = PID(1,0,0,50)
    pid.set_sampletime(0.1)
    for i in range(100):
        print(pid.update(i)%65536)

    return 1

def main():
    init()
    loop()
    return 1

main()