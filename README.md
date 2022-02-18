# ds18b20
Setup many ds18b20

## 1. DS18B20 Schematic
![image](https://user-images.githubusercontent.com/86288255/154648619-e5ede45c-2ee6-4b96-af3c-cb37f90e9d65.png)

## 2. Setup Raspberry Pi
`sudo nano /boot/config.txt`

Add the following line 

Default pin GPIO4:
```dtoverlay=w1-gpio```

Custom pin GPIO:
```dtoverlay=w1-gpio,gpiopin=x```
Change `x` to custom pin GPIO

## 3. Clone this program to some directory
`git clone https://github.com/renaldyks/ds18b20.git`

## 4. Run app.py
`sudo python3 app.py`
