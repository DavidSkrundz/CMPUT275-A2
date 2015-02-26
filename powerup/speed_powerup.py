import pygame
from pygame.sprite import Sprite
import powerup
from powerup.base_powerup import BasePowerup

class SpeedPowerup(BasePowerup):
	sprite = pygame.image.load("assets/Speed_PUP.png")

	def __init__(self, **keywords):
		#load the image for the base class.
		self._base_image = SpeedPowerup.sprite

		#load the base class
		super().__init__(**keywords)

powerup.powerup_types["SpeedPowerup"] = SpeedPowerup
