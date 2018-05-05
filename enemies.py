import items

class Enemy:
	name = ""
	description = ""
	attack_description = ""
	
	hp = 0
	damage = 0
	
	loot = []
	
	agro = False	# Used to cause enemies to attack spontaneously.
	
	def __init__(self, direction = None, loot = []):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		else:
			self.direction = None
		
		if(len(self.loot) > 0):
			for item in loot:
				self.loot.append(item)
		else:
			self.loot = loot

	def __str__(self):
		return self.name
		
	def check_text(self):
		text = ""
		if(self.direction):
			text = "A %s is blocking your progress to the %s." % (self.name, self.direction)
		text += " " + self.description			
		return text

	def take_damage(self, amount):
		self.hp -= amount
		if(self.hp <= 0):
			self.hp = 0
			defeat_text = "The %s is defeated." % self.name
			if(len(self.loot) > 0):
				defeat_text += " It dropped the following items: "
				for item in self.loot:
					defeat_text += "* " + str(item)
			return defeat_text
		else:
			return "The %s took %d damage." % (self.name, amount)
			
	def is_alive(self):
		return self.hp > 0
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class Thrall(Enemy):
	name = "Thrall"
	description = "It will charge headlong into melee combat range if provoked."
	hp = 10
	damage = 2
	loot = [items.Gold_Coins("A small stack of shiny gold coins lies next to the thrall's corpse.")]


class Ogre(Enemy):
	name = "Ogre"
	description = "Be mindful that they have powerful attacks, making almost any position unsafe regardless of cover."
	hp = 30
	damage = 20
	loot = [items.Gold_Coins("A small stack of shiny gold coins lies next to the Ogre's corpse.")]


class Shreiker(Enemy):
	name = "Shreiker"
	description = "When it begins attacking, it will not stop"
	hp = 100
	damage = 4
	loot = [items.Gold_Coins("A small stack of shiny gold coins lies next to the Shreiker's corpse.")]
	
	agro = True


class Knight(Enemy):
	name = "Knight"
	description = "An armored knight with a cleaver in its hand and an damaged iron key in its back is eager to attack."
	hp = 80
	damage = 15
	loot = [items.Iron_Key("An old iron key lies on the ground near the remains of the Knight."), items.Mountain_of_Gold("The Knight's mountain of gold sits near the key")]