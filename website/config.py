# Set as environment variables if you need info to be secret!

class Config:
	# Three /// creates a realative path alongside the module, so will place inside same folder
	SECRET_KEY = '352fd3d0f45582d3c5642c75ada5c408'
	SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']