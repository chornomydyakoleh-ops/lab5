import pytest
from validator.validator import validate_brackets


def test_valid_strings():
    assert validate_brackets("") is None
    assert validate_brackets("print('Hello, world!')") is None
    assert validate_brackets("<div><p>{ test }</p></div>") is None
    assert validate_brackets("((<({<{}>})>))") is None


def test_unmatched_closing_bracket():
    with pytest.raises(ValueError) as exc_info:
        validate_brackets("foo)")
    assert "Дужки незбалансовані на позиціях 3" in str(exc_info.value)
    assert "^" in str(exc_info.value)


def test_unclosed_opening_bracket():
    with pytest.raises(ValueError) as exc_info:
        validate_brackets("(bar")
    assert "Дужки незбалансовані на позиціях 0" in str(exc_info.value)


def test_mismatched_brackets():
    with pytest.raises(ValueError) as exc_info:
        validate_brackets("{>")
    msg = str(exc_info.value)
    assert "0" in msg
    assert "1" in msg

def test_assignment_example():
    sample = "<div><p>{ test }}</p</div>"
    with pytest.raises(ValueError) as exc_info:
        validate_brackets(sample)

    msg = str(exc_info.value)
    assert "16" in msg
    assert "17" in msg
    assert "^^" in msg