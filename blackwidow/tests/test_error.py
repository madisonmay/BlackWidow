from blackwidow import error

def test_blackwidow_error():
    assert isinstance(error.BlackWidowIOError(), IOError)
