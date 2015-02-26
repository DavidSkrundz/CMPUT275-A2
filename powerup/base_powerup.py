import pygame
from pygame.sprite import Sprite

SIZE = 20

class BasePowerup(Sprite):
	"""
	The basic representation of a powerup from which all powerups extend.
	Has a graphical representation and just sits there until a unit collides
	with it.

	Note: self._base_image MUST be set in subclasses! This is the image from
	which the powerup renders its image.
	"""
	active_powerups = pygame.sprite.LayeredUpdates()

	def __init__(self, tile_x = None, tile_y = None):
		Sprite.__init__(self)

		self.info = "POWERUP"

		#Take the keywords off
		self.tile_x = tile_x
		self.tile_y = tile_y

		self._active = False
		self.rect = pygame.Rect(0, 0, SIZE, SIZE)

		self._update_image()
		self.activate()

	@staticmethod
	def get_powerup_at_pos(pos):
		"""
		Returns the active unit at the given tile position, or None if no unit
		is present.
		"""
		for u in BasePowerup.active_powerups:
			if (u.tile_x, u.tile_y) == pos:
				return u
		return None

	def consume(self, unit):
		self.deactivate()
		self.used(unit)

	def used(self, unit):
		"""
		Override this in subclasses
		"""
		pass

	def activate(self):
		"""
		Adds this unit to the active roster.
		"""
		if not self._active:
			self._active = True
			BasePowerup.active_powerups.add(self)

	def deactivate(self):
		"""
		Removes this unit from the active roster.
		"""
		if self._active:
			self._active = False
			BasePowerup.active_powerups.remove(self)

	def _update_image(self):
		"""
		Re-renders the unit's image.
		"""
		# Pick out the right sprite depending on the team
		try:
			subsurf = self._base_image.subsurface(self.rect)
		except ValueError:
			# No sprite for this team
			raise ValueError(
				"Class {} does not have a sprite for team {}!".format(self.__class__.__name__, self.team))
		except AttributeError:
			# No image is loaded
			return

		# Rotate the sprite
		self.image = pygame.transform.rotate(subsurf, 0)
