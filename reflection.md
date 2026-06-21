# 💭 Reflection: Game Glitch Investigator

As I started playing, I noticed the hints were completely misleading. When I guessed too high, the game told me to go higher, and when I guessed too low, it told me to go lower. The difficulty settings also didn't seem to work properly - Hard mode showed a range of 1-100 instead of 1-50, and the attempt counter was always off by one. The game was essentially unplayable because the hints were actively pushing me in the wrong direction.

## 1. What was broken when you started?

1. the hints were backwards"
2. The difficulty range display was wrong - When I selected Hard mode, the sidebar correctly showed "Range: 1 to 50" but the main game area still said "Guess a number between 1 and 100" which was confusing and contradictory.

3. The attempt counter was wrong - In Hard mode, the sidebar showed "Attempts allowed: 5" but the game displayed "Attempts left: 4" before I even made a single guess.

4.Change difficulty in sidebar doesn't reset attempts and score

5. When we start a new game, the secret number does not change

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|

|Select Hard difficulty	|shows Guess a number between 1 and 50.	|shows Guess a number between 1 and 100.	"none"|
|Click ""New Game"|	when we start a new game, the secret number respect the difficulty range user selected	|the secret number is always between 1-100	|none|
|2nd, 4th, 6th attempt|	Correct hint based on actual number|	Hint is incorrect due to string comparison|none|
|Choose hard difficulity|	Attempt left should be 5	|Attempt left shows 4	|none
|Guess>secret|	Show Too high, go lower|	Too high, go higher|	none|
|Change difficulty in sidebar|	Attempt, score and secret reset	|Shows previous attempt and score	|none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (Claude)?
- Give one example of an AI suggestion that was correct:
AI suggested should change fixed hardcoded range display - AI suggested using f-string with {low} and {high},I verified this by updating the code and testing the game
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Initially, the AI suggested using float() comparisons to handle decimal inputs more gracefully.I noticed float comparisons can have precision issues.
I tested with input "5.5" → The game should reject this or round it.
The AI's suggestion would have accepted "5.5" and compared it to the secret.I confirmed that the original parse_guess() function correctly converts decimal inputs to integers by using int(float(raw)).The AI's suggestion would have unnecessarily complicated the code
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I did manual test after fix each bug to check if it meet my expectation.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  I select "Hard" in sidebar to check main display, it's expected to "Guess a number between 1 and 50" and the page meet my expectation.
  I select Easy, make some guesses (attempts: 3) and switch to Hard to check attempts, it's reset.
- Did AI help you design or understand any tests? How?
  AI help me generated test_game_logic.py to run all the test cases and it passed.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

The entire Python script runs from top to bottom again which is rerun. But when the script reruns, all your variables reset to their original values. So if you had a counter that was at 5, it would go back to 0 when the page reloads. st.session_state like a sticky note you attach to the recipe book that remembers things between reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to continue using systematic bug tracking with a reproduction log. Creating a structured table with columns for "Input," "Expected Behavior," "Actual Behavior," and "Console Output" helped me stay organized and ensure I wasn't missing any issues. Instead of randomly trying to fix bugs, I had a clear list of what needed to be addressed, and I could work through them one by one. This approach also helped me communicate more clearly with the AI assistant because I could point to specific bugs with exact reproduction steps. For example, when I noticed the attempt counter was wrong, I could say "Bug #5: In Hard mode, attempts left shows 4 instead of 5 before any guesses" and the AI could immediately understand what I was talking about.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
Next time, I would start with a test plan before asking for fixes. In this project, I started playing the game and noticing bugs, then asked the AI for solutions one at a time. I should have first created a comprehensive test plan covering all features and difficulty levels, then systematically tested everything and documented all bugs upfront. This would have given me a complete picture of what was broken before I started fixing things.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project taught me that AI can generate code that looks functional and well-structured on the surface, but it may have subtle logical errors that make the application completely unusable. I now understand that AI-generated code should always be verified before apply it.
