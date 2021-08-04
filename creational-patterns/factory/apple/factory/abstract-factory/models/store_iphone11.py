from abc import abstractmethod, ABCMeta
from models.store import Store
from models.iphone import Iphone
from models.iphone_11 import Iphone11
from factory.iphone11_hardware_factory import Iphone11HardwareFactory


class StoreIphone11(Store):

    def __init__(self, hardware_factory: Iphone11HardwareFactory) -> None:
        super().__init__()
        self.hardware_factory = hardware_factory

    def orderIphone(self) -> Iphone:
        self.device = Iphone11(self.hardware_factory)
        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device
