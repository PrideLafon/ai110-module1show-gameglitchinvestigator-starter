# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    When I first ran the game, it opened in the browser as a number guessing
game with a guess box, a "Show hints" checkbox, and a score. It looked
normal, but it behaved wrongly as soon as I started guessing. The hints
were backwards, bad inputs were accepted, nothing confirmed my guess when
hints were off, and the score behaved strangely.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  - **Reversed hints:** When I guessed a number higher than the secret, the
  game told me to go higher instead of lower.
- **No range validation:** I guessed -1 and 1000, which are outside the
  allowed range. The game accepted both as real guesses and gave reversed
  hints for them (-1 said "go lower" and 1000 said "go higher").
- **No feedback with hints off:** With "Show hints" unchecked, nothing
  told me whether my guess had been received.
- **Broken score:** The score went negative, and at some points it did
  not change at all after a guess.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input Used | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|------------|-------------------|-----------------|------------------------|-------------------------|
| A number higher than the secret | Hint tells me to go lower ("Too High") | Hint told me to go higher | none | `app.py`, `check_guess` (hint messages are swapped) |
| Guess of -1 | Rejected as out of range | Accepted; hint said "go lower" | none | `app.py`, `parse_guess` (no range check) |
| Guess of 1000 | Rejected as out of range | Accepted; hint said "go higher" | none | `app.py`, `parse_guess` (no range check) |
| Any guess with "Show hint" unchecked | Some confirmation that the guess was received | Nothing displayed | none | `app.py`, the `if show_hint:` block |
| Several wrong guesses in a row | Score only goes down on wrong guesses and never goes negative | Score went negative and sometimes did not change | none | `app.py`, `update_score` ("Too High" branch adds or subtracts 5 depending on attempt number) |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
