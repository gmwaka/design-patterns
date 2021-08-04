from abc import abstractmethod, ABCMeta
from models.store import Store
from models.iphone import Iphone
from models.iphone_12_mini import Iphone12Mini
from factory.iphone12mini_hardware_factory import Iphone12MiniHardwareFactory


class StoreIphone12Mini(Store):

    def __init__(self, hardware_factory: Iphone12MiniHardwareFactory) -> None:
        super().__init__()
        self.hardware_factory = hardware_factory

    def orderIphone(self) -> Iphone:
        self.device = Iphone12Mini(self.hardware_factory)
        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device
