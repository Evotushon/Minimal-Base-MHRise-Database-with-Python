from dataimports import *
class item:
    def __init__(self, itemname, max, description, obtain, percentual, location, isloot, monster, monsterpart, ):
        self.name = str(itemname)
        self.max = int(max)
        self.description = str(description)
        self.obtain = str(obtain)
        self.isloot = bool(isloot)
        self.percentual = int(percentual)
        if self.isloot:
            self.monster = monster
            self.monsterpart = monsterpart
        else:
            self.location = location
