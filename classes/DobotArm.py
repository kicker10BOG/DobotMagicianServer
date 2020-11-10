from classes.Position import Position

from devices import device
from serial.tools import list_ports
from .Dobot import Dobot

device = None

class DobotArm:
    def __init__(self):
        pass

    def connect(self):
        port = list_ports.comports()[0].device
        self.device = Dobot(port=port, verbose=False)

    def disconnect(self):
        self.device.disconnect()

    def updateStatus(self):
        pass

    def home(self):
        self.device.home()

    def moveTo(self, position, wait=True): 
        self.device.move_to(position.x, position.y, position.z, position.r, wait=wait)

    def setSpeed(self, velocity, acceleration) :
        self.device.set_speed(velocity=velocity, acceleration=acceleration)

    def speed(self):
        return self.device.get_speed()[0]

    def acceleration(self):
        return self.device.get_speed()[1]