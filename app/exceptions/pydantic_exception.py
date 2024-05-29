from .exception import BaseAppException


class PydanticDumpException(BaseAppException):
    
    def __init__(
        self,
        message: str = "###pydantic error"
    ):

        self.message = message
        super().__init__(self.message)