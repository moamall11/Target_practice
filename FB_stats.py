class Stats:
	"""manage the statistics of the game"""
	def __init__(self,game):
		"""initialize the statistic's attributes"""
		#the game starts in an inactive state.
		self.settings=game.settings
		self.game_active=False