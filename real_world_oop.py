class Mobile():
    """An attempt to describe a mobile phone"""

    def __init__(self, processor, ram, internal_memory):
        self.processor = processor
        self.ram = ram
        self.internal_memory = internal_memory

    def phone_features(self):
        phone= "This phone is of processor " + str(self.processor) + ", has " + str(self.ram) + " RAM and " + str(self.internal_memory) + " memory storage"
        return phone
    
    def message(self):
        msg = input("Enter text message\n")
        return msg
        
class Htc(Mobile):

    def __init__(self, processor, ram, internal_memory):
        """Initialize attributes from parent class"""
        super().__init__(processor, ram, internal_memory) #Inheritance

        
    def _imeiNumber(self):#polymorphism
        imei = "To access IMEI number, dial *#06#"
        return imei
    

class Nokia(Mobile):
    def __init__(self, processor, ram, internal_memory):
        """Initialize attributes from parent class"""
        super().__init__(processor, ram, internal_memory)

    def connectBluetooth(self):
        pass
