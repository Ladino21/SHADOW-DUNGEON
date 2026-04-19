


class Hunter:
     def __init__(self,name,stat,rank,origin,gold):
          self.name=name
          self.type=type
          self.rank=rank
          self.origin=origin
          self.gold=gold

     def get_description(self):
          print("Name:",self.namen,"| Type",self.type,"| Statistics:",self.stat,"| Rank:",self.rank,"| Origin:",self.origin,"| Money",self.gold)

class Tank(Hunter):
     def __init__(self):
class Statistics:
     def __init__(self,hp,mp,str,agi,int,per,sta,sen):
          self.hp=hp
          self.mp=mp
          self.str=str
          self.agi=agi
          self.int=agi
          self.int=int
          self.per=per
          self.sta=sta
          self.sen=sen

     def get_description(self):
          print("Health point:",self.hp,"| Mana point:",self.mp,"| Strength :",self.str,"| Agility:",self.agi,"| Intelligence:",self.int,"| Perception:",self.per,"| Stamina:",self.sta,"| Sense:",self.sen)



class Inventory:
     def __init__(self,weapon,armour,ring,necklace,place):
          self.weapon=weapon
          self.armour=armour
          self.collar=necklace
          self.ring=ring
          self.place=place


class Armour:
     def __init__(self):
          self.parts={
               "body":False,
               "head":False,
               "legs":False,
               "arms":False,
               "chest":False
          }

     def get_description(self):
          if all(self.parts.values()):
               print("You owns the armour in the entire body")
          elif any(self.parts.values()):
               print("You are wearing armour:")
               k=0
               for var in self.parts:
                    if var is True and k==0:
                         print(var)
                    elif var is True and k!=0:
                         print(" | ",var)
          else:
               print("You aren't wearing any armour")
