from temp import read_thermometer
import numpy as np
from machine import ADC

class Kettle:

    def __init__(self) -> None:

        self.temperature = 0
        self.goal_temperature = 0
        self.thermometer_history = np.array([])
        
        self.physical_thermometer = ADC(28)
    
    def set_goal(self, goal_temperature) -> None:
        '''
        Args:
            goal_temperature <int64>

        Updates goal temperature specified by user input
        '''
        self.goal_temperature = goal_temperature

    def update_temperature(self) -> None:
        '''
        Updates temperature as an average of the 20 last thermometer readings
        '''
        self.temperature = np.sum(self.thermometer_history[-20:])/20 
    
    def read_thermometer(self) -> None:
        '''
        Reads thermometer voltage and converts to degrees.
        Adds this value to thermometer history.
        Should run as often as possible.
        '''
        conversion_factor = 3.3/65535
        voltage = self.physical_thermometer.read_u16()*conversion_factor
        self.thermometer_history = np.append(self.thermometer_history, voltage*100)