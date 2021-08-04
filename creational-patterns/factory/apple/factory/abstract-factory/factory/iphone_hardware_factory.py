from abc import abstractmethod, ABCMeta


class IphoneHardwareFactory(metaclass=ABCMeta):
    """Abstract Factory to create a group of products(components)"""

    @abstractmethod
    def createModel() -> None:
        pass

    @abstractmethod
    def createChip() -> None:
        pass

    @abstractmethod
    def createDisplay() -> None:
        pass

    @abstractmethod
    def createCamera() -> None:
        pass
