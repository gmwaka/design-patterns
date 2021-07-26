from .iphone import Iphone


class Iphone11Pro(Iphone):

    def getHardware(self) -> None:
        super().getHardware()
        print("Iphone 11 Pro : Hardware list")
        print("\t- 6.1in Screen")
        print("\t- A13 Chipset")
        print("\t- 4Gb RAM")
        print("\t- 256Gb Memory")
