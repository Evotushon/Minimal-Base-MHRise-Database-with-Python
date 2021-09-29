class monster:
    def __init__(self, name, type, stars, location, hitzone):
        self.name = str(name)
        self.type = str(type)
        self.stars = int(stars)
        self.location = list(location)
        self.hitzones = dict(hitzone)
