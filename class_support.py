class Weapon:
  def __init__(self, wn, watk, whit, wType):
    self.wname = wn
    self.watk = watk
    self.w_hit = whit
    self.wType = wType

class Armor:
  def __init__(self, armn, armrate, armwg, aType):
    self.aname = armn
    self.arate = armrate
    self.aweight = armwg
    self.aType = aType

class Item:
  def __init__(self, inm, ityp, ia, iD=0):
    self.iname = inm      # name of the item
    self.itype = ityp     # type of item heal, Consumable, key
    self.iamount = ia     # amount of items in inventory
    self.iDmg = iD        # damage the itme does

class Spell:
  def __init__(self, sNm, slvl, sTyp, sC, sDmg):
    self.sname = sNm   # name of the Spell
    self.slevel = slvl
    self.stype = sTyp  # type of Spell: heal, Dmg
    self.sCost = sC    # mana Cost
    self.sDmg = sDmg   # Spell Dmg/heal amount
    
class Skill:
  def __init(self, kNm, kTyp, kC, kDmg):
    self.kname= kNm  # skill name
    self.ktype= kTyp # skill type (atk, heal)
    self.kCost= kC   # Stamina
    self.kDmg= kDmg  # amount of damage the skill does
