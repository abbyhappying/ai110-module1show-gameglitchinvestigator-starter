# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude to identify three potential edge case inputs that might still break the Glitchy Guesser game and generate a comprehensive suite of pytest tests to verify they work correctly.

**What did the agent do?**

<!-- List the steps the agent took (files edited, commands run, etc.) -->
Step 1: The agent examined the existing code.
Step 2: The agent created the test functions for three edge cases.
Step 3: I runned the updated test_game_logic.py file

**What did you have to verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->
The agent works well, I manually update my input to verified the code is good.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Negative number input |can you identify potential edge case inputs of negative numbers that might still break the game, and generate a suite of `pytest` cases that verify the game handles these inputs0 |test_parse_negative_number_guess| Passed

| Decimal input |can you identify potential edge case inputs of decimals that might still break the game, and generate a suite of `pytest` cases that verify the game handles these inputs|Passed

| Extremely large integer input |can you identify potential edge case inputs of extremely large values that might still break the game, and generate a suite of `pytest` cases that verify the game handles these inputs|Passed|

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
<!-- Paste the prompt you gave the AI -->
```
can you identify three potential "edge case" inputs (e.g., negative numbers, decimals, or extremely large values) that might still break your game, and generate a suite of `pytest` cases that verify the game handles these inputs

**Linting output before:**

```
<!-- Paste relevant linter warnings/errors -->
```

**Changes applied:**

<!-- Describe what you changed based on the AI's suggestions -->

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
