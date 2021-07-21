from models.iphone import Iphone
from models.iphone_12 import Iphone12
from models.iphone_11 import Iphone11
from models.iphone_12_mini import Iphone12Mini
from models.iphone_12_pro import Iphone12Pro
from models.iphone_11_pro import Iphone11Pro
from models.iphone_12_pro_max import Iphone12ProMax
from models.iphone_11_pro_max import Iphone11ProMax


class IphoneSimpleFactory:
    def createIphone(self, generation: str, model: str) -> Iphone:
        self.device = None
        if generation == "12":
            if model == "standard":
                self.device = Iphone12()
            elif model == "Pro":
                self.device = Iphone12Pro()
            elif model == "Pro Max":
                self.device = Iphone12ProMax()
            elif model == "Mini":
                self.device = Iphone12Mini()
        elif generation == "11":
            if model == "standard":
                self.device = Iphone11()
            elif model == "Pro":
                self.device = Iphone11Pro()
            elif model == "Pro Max":
                self.device = Iphone11ProMax()

        return self.device
