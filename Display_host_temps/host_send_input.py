import serial
import time
import psutil

cpu_temps_list = []
# open a serial connection
def get_cpu_temps():
    cpu_temps_list.clear()
    cpu_temp = psutil.sensors_temperatures()['k10temp']
    for temp_types in cpu_temp:
        for value, temps in enumerate(temp_types):
            #print(value, temps)
            cpu_temps_list.append(temps)
            if value >= 1:
                break
    # print(str(cpu_temps_list))
    return str(cpu_temps_list)
        
    




s = serial.Serial("/dev/ttyACM0", 115200)

# blink the led

while True:
    s.write(get_cpu_temps().encode('utf-8'))
    s.write(b'\n')
    time.sleep(1)
