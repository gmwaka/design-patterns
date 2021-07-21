from .iphone import Iphone


class Iphone12Pro(Iphone):

    def getHardware(self) -> None:
        super().getHardware()
        print("Hardware list")
        print("\t- 6.1in Screen")
        print("\t- A14 Chipset")
        print("\t- 8Gb RAM")
        print("\t- 256Gb Memory")
