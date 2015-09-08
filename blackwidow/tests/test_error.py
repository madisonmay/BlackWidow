from .. import error

def test_spider_error():
    assert isinstance(error.SpiderIOError(), IOError)
