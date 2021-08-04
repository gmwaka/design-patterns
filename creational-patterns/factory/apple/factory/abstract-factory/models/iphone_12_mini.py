from .iphone import Iphone
from factory.iphone12mini_hardware_factory import Iphone12MiniHardwareFactory


class Iphone12Mini(Iphone):

    def __init__(self, hardware_factory: Iphone12MiniHardwareFactory) -> None:
        super().__init__()
        self.hardware_factory = hardware_factory

    def getHardware(self) -> None:
        super().getHardware()
        print("Hardware list")
        self.model = self.hardware_factory.createModel()
        self.camera = self.hardware_factory.createCamera()
        self.chip = self.hardware_factory.createChip()
        self.display = self.hardware_factory.createDisplay()
