from models.store import Store
from models.iphone import Iphone
from models.iphone_12 import Iphone12
from models.iphone_12_mini import Iphone12Mini
from models.iphone_12_pro import Iphone12Pro
from models.iphone_12_pro_max import Iphone12ProMax


class StoreIphone12(Store):
    # This is the implementation of the factory method
    def createIphone(self, model: str) -> Iphone:
        if model == "Mini":
            return Iphone12Mini()
        elif model == "standard":
            return Iphone12()
        elif model == "Pro":
            return Iphone12Pro()
        elif model == "Pro Max":
            return Iphone12ProMax()
