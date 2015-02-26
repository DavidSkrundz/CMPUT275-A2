import pygame
from pygame.sprite import Sprite
import powerup
from powerup.base_powerup import BasePowerup

class HealthPowerup(BasePowerup):
	sprite = pygame.image.load("assets/Health_PUP.png")

	def __init__(self, **keywords):
		#load the image for the base class.
		self._base_image = HealthPowerup.sprite

		#load the base class
		super().__init__(**keywords)

		self.info = "Heals unit by 10"

	def used(self, unit):
		unit.health = min(unit.health + 10, unit.max_health)

powerup.powerup_types["HealthPowerup"] = HealthPowerup
