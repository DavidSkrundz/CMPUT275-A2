from unit.water_unit import WaterUnit
import unit, helper, effects
from tiles import Tile
import pygame

class PTBoat(WaterUnit):
	"""
	The PT boat is a faster, smaller, more fragile boat.
	It does slightly less damage, but can get around more easily.

	Armour: LOW
	Speed: VERY HIGH
	Range: MEDIUM
	Damage: LOW

	Other notes:
	- Despite its low stats, this unit is constrained to the water, so its
	  uses are fairly specialized and limited.
	"""
	sprite = pygame.image.load("assets/PT-boat.png")

	def __init__(self, **keywords):
		#load the image for the base class.
		self._base_image = PTBoat.sprite

		#load the base class
		super().__init__(**keywords)

		#sounds
		self.hit_sound = "ArtilleryFire"

		#set unit specific things.
		self.type = "PT Boat"
		self.speed = 12
		self.max_atk_range = 6
		self.damage = 4
		self.defense = 1
		self.hit_effect = effects.Explosion

		self.health = 12
		self.max_health = self.health

		self._update_image()

unit.unit_types["PTBoat"] = PTBoat
