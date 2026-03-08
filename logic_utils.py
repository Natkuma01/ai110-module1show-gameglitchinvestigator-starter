def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# FIX: Refactored logic with proper data type, ensure the input range is base on the difficulties level
#      with Copilot Agent mode
def parse_guess(raw: str, low: int, high: int):
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = float(raw)
        else:
            value = int(raw)
    except (ValueError, TypeError):
        return False, None, "That is not a number. Only integers and decimals are accepted."

    if not isinstance(value, (int, float)):
        return False, None, "Only int or float (double) values are accepted."

    if value < low or value > high:
        return False, None, f"Please enter a number between {low} and {high}."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if not isinstance(guess, (int, float)):
        raise TypeError(f"guess must be int or float, got {type(guess).__name__}")
    if not isinstance(secret, (int, float)):
        raise TypeError(f"secret must be int or float, got {type(secret).__name__}")

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
