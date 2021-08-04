from abc import abstractmethod, ABCMeta
from models.iphone import Iphone


class Store(metaclass=ABCMeta):
    @abstractmethod
    def orderIphone() -> None:
        pass
