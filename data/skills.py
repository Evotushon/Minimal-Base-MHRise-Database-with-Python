from dataimports import *
class skill:
    def __init__(self, skillname, maxlevel, gunneronly, swordmasteronly, foreveryweapon, jewelname, jewelslots):
        self.skillname = str(skillname)
        self.maxlevel = int(maxlevel)
        self.gunneronly = bool(gunneronly)
        self.swordmasteronly = bool(swordmasteronly)
        self.foreveryweapon = foreveryweapon
        self.jewelname = str(jewelname)
        self.jewelslots = int(jewelslots)
        if self.foreveryweapon:
            swordmasteronly = False
            gunneronly = False
        if not self.gunneronly and not self.swordmasteronly:
            foreveryweapon = True