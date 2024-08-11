class LoadError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.type_error = "LoadError"