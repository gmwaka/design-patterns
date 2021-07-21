from models.store import Store
from models.iphone_simple_factory import IphoneSimpleFactory


if __name__ == "__main__":
    store = Store(IphoneSimpleFactory)
    print(store.orderIphone(generation='12', model='standard'))
    print(store.orderIphone(generation='11', model='Pro Max'))
