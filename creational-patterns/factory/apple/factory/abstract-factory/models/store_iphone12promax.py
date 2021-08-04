from abc import abstractmethod, ABCMeta
from models.store import Store
from models.iphone import Iphone
from models.iphone_12_pro_max import Iphone12ProMax
from factory.iphone12promax_hardware_factory import Iphone12ProMaxHardwareFactory


class StoreIphone12ProMax(Store):

    def __init__(self, hardware_factory: Iphone12ProMaxHardwareFactory) -> None:
        super().__init__()
        self.hardware_factory = hardware_factory

    def orderIphone(self) -> Iphone:
        self.device = Iphone12ProMax(self.hardware_factory)
        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device
