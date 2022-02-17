# Temp.py

from ds18b20 import DS18B20	
	
# test temperature sensors
while True:
	x = DS18B20()
	count=x.device_count()
	i = 0
	while i < count:
		print("Sensor Suhu Ke: ",i," Suhu: ",x.tempC(i))
		i += 1
