import json

class Statistics:
    def __init__(self,hp,mp,str_val,agi,int_val,per,end,sen):
        self.hp=hp
        self.mp=mp
        self.str=str_val
        self.agi=agi
        self.int=int_val
        self.per=per
        self.end=end
        self.sen= en

    def get_description(self):
        return f"HP: {self.hp} | MP: {self.mp} | STR: {self.str} | AGI: {self.agi} | INT: {self.int} | PER: {self.per} | END: {self.end} | SEN: {self.sen}"

class Armour:
    def __init__(self):
        self.parts={
            "head":None,
            "chest":None,
            "legs":None
        }

    def get_description(self):
        equipped=[k for k, v in self.parts.items() if v is not None]
        if not equipped:
            return "Aucune armure équipée."
        return "Pièces équipées : " + " | ".join(equipped)

class Inventory:
    def __init__(self):
        self.weapon=None
        self.armour=Armour()
        self.ring=None
        self.necklace=None
        self.items=[]
        self.max_slots=30 

class Hunter:
    def __init__(self, name,hunter_class,stats):
        self.name=name
        self.hunter_class= hunter_class
        self.rank="E"
        self.level=1
        self.xp=0
        self.gold=0
        self.stats=stats
        self.inventory=Inventory()

    def get_description(self):
        print(f"--- Profil de {self.name} ---")
        print(f"Classe: {self.hunter_class} | Rang: {self.rank} | Niveau: {self.level}")
        print(f"Stats: {self.stats.get_description()}")
        print(f"Or: {self.gold} | {self.inventory.armour.get_description()}")

class Warrior(Hunter):
    def __init__(self,name):
        stats=Statistics(hp=150,mp=40,str_val=15, agi=5, int_val=5, per=5, end=12, sen=5)
        super().__init__(name,"Guerrier", stats)
        self.signature_skill="Frappe du Conquérant"

class Assassin(Hunter):
    def __init__(self,name):
        stats=Statistics(hp=90, mp=60, str_val=8, agi=18, int_val=5, per=7, end=5, sen=15)
        super().__init__(name,"Assassin", stats)
        self.signature_skill="Lame de l'Ombre"

class Mage(Hunter):
    def __init__(self,name):
        stats=Statistics(hp=80, mp=150, str_val=4, agi=6, int_val=18, per=8, end=5, sen=10)
        super().__init__(name, "Mage", stats)
        self.signature_skill="Nova Arcanique"

class Healer(Hunter):
    def __init__(self,name):
        stats=Statistics(hp=110, mp=100, str_val=5, agi=7, int_val=10, per=6, end=12, sen=14)
        super().__init__(name, "Guérisseur", stats)
        self.signature_skill = "Lumière Sacrée"

class Archer(Hunter):
    def __init__(self,name):
        stats=Statistics(hp=100, mp=70, str_val=10, agi=15, int_val=5, per=15, end=6, sen=8)
        super().__init__(name, "Archer",stats)
        self.signature_skill="Flèche Perçante"
