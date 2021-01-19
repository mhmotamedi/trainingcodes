#import requests
import sys
print(sys.version)

def add(x, y):
    return x+y

def test_add():
    """unit test for add func
    """
    assert add(1, 2) == 3