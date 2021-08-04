from factory.iphone_hardware_factory import IphoneHardwareFactory


class Iphone11HardwareFactory(IphoneHardwareFactory):
    def createModel() -> str:
        return "Iphone 11"

    def createChip() -> str:
        return "A13 Bionic"

    def createDisplay() -> str:
        return "6.1 inch for Iphone 11"

    def createCamera() -> str:
        """
        This method could instatiate a camera object.
        To keep stuff simple here, we are just creating an instance of string
        """
        return "2 Camera 12Mp for Iphone 11"
