import serial
import logging
import re
import time
import sys
import codecs


ENCODE = "utf-8"
CMD_LEN = 1024


class excuting:
    def __init__(
        self,
        portName="",
        baudRate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        timeout=5,
    ):
        self.portName = portName
        self.baudRate = baudRate
        self.bytesize = bytesize
        self.parity = parity
        self.stopbits = stopbits
        self.timeout = timeout

    def openComPort(self):
        try:
            self.ser = serial.Serial(
                self.portName,
                self.baudRate,
                timeout=self.timeout,
                bytesize=self.bytesize,
                parity=self.parity,
                stopbits=self.stopbits,
            )
            time.sleep(0.5)
            return True
        except Exception as e:
            print(e)
            self.portName = str(self.portName)
            logging.error("Couldn't open desired tty port: " + self.portName)
            return False

    def closeComPort(self):
        try:
            self.ser.close()
            print("port closed")
        except Exception as e:
            logging.error("port already open (or) Couldn't close tty port")
            print(e)
            sys.exit()

    def sendAtCommand(self, command):
        self.command = command
        command = (command + "\r").encode()
        try:
            self.ser.write(command)
            received = self.ser.read(1024).decode()
            logging.debug(received)
            if "ERROR" in received:
                return False
            return received
        except Exception as e:
            print(e)
            print("Couldn't write on " + self.portName)
            return False

    def checkCommunication(self):
        if not self.sendAtCommand("AT"):
            logging.error("not success")
            return False
        return True

    def verbose(self):
        cm = self.sendAtCommand("AT+CMEE=2")
        print(cm)
        if cm == logging.error:
            print(cm)
            print("AT+CMEE=2 not success")
            return False
        return True

    def checkpin(self):
        if not self.sendAtCommand("AT+CPIN?"):
            logging.error("check sim")
            return False
        else:
            return True

    def checksignal(self):
        signal = self.sendAtCommand("AT+CSQ")
        signal = signal.split(",")[0]
        if signal == logging.error:
            return False
        else:
            return signal

    def checkimei(self):
        num = ""
        imei = self.sendAtCommand('AT+GSN')
        if imei == logging.error:
            return False
        else:
            for i in range(len(imei)):
                if (imei[i].isdigit()):
                    num = num+imei[i]
        return num

    def checkphone(self):
        num = ""
        phone = self.sendAtCommand('AT+CNUM')
        if phone =="ERROR":
            return False
        else:
            return num

    def mulsim(self, a):
        print(a)
        try:
            musim = self.sendAtCommand('SIM#'+a)
            print(musim)
            if musim == logging.error:
                print("change error")
                return False
            return True
        except Exception as e:
            print(e)

    def sendSms(self, number, message):
        try:
            number = number
        except Exception as e:
            logging.error("Error: " + str(e))
            return False
        try:
            message = message
        except Exception as e:
            logging.error("Error: " + str(e))
            return False

        try:
            print("\n\r...sending SMS")
            print("the sec", self.portName)
            if not self.sendAtCommand("AT+CMGF=1"):
                logging.error("To send AT command: AT+CMGF=1")
                return False
            if not self.sendAtCommand('AT+CMGS="' + number + '"'):
                logging.error("To send AT command: AT+CMGS=")
                return False
            if not self.sendAtCommand(message):
                logging.error("error in msg")
                return False
            if not self.sendAtCommand('\x1A'):
                logging.error("error in exit")
                return False
            else:
                return True
        except Exception as e:
            print(e)

    def readsms(self):
        read = self.sendAtCommand('AT+CMGL="ALL"')
        if read == logging.error:
            return False
        return read


# enable the USSD
# if not self.sendAtCommand('AT+CUSD=1'):
#     logging.error("To send AT command: AT+CUSD=1)")
#     return False

# check the balance using USSD
# if not self.sendAtCommand('AT+CUSD=1,”*123#”,15'):
#     logging.error("To send AT command: AT+CUSD=1,”*123#”)")
#     return False
