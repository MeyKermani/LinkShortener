class UnableToCreateShorterURL(Exception):
    """ Exception raised for errors in generating short links"""
    def __init__(self, message="Couldn't  create a short link"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ErrorInSavingTheLinkInDatabase(Exception):
    """ Exception raised when the system can't save the link in database"""
    def __init__(self, message="Couldn't save to database"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ErrorInFindingTheOriginalURL(Exception):
    """ Exception raised when the system can't retrieve the original URL"""
    def __init__(self, message="Couldn't find the original URL"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message
