from .iphone import Iphone
from factory.iphone11_hardware_factory import Iphone11HardwareFactory


class Iphone11(Iphone):

    def __init__(self, hardware_factory: Iphone11HardwareFactory) -> None:
        super().__init__()
        self.hardware_factory = hardware_factory

    def getHardware(self) -> None:
        super().getHardware()
        print("Hardware list")
        self.model = self.hardware_factory.createModel()
        self.camera = self.hardware_factory.createCamera()
        self.chip = self.hardware_factory.createChip()
        self.display = self.hardware_factory.createDisplay()
