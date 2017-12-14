'''
Common Error handler class
--------------------------
'''

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class UserTypeError(Error):
    """Invalid user type error."""
    pass
