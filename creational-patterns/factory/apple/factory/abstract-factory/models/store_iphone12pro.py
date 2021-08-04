from abc import abstractmethod, ABCMeta
from models.store import Store
from models.iphone import Iphone
from models.iphone_12_pro import Iphone12Pro
from factory.iphone12pro_hardware_factory import Iphone12ProHardwareFactory


class StoreIphone12Pro(Store):

    def __init__(self, hardware_factory: Iphone12ProHardwareFactory) -> None:
        super().__init__()
        self.hardware_factory = hardware_factory

    def orderIphone(self) -> Iphone:
        self.device = Iphone12Pro(self.hardware_factory)
        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device
