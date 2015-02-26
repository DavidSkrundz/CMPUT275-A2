import pygame
from pygame.sprite import Sprite
import powerup
from powerup.base_powerup import BasePowerup
from unit.transport import Transport

class AttackPowerup(BasePowerup):
	sprite = pygame.image.load("assets/Damage_PUP.png")

	def __init__(self, **keywords):
		#load the image for the base class.
		self._base_image = AttackPowerup.sprite

		#load the base class
		super().__init__(**keywords)

		self.info = "Boost Damage by 2"

	def used(self, unit):
		if not isinstance(unit, Transport):
			unit.damage += 2

powerup.powerup_types["AttackPowerup"] = AttackPowerup
