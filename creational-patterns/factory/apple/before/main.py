from models.store import Store


if __name__ == "__main__":
    store = Store()
    print(store.orderIphone(generation='12', model='standard'))
    print(store.orderIphone(generation='11', model='Pro Max'))
