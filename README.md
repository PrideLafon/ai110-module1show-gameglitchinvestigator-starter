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

**Purpose of the game:** A number guessing game built with Streamlit. The
player guesses a secret number within a range set by the difficulty
level, and the game gives higher/lower hints and tracks attempts and a
score. The starter version was AI-generated and contained several bugs.

**Bugs I found:**
- The hints were reversed: a guess above the secret said "Go HIGHER".
- Out-of-range guesses (such as -1 and 1000) were accepted as real guesses.
- On even-numbered attempts, `app.py` converted the secret to a string,
  so the number-vs-text comparison gave unreliable results.
- With "Show hint" unchecked, nothing confirmed that a guess was received.
- The score could go negative, and wrong guesses sometimes added points.
- The "Attempts left" counter is off by one, and the info box always says
  1 to 100 regardless of difficulty.

**Fixes I applied:**
- Fixed the swapped hint messages in `check_guess`.
- Added range validation to `parse_guess`, so guesses outside the
  difficulty's range are rejected with an error message.
- Removed the `str(secret)` conversion in `app.py`, so the real number
  is always passed to `check_guess`.
- Moved the game logic from `app.py` into `logic_utils.py`.
- Rewrote the starter tests so they unpack the `(outcome, message)` pair
  that `check_guess` returns, and added a test for range validation.

**Known issues I did not fix:** the score logic (`update_score`), the
missing confirmation when hints are off, and the attempts-left counter.

## 📸 Demo Walkthrough

Example game on Normal difficulty (range 1 to 100), where the secret
number is 64:

1. The user enters a guess of 40, and the game shows "Go HIGHER!".
2. The user enters a guess of 90, and the game shows "Go LOWER!".
3. The user enters a guess of 1000, and the game shows an error saying
   the guess must be between 1 and 100.
4. The user enters a guess of 64, and the game shows a balloons animation
   and a message saying they won, along with the secret and final score.
5. Any further guess is blocked until the user clicks "New Game".

## 🧪 Test Results

```
collected 4 items

tests/test_game_logic.py ....                               [100%]

======================== 4 passed in 0.02s ========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
