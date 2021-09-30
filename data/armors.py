from dataimports import *
class armor:
    def __init__(self, setname, monster, requireditems, armorpieces, skills):
        self.setname = str(setname)
        self.monster = monster
        self.requireditems = dict(requireditems)
        self.armorpieces = dict(armorpieces)
        self.skills = dict(skills)