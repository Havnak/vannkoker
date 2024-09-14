# Temperature controlled kettle 
### --- WIP ---
I am modifying a Wilfa Rapid kettle to be temperature controlled.

### Base idea
To do this, I'm using two Raspberry Pi Pico W (Pico) microcontrollers I had lying around.
Pico 1 is in the base of the kettle. This is the main microcontroller. It runs the control program, and drives the user interface (UI).
Pico 2 is in the handle of the kettle. This microcontroller sends temperature readings to Pico 1 over WiFi. Very overkill for the task.

The actuator is a solid state relay (SSR), which controls the wattage of the element through PWM. Because of the thermal mass of the kettle and heating element, this is equivalent to power regulation with voltage.
Because the actuator will turn off and on the electricity supply, Pico 2 will lose power often. To combat this, I'm using a 1F supercapacitor with low ESR. 

To supply each of the Picos, I'm using phone chargers from IKEA. They are pretty cheap, and I believe they are safer than if I made voltage regulators myself. 

The UI and SSR don't fit the original base, so I modified the base with 3D-printed parts. I'm also planning to attach the base to a plate of aluminium to act as a heat sink for the SSR and give some structure and weight to the base. 

### Improvements
Because the Picos are overkill, I want to host a website with stats for the kettle, just for fun:) 
This can enable me to save lots of data from the kettle to my main computer, so that I in the future can use machine learning to for example predict time left, or improve the control algorithm.
