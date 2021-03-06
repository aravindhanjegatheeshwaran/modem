import serial.tools.list_ports
import sys
import glob
import serial


def check():
    if sys.platform.startswith('win'):
        ports = serial.tools.list_ports.comports()
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    if ports:
        pass
    else:
        print("No ports on your machine")
    for port in ports:
        po = str(port).split(" ")[0]
        result.append(po)
    return result


