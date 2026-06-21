# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

Step 1: Launch the Game
Run the Streamlit app and you'll see the main interface with the title "🎮 Game Glitch Investigator" and a subtitle about being an "AI-generated guessing game. Something is off." (The subtitle keeps its charm even though the bugs are fixed!)

Step 2: Select Your Difficulty
In the left sidebar, choose your difficulty level:

Easy: Guess a number between 1-20 with 6 attempts

Normal: Guess a number between 1-100 with 8 attempts

Hard: Guess a number between 1-50 with 5 attempts

The sidebar will update to show your selected range and attempts allowed.

Step 3: Start a New Game
Click the "New Game" button to generate a secret number within your selected difficulty range. The game will display a success message confirming the new game has started.

Step 4: Enter Your Guess
Type your guess into the text input field and click "Submit Guess ". The game will:

Show a hint in a warning box (if "Show hint" is checked)

Track your remaining attempts

Update your score based on performance

Step 5: Use Hints Effectively
When you guess a number:

Too High: The game will tell you "Go LOWER!" (previously this was backwards!)

Too Low: The game will tell you " Go HIGHER!" (also fixed!)

Correct: You'll see " Correct!" and balloons will appear!

Step 6: Track Your Progress
As you play, you'll see:

Attempts left: Updates in real-time (no more off-by-one errors!)

Score: Accumulates points (100 points for first-guess win, minus 10 per attempt)

History: All your guesses are tracked and displayed

Step 7: Win or Lose
Win: If you guess the secret number, you'll see balloons and your final score

Lose: If you run out of attempts, the game will reveal the secret number and your final score

Step 8: Change Difficulty Mid-Game
You can switch difficulty at any time! The game will automatically:

Reset your attempts to 0

Reset your score to 0

Generate a new secret number within the new difficulty range

Provide a fresh start with the new settings

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
platform win32 -- Python 3.11.4, pytest-9.0.3, pluggy-1.6.0 -- C:\CodePath\ai110-module1show-gameglitchinvestigator-starter\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\CodePath\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 11 items

tests/test_game_logic.py::test_winning_guess PASSED                                                          [  9%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                         [ 18%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                          [ 27%]
tests/test_game_logic.py::test_changing_difficulty_resets_game_state PASSED                                  [ 36%]
tests/test_game_logic.py::test_changing_difficulty_gives_secret_in_new_range PASSED                          [ 45%]
tests/test_game_logic.py::test_attempts_left_never_negative PASSED                                           [ 54%]
tests/test_game_logic.py::test_attempts_start_at_zero PASSED                                                 [ 63%]
tests/test_game_logic.py::test_too_high_hint_tells_player_to_go_lower PASSED                                 [ 72%]
tests/test_game_logic.py::test_too_low_hint_tells_player_to_go_higher PASSED                                 [ 81%]
tests/test_game_logic.py::test_range_banner_matches_selected_difficulty PASSED                               [ 90%]
tests/test_game_logic.py::test_new_game_secret_within_difficulty_range PASSED                                [100%]
# ========================= 11 passed in 1.69s =========================
```
..............                                                     [100%]
14 passed in 3.73s


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
