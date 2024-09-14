'''
    Kettle class for interacting with kettle
    Copyright (C) 2024  Haavard Nakling

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


from machine import ADC, Pin
import time

class Kettle:
    '''
    member functions:
        set_goal,
        update_temperature,
        read_thermometer
    '''

    def __init__(self, physical_output_pin) -> None:

        self.temperature = self.read_thermometer()
        self.goal_temperature = 0
        self.thermometer_history = []
        self.power_level = 0
        self.delta_t_duty_cycle = 10
        self.time_0_s = time.ticks_ms()*1000
        
        self.physical_thermometer = ADC(28) # TODO
        self.physical_output_pin = Pin(physical_output_pin, Pin.OUT) # TODO
        
    def set_goal(self, goal_temperature) -> None:
        '''
        Args:
            goal_temperature <int64>

        Updates goal temperature specified by user input
        '''
        self.goal_temperature = goal_temperature

    def update_temperature(self) -> bool:
        '''
        Updates temperature as an average of the 20 last thermometer readings
        
        return:
            <bool> 
        '''
        self.read_thermometer()
        if len(self.thermometer_history)>19:
            self.temperature = sum(self.thermometer_history[-20:])/20
            self.thermometer_history = []
            return True
        return False

    def _read_thermometer(self) -> int:
        '''
        Reads thermometer voltage and converts to degrees.
        Adds this value to thermometer history.
        Should run as often as possible.
        '''
        conversion_factor = 3.3/65535
        voltage = self.physical_thermometer.read_u16()*conversion_factor
        self.thermometer_history.append(voltage*100)
        return voltage*100

    def set_power_level(self, power_level_percentage) -> None:
        '''
        Sets output pin high or low depending on power level and time

        Args:
            power_level <int64> : percentage
        '''
        if (self.time_0_s % self.delta_t_duty_cycle) < (power_level_percentage / (100/self.delta_t_duty_cycle)):
            self.physical_output_pin.value(1)
        else:
            self.physical_output_pin.value(0)
