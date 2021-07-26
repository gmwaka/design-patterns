from .iphone import Iphone


class Iphone12ProMax(Iphone):

    def getHardware(self) -> None:
        super().getHardware()
        print("Hardware list")
        print("\t- 6.8in Screen")
        print("\t- A14 Chipset")
        print("\t- 8Gb RAM")
        print("\t- 512Gb Memory")
