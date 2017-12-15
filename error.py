'''
Common Error handler class
--------------------------
'''

class Error(Exception):
    """Base class for exceptions in this module."""
    """.. todo: add filename, line number """
    
    def __init__(self, filename_= "<Unknown file>",linenumber= "<Unknown line#>"):
        self.message = "Base (unknown type) error"

class UserTypeError(Error):
    """Exception for Invalid user type errors."""
    
    def __init__(self):
        self.message = "Invalid user type error"
 
class UserListCreationError(Error):
    """Exception for error in creation of user list."""
    
    def __init__(self):
        self.message = "Error creating user list"
        
class UserListCreationFromJSONError(UserListCreationError):
    """Exception for error in creation of user list from JSON file."""
    
    def __init__(self):
        self.message = "Error creating user list from JSON"
