
from kanashi.buffer import AoE

class Virtual( AoE ):
	
	# Class initialization.
	def __init__( self ):
		pass
		
	# Get data from response.
	def get( self ):
		try:
			with open( "kanashi/saveds/response/response.json", "r" ) as fopen:
				data = fopen.read()
				fopen.close()
			return( data )
		except FileNotFoundError as e:
			self.tree( "kanashi/saveds/response" )
			with open( "kanashi/saveds/response/response.json", "w" ) as fopen:
				fopen.write( "[]" )
				fopen.close()
			return([])
	
# Get virtual data from request response.
data = Virtual().get()
