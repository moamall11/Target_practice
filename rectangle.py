import pygame

class Rectangle:
	"""manage the rectangle"""
	def __init__(self,game):
		"""initialize the attributes for the rectangle"""
		self.settings=game.settings
		self.screen=game.screen
		#set the rect.
		self.rect=pygame.Rect(
			0,0,self.settings.rect_width,self.settings.rect_height)
		#set the position.
		self.rect.x=self.settings.screen_width - self.rect.width
		self.rect.y=self.rect.height
		#store the decimal value of the y dimension of the rectangle.
		self.y=float(self.rect.y)


	def update(self):
		"""update the position of the rectangle"""
		self.y+=(self.settings.rect_speed * self.settings.rect_direction)
		self.rect.y=self.y
		if self.rect.bottom >= self.screen.get_rect().bottom or self.rect.y <=0:
			self.settings.rect_direction *= -1
		if self.settings.level>=5:
			self.settings.rect_color=(250,0,0)

	def draw_rect(self):
		"""draw the rectangle to the surface"""
		pygame.draw.rect(self.screen,self.settings.rect_color,self.rect)