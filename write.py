import time
import pigpio

txpin=4


pi = pigpio.pi() # Connect to local Pi.

pi.set_mode(txpin, pigpio.OUTPUT)

while pi.wave_tx_busy():
   time.sleep(0.1)

pi.wave_add_serial(txpin, 9600, [23, 128, 234], 0, 9, 1)

pi.stop()