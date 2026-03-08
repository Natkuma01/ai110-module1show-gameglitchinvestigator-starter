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

- ✅ Describe the game's purpose.
- ✅ Detail which bugs you found.
- ✅ Explain what fixes you applied.

## 📸 Demo
<img width="600" height="400" alt="Screenshot 2026-03-08 at 6 25 20 PM" src="https://github.com/user-attachments/assets/fe743424-6631-4927-8faf-4609b693b4b3" />
<img width="400" height="500" alt="Screenshot 2026-03-08 at 6 27 56 PM" src="https://github.com/user-attachments/assets/1db3ab53-f051-4d4c-bf29-889e3435c138" />


