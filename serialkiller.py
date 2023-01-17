import serial
import sys

print("Usage: python3 serialkilla.py url serialport")
# configure the remote serial port
ser = serial.Serial(
    port=str(sys.argv[2]),
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1,
    #remote server address
    url=str(sys.argv[1])
)

def request_data():
    # send the request over the serial line
    ser.write(b'request_all_data\n')
    # read the response from the serial line
    response = ser.readline()
    return response

# call the request_data function
data = request_data()

# print the received data
print(data.decode())

# close the serial port
ser.close()
