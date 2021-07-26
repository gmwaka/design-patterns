from models.iphone import Iphone
from factory.iphone_simple_factory import IphoneSimpleFactory


class Store:
    def __init__(self, factory: IphoneSimpleFactory) -> None:
        self.factory = factory

    def orderIphone(self, generation: str, model: str) -> Iphone:
        self.device = self.factory.createIphone(self, generation, model)
        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device
