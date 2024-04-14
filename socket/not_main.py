from machine import ADC, Pin
import network
import random
import socket
import time
import constants


led = Pin('LED', Pin.OUT)
led.high()

ssid = constants.ssid
pw = constants.password

# Setting up access point
ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=pw)
ap.active(True)


# Wait for connect
while not ap.active():
  pass
print('Access point active')
# Open socket
addr = '192.168.4.1'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((addr, 1234))
s.listen(5)

# Listen for connections


while True:
    try:
        cl, addr = s.accept()
        # request = cl.recv(1024)
        # print(request)
        # No need to unpack request in this example
        for _ in range(20):
          ran_num = str(random.randint(0, 100))
          cl.send(bytes(ran_num+'\n', 'utf-8'))
          print("Sent: " + ran_num)
          time.sleep(1)
        # cl.close()

    except OSError as e:
        cl.close()
        print('connection closed')