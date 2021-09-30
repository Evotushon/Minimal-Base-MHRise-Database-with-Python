from dataimports import *
class armor:
    def __init__(self, setname, monster, requireditems, armorpieces, skills, skill_level):
        self.setname = str(setname)
        self.monster = monster
        self.requireditems = dict(requireditems)
        self.armorpieces = dict(armorpieces)
        self.skills = dict(skills)
        self.skill_level = int(skill_level)