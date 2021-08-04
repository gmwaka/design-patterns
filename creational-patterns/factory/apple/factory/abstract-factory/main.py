from models.store_iphone11 import StoreIphone11
from models.store_iphone12 import StoreIphone12
from factory.iphone11_hardware_factory import Iphone11HardwareFactory
from factory.iphone12_hardware_factory import Iphone12HardwareFactory


if __name__ == "__main__":
    store_iphone11 = StoreIphone11(Iphone11HardwareFactory)
    store_iphone12 = StoreIphone12(Iphone12HardwareFactory)
    print(store_iphone11.orderIphone())
    print(store_iphone12.orderIphone())
