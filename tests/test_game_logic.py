import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import parse_guess, check_guess

# --- parse_guess tests ---

def test_parse_guess_empty_string():
    ok, value, err = parse_guess("", 1, 100)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_none():
    ok, value, err = parse_guess(None, 1, 100)
    assert ok is False
    assert value is None
    assert err == "Enter a guess."

def test_parse_guess_non_numeric():
    ok, value, _ = parse_guess("abc", 1, 100)
    assert ok is False
    assert value is None

def test_parse_guess_valid_int():
    ok, value, err = parse_guess("42", 1, 100)
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_valid_float():
    ok, value, err = parse_guess("42.5", 1, 100)
    assert ok is True
    assert isinstance(value, float)
    assert err is None

def test_parse_guess_below_range():
    ok, value, err = parse_guess("0", 1, 100)
    assert ok is False
    assert value is None
    assert "1" in err and "100" in err

def test_parse_guess_above_range():
    ok, value, err = parse_guess("101", 1, 100)
    assert ok is False
    assert value is None
    assert "1" in err and "100" in err

def test_parse_guess_at_lower_bound():
    ok, value, _ = parse_guess("1", 1, 100)
    assert ok is True
    assert value == 1

def test_parse_guess_at_upper_bound():
    ok, value, _ = parse_guess("100", 1, 100)
    assert ok is True
    assert value == 100

def test_parse_guess_rejects_complex_string():
    ok, value, _ = parse_guess("3+4j", 1, 100)
    assert ok is False
    assert value is None


# --- check_guess tests ---

def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
