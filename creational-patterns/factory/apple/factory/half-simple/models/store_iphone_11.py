from models.store import Store
from models.iphone import Iphone
from models.iphone_11 import Iphone11
from models.iphone_11_pro import Iphone11Pro
from models.iphone_11_pro_max import Iphone11ProMax


class StoreIphone11(Store):
    # This is the implementation of the factory method
    def createIphone(self, model: str) -> Iphone:
        if model == "standard":
            return Iphone11()
        elif model == "Pro":
            return Iphone11Pro()
        elif model == "Pro Max":
            return Iphone11ProMax()
