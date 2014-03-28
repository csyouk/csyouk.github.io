class HousePark:
    lastname ="Park"
    def __init__(self,name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print "%s,%s go to travel." % (self.fullname, where)
    def __del__(self):
        print "%s instance is deleted" % self.fullname

class HouseKim(HousePark):
    lastname = "kim"
