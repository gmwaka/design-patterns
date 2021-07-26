from abc import abstractmethod, ABCMeta
from models.iphone import Iphone


class Store(metaclass=ABCMeta):
    def orderIphone(self, model: str) -> Iphone:
        self.device = self.createIphone(model)
        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device

    # This is the factory method
    @abstractmethod
    def createIphone(self, model: str) -> None:
        pass
