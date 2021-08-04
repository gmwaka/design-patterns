from abc import abstractmethod, ABCMeta


class Iphone(metaclass=ABCMeta):
    model: str
    chip: str
    display: str
    camera: str

    @abstractmethod
    def getHardware(self) -> None:
        pass

    def assemble(self) -> None:
        print("Assembling all the hardwares")

    def certificates(self) -> None:
        print("Testing all the certificates")

    def pack(self) -> None:
        print("Packing the device")

    def __str__(self) -> str:
        return " Model: " + self.model
