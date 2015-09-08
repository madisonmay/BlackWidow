class BlackWidowError(Exception):
    pass 


class BlackWidowIOError(BlackWidowError, IOError):
    pass


class BlackWidowValueError(BlackWidowError, ValueError):
    pass
