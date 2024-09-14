import time

class PID:
    def __init__(self, P=1.0, I=0.0, D=0.0, setpoint=0.0, sample_time_ms = 1000):
        self.Kp = P
        self.Ki = I
        self.Kd = D
        self.SetPoint = setpoint 
        self.sample_time = sample_time_ms
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
            self.output = max(0, (self.Kp * error) + (self.Ki * self.integral) + (self.Kd * self.derivative))

        return self.output

    def set_setpoint(self, setpoint):
        self.SetPoint = setpoint

