from abc import abstractmethod


class Iphone:
    @abstractmethod
    def getHardware(self) -> None:
        pass

    def assemble(self) -> None:
        print("Assembling all the hardwares")

    def certificates(self) -> None:
        print("Testing all the certificates")

    def pack(self) -> None:
        print("Packing the device")
