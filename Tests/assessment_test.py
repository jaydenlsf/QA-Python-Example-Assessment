import pytest
from Code.example import endsPy


def test_endsPy():
    assert endsPy("ilovepy") == True
    assert endsPy("welovepy") == True
    assert endsPy("welovepyforreal") == False
    assert endsPy("pyiscool") == False
    assert endsPy("hurrayforpY") == True
