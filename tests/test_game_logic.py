import os
import sys

# Make the project root importable (for logic_utils) and locatable (for app.py)
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
APP_PATH = os.path.join(PROJECT_ROOT, "app.py")

from logic_utils import check_guess, parse_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_parse_negative_number_guess():
    ok, value, err = parse_guess("-5")
    assert ok is True
    assert value == -5
    assert err is None

    outcome, _ = check_guess(value, 0)
    assert outcome == "Too Low"


def test_parse_decimal_guess_uses_integer_part():
    ok, value, err = parse_guess("12.9")
    assert ok is True
    assert value == 12
    assert err is None

    outcome, _ = check_guess(value, 13)
    assert outcome == "Too Low"


def test_parse_extremely_large_guess_is_handled():
    huge_guess = "99999999999999999999999999999999999999"
    ok, value, err = parse_guess(huge_guess)
    assert ok is True
    assert value == int(huge_guess)
    assert err is None

    outcome, _ = check_guess(value, 1)
    assert outcome == "Too High"


# ---------------------------------------------------------------------------
# Behavioral tests that drive the real app.py through Streamlit's AppTest.
# These target the bugs just fixed plus every FIXME marked in app.py.
# ---------------------------------------------------------------------------
from streamlit.testing.v1 import AppTest


def _run_app():
    """Return a freshly-run AppTest instance for app.py."""
    return AppTest.from_file(APP_PATH).run()


def _attempts_left_text(at):
    """Pull the 'Attempts left: N' substring from the info banner."""
    for element in at.info:
        if "Attempts left:" in element.value:
            return element.value
    return ""


# --- Bug just fixed: changing difficulty must reset the game ----------------
# (FIXME: "Difficulty change doesn't reset state")
def test_changing_difficulty_resets_game_state():
    at = _run_app()

    # Simulate a finished game on the starting difficulty.
    at.session_state["attempts"] = 4
    at.session_state["status"] = "lost"
    at.session_state["score"] = 30
    at.session_state["history"] = [10, 20]
    at.run()

    # Switch difficulty -> the game should reset.
    at.selectbox[0].set_value("Hard").run()

    assert at.session_state["attempts"] == 0
    assert at.session_state["status"] == "playing"
    assert at.session_state["history"] == []
    assert at.session_state["score"] == 0
    assert at.session_state["current_difficulty"] == "Hard"


def test_changing_difficulty_gives_secret_in_new_range():
    at = _run_app()
    at.selectbox[0].set_value("Easy").run()  # Easy range is 1..20
    assert 1 <= at.session_state["secret"] <= 20


# --- Bug just fixed: "Attempts left" must never display a negative number ---
def test_attempts_left_never_negative():
    at = _run_app()
    at.session_state["attempts"] = 999  # well past any limit
    at.run()

    text = _attempts_left_text(at)
    assert "Attempts left: 0" in text
    # Guard against a "-" sneaking into the count.
    assert "-" not in text.split("Attempts left:")[1]


# --- FIXME: attempts should start at 0, not 1 -------------------------------
def test_attempts_start_at_zero():
    at = _run_app()
    assert at.session_state["attempts"] == 0


# --- FIXME: hint messages swapped (Too High should say "Go Lower") ----------
def test_too_high_hint_tells_player_to_go_lower():
    at = _run_app()
    at.session_state["secret"] = 50
    at.run()
    at.text_input[0].set_value("60").run()
    at.button[0].click().run()  # Submit Guess

    warnings = " ".join(w.value for w in at.warning)
    assert "Lower" in warnings
    assert "Higher" not in warnings


def test_too_low_hint_tells_player_to_go_higher():
    at = _run_app()
    at.session_state["secret"] = 50
    at.run()
    at.text_input[0].set_value("40").run()
    at.button[0].click().run()  # Submit Guess

    warnings = " ".join(w.value for w in at.warning)
    assert "Higher" in warnings
    assert "Lower" not in warnings


# --- FIXME: hardcoded range -> banner must reflect the chosen difficulty ----
def test_range_banner_matches_selected_difficulty():
    at = _run_app()
    at.selectbox[0].set_value("Easy").run()  # Easy range is 1..20
    banner = " ".join(i.value for i in at.info)
    assert "between 1 and 20" in banner


# --- FIXME: New Game secret must respect the difficulty range ---------------
def test_new_game_secret_within_difficulty_range():
    at = _run_app()
    at.selectbox[0].set_value("Easy").run()  # Easy range is 1..20
    at.button[1].click().run()  # New Game
    assert 1 <= at.session_state["secret"] <= 20
