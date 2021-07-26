from models.store import Store
from models.store_iphone_11 import StoreIphone11
from models.store_iphone_12 import StoreIphone12


if __name__ == "__main__":
    store_iphone11 = StoreIphone11()
    store_iphone12 = StoreIphone12()
    print(store_iphone11.orderIphone(model='standard'))
    print(store_iphone12.orderIphone(model='Pro Max'))
