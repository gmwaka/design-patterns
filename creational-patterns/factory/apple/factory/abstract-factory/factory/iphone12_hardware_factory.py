from factory.iphone_hardware_factory import IphoneHardwareFactory


class Iphone12HardwareFactory(IphoneHardwareFactory):
    def createModel() -> str:
        return "Iphone 12"

    def createChip() -> str:
        return "A14 Bionic"

    def createDisplay() -> str:
        return "6.1 inch"

    def createCamera() -> str:
        return "2 Camera 12Mp"
