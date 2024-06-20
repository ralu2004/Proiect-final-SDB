class ProgramError(Exception):
    pass


class ValidationError(ProgramError):
    pass


class DuplicateException(ProgramError):
    def __init__(self, entity) -> None:
        message = '{0} already exists!'.format(entity)
        super().__init__(message)


class NotFoundException(ProgramError):
    def __init__(self, entity) -> None:
        message = '{0} does not exist!'.format(entity)
        super().__init__(message)


class NoPromotionsException(ProgramError):
    def __init__(self) -> None:
        message = "The list of promotions is empty!"
        super().__init__(message)


class NoProductsException(ProgramError):
    def __init__(self) -> None:
        message = "The list of products is empty!"
        super().__init__(message)


class TooMuchException(ProgramError):
    def __init__(self) -> None:
        message = "The product is unavailable in this quantity! Try entering less!"
