from dataimports import *
class skill:
    def __init__(self, skillname, maxlevel, gunneronly, swordmasteronly, foreveryweapon):
        self.skillname = str(skillname)
        self.maxlevel = int(maxlevel)
        self.gunneronly = bool(gunneronly)
        self.swordmasteronly = bool(swordmasteronly)
        if not self.gunneronly and not self.swordmasteronly:
            self.foreveryweapon = foreveryweapon
            foreveryweapon = True