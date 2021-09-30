from dataimports import *
class monster:
    def __init__(self, name, type, stars, location, hitzone, loot, set, head, body, arms, legs, boots):
        self.name = str(name)
        self.type = str(type)
        self.stars = int(stars)
        self.location = list(location)
        self.hitzones = dict(hitzone)
        self.loot = dict(loot)
        self.head = head
        self.body = body
        self.arms = arms
        self.set = dict(set) = {
            self.head,
            self.body,
            self.arms,
            self.legs,
            self.boots,
        }
