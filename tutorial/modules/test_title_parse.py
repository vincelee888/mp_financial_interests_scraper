__author__ = 'Vince Lee'

import title_parse as target


def test_parse_simple():
    title = "LEE, Vincent (Manchester, Gtr. Manchester)"
    result = target.parse(title)
    assert result.firstName == "Vincent"
    assert result.surname == "Lee"
    assert result.constituency == "Manchester, Gtr. Manchester"

def test_parse_double_barrelled():
    title = "LEE-LEE, Vincent (Manchester, Gtr. Manchester)"
    result = target.parse(title)
    assert result.firstName == "Vincent"
    assert result.surname == "Lee-Lee"
    assert result.constituency == "Manchester, Gtr. Manchester"

def test_parse_middle_names():
    title = "LEE, Vincent Stanley (Manchester, Gtr. Manchester)"
    result = target.parse(title)
    assert result.firstName == "Vincent Stanley"
    assert result.surname == "Lee"
    assert result.constituency == "Manchester, Gtr. Manchester"