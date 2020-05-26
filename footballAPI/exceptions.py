class InvalidParams(Exception):
	"""
	Raised when invalid params have been passed to the request.
	"""
	pass

class InvalidStatusCode(Exception):
	"""
	Raised when an invalid status code is recieved from the API.
	"""
	pass

class MissingAPIKey(Exception):
	"""
	Raised when the api key has not been passed to the APIFootball class and is not an environment variable.
	"""
	pass

class NoAvailableCredits(Exception):
	"""
	Raised when the user does not have enough credits to make the requested calls.
	"""
	pass