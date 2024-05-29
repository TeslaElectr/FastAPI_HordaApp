from .exception import BaseAppException

class DataBaseConnectionError(BaseException):
    
    def __init__(
        self,
        message: str = "###error to connect db",
    ):

        self.message = message
        super().__init__(self.message)