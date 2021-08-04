from factory.iphone_hardware_factory import IphoneHardwareFactory


class Iphone12ProMaxHardwareFactory(IphoneHardwareFactory):
    def createModel() -> str:
        return "Iphone 12 Pro Max"

    def createChip() -> str:
        return "A14 Bionic"

    def createDisplay() -> str:
        return "6.8 inch"

    def createCamera() -> str:
        return "3 Camera 12Mp"
