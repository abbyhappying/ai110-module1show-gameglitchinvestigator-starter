def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# FIX #4: Swapped "Too High/Low" messages - AI identified this as critical bug making game unplayable
# FIX #3: Refactored to always use integer comparison - AI suggested this approach during pair programming session
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        guess_int = int(guess)
        secret_int = int(secret)

        if guess_int == secret_int:
            return "Win", "🎉 Correct!"
        elif guess_int > secret_int:
            return "Too High", "📈 Go Lower!"
        else:
            return "Too Low", "📉 Go Higher!"
    except (ValueError, TypeError):
        # If conversion fails, it's not a valid number
        return "Error", "Invalid comparison!"


# FIX #5: Reversed score reward/penalty logic - AI noticed the +5/-5 were swapped
# FIX #6: Fixed attempt_number off-by-one - AI used debugging session to trace the issue
def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        # FIX: Corrected attempt_number calculation - AI suggested using attempt_number - 1
        # Previously: 100 - 10 * (attempt_number + 1)
        points = 100 - 10 * attempt_number  # FIXED: Now correct for first attempt
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
