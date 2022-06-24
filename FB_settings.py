class Settings:
	"""the settings for the game"""
	def __init__(self):
		"""initialize the static settings for the game"""
		
		#screen settings
		self.screen_width=1200
		self.screen_height=650
		self.bg_color=(230,230,230)
		
		#bullets settings
		self.bullet_width=30
		self.bullet_height=6
		self.bullet_limit=3
		self.bullet_color=(100,0,0)
		
		#rectangle settings
		self.rect_width=25
		self.rect_height=90
		self.rect_color=(60,60,60)
		
		self.spead_scale=1.2

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""initialize the settings that change during the game"""
		self.bullet_speed=3
		#ship settings
		self.ship_speed=1
		self.rect_speed=0.3
		#the direction of the rectangle where 1 means down and -1 means up.
		self.rect_direction=1
		self.score=0
		self.misses=0
		self.level=0


	def increase_spead(self):
		"""increase the spead of the game"""
		self.bullet_speed*=self.spead_scale
		self.ship_speed*=self.spead_scale
		self.rect_speed*=self.spead_scale

