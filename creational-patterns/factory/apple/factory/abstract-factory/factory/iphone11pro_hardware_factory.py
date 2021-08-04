from factory.iphone_hardware_factory import IphoneHardwareFactory


class Iphone11ProHardwareFactory(IphoneHardwareFactory):
    def createModel() -> str:
        return "Iphone 11 Pro"

    def createChip() -> str:
        return "A13 Bionic"

    def createDisplay() -> str:
        return "5.8 inch"

    def createCamera() -> str:
        return "3 Camera 12Mp"
