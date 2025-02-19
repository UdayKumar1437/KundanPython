class Raghavarao:
    def __init__(self,son):
        self.son = son
    
    def hitech_city_property(self):
        print("Hi-Tech City Property")

    def kakinada_property(self):
        print("Kakinada Property")

class Dinesh(Raghavarao):
    def __init__(self, daughter,wife):
        Raghavarao.__init__(self,"Dinesh")
        self.daughter = daughter
        self.wife = wife
    
    def malkajgiri_property(self):
        print("Malkajgiri property")
    
    def bangalore_property(self):
        print("Bangalore Property")

class Kundan(Dinesh):
    def __init__(self, daughter, wife):
        Dinesh.__init__(self,daughter,wife)

kundanika = Kundan("Kundan","Anju")
kundanika.bangalore_property()
print(kundanika.daughter)