from twttr import shorten
import pytest


def test_shorten():
    assert shorten("CAT") == "CT"
    assert shorten("hello") == "hll"
    assert shorten("1234") == "1234"
    assert shorten("hello, world") == "hll, wrld"