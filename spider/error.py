class SpiderError(Exception):
    pass 


class SpiderIOError(SpiderError, IOError):
    pass


class SpiderValueError(SpiderError, ValueError):
    pass
