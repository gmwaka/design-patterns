from .iphone import Iphone
from .iphone_12 import Iphone12
from .iphone_11 import Iphone11
from .iphone_12_mini import Iphone12Mini
from .iphone_12_pro import Iphone12Pro
from .iphone_11_pro import Iphone11Pro
from .iphone_12_pro_max import Iphone12ProMax
from .iphone_11_pro_max import Iphone11ProMax


class Store:
    def orderIphone(self, generation: str, model: str) -> Iphone:
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

        self.device.getHardware()
        self.device.assemble()
        self.device.certificates()
        self.device.pack()

        return self.device
