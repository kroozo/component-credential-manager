"""[summary]
Main module.
[description]
The main module starts the web service
"""
from app import app

if __name__ == "__main__":
	"""[summary]
	
	[description]
	The main module defines exception handler and runs the web service
	"""
	app.run(host= '0.0.0.0',port=5001)
