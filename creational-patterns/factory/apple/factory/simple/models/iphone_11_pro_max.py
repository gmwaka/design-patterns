from .iphone import Iphone


class Iphone11ProMax(Iphone):

    def getHardware(self) -> None:
        super().getHardware()
        print("Hardware list")
        print("\t- 6.8in Screen")
        print("\t- A13 Chipset")
        print("\t- 4Gb RAM")
        print("\t- 512Gb Memory")
