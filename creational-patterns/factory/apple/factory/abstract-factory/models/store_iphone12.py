from abc import abstractmethod, ABCMeta
from models.store import Store
from models.iphone import Iphone
from models.iphone_12 import Iphone12
from factory.iphone12_hardware_factory import Iphone12HardwareFactory


class StoreIphone12(Store):

    def __init__(self, hardware_factory: Iphone12HardwareFactory) -> None:
        super().__init__()
        self.hardware_factory = hardware_factory

    def orderIphone(self) -> Iphone:
        self.device = Iphone12(self.hardware_factory)
        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device
