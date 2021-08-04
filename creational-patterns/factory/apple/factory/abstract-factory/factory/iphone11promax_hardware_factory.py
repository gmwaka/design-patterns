from factory.iphone_hardware_factory import IphoneHardwareFactory


class Iphone11ProMaxHardwareFactory(IphoneHardwareFactory):
    def createModel() -> str:
        return "Iphone 11 Pro Max"

    def createChip() -> str:
        return "A13 Bionic"

    def createDisplay() -> str:
        return "6.8 inch"

    def createCamera() -> str:
        return "3 Cameras 12Mp"
