from .iphone import Iphone


class Iphone12Mini(Iphone):

    def getHardware(self) -> None:
        super().getHardware()
        print("Iphone 12 Mini : Hardware list")
        print("\t- 5.1in Screen")
        print("\t- A14 Chipset")
        print("\t- 4Gb RAM")
        print("\t- 64Gb Memory")
