from os import environ
from re import compile, match


regularExpression = "^[a-z]{1,6}_{0,1}\\d{0,4}@hackerrank.com$"

pattern = compile(regularExpression)


def test_regex():
    assert pattern.match("julia@hackerrank.com")
    assert pattern.match("julia_@hackerrank.com")
    assert pattern.match("julia_0@hackerrank.com")
    assert not pattern.match("julia0_@hackerrank.com")
    assert not pattern.match("julia@gmail.com")

    assert not pattern.match("manychars@hackerrank.com")
    assert not pattern.match("_01@hackerrank.com")
    assert not pattern.match("chars_char@hackerrank.com")
    assert not pattern.match("chars_c1@hackerrank.com")
    assert not pattern.match("char1_1@hackerrank.com")

    assert pattern.match("ysvavv_@hackerrank.com")
    assert pattern.match("rlkspp_0491@hackerrank.com")
    assert pattern.match("liizgt@hackerrank.com")
    assert pattern.match("knfgqh5@hackerrank.com")
