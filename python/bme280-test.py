# Source: https://pypi.org/project/RPi.bme280/
#import sys
import platform
import smbus2
import bme280

line = '-' * 70
double_line = '=' * 70

#print(f"Python verion: '{sys.version}'")
print(double_line)
print("== {}: {}".format('Python verion', platform.python_version()))
print(double_line)
print()

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes

print(line)
print(f"-- {data.id}")
print(line)

print("{:16}{}".format('Date and time', data.timestamp))
print("{:16}{:.2f} °C".format('Temperature', data.temperature))
print("{:16}{:.2f} hPa".format('Pressure', data.pressure))
print("{:16}{:.2f}% rH".format('Humidity', data.humidity))
print()

# there is a handy string representation too
#print(data)