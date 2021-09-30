from dataimports import *
class item:
    def __init__(self, itemname, max, description, obtain, isloot):
        self.name = str(itemname)
        self.max = int(max)
        self.description = str(description)
        self.obtain = str(obtain)
        self.isloot = bool(isloot)
