from abc import abstractmethod, ABCMeta
from models.store import Store
from models.iphone import Iphone
from models.iphone_11_pro import Iphone11Pro
from factory.iphone11pro_hardware_factory import Iphone11ProHardwareFactory


class StoreIphone11Pro(Store):

    def __init__(self, hardware_factory: Iphone11ProHardwareFactory) -> None:
        super().__init__()
        self.hardware_factory = hardware_factory

    def orderIphone(self) -> Iphone:
        self.device = Iphone11Pro(self.hardware_factory)
        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device
