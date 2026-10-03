from logic_utils import check_guess, parse_guess


def test_winning_guess():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_parse_guess_rejects_out_of_range():
    ok, value, err = parse_guess("1000", 1, 100)
    assert ok is False
    ok, value, err = parse_guess("-1", 1, 100)
    assert ok is False