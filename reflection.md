# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. Guess number are not checked/ can be out of range
  2. The hints is always "go higher" unless it is the exact number
  3. The New Game does not reset the entire game, it only reset the numbers of attempts left and the secret number
  4. Difficulty level of normal and hard is switched
  
  

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Bugs: fix the guess input range and data type
  Copilot Agent help me to set the input range base on the difficulties.
  During the testing part, there are few tests always failed, I asked AI to explain what is the reason to cause it fail. AI suggest to move all the reusable functions out of app.py and into logic_utils.py, which has no Stremlit imports. I was unsure, so I move it to the logic_utils.py and test it. All tests passed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When I try to ask AI to add the limit for the input range, it set the limite to 1 - 100, it does not adjust the range base on the difficulty level.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  By runing pytest, and manually testing on the website
- Describe at least one test you ran (manual or using pytest) 
  and what it showed you about your code.
   I switch around the difficulties of the level, and test the upper range, for example, if the range is 1 - 20, I test 21 and 20. Then, switch to "hard" level, and test 100 and 101. Do the same to the normal level. Then, try to test with negative number, empty input, and characters. 

   The error message display correctly. The input range is limited base on the difficulty level.
- Did AI help you design or understand any tests? How?
   Yes, it help me understand the test_winning_guess function in test_game_logic.py 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
