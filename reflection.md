# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  <br> The game take any integer or character for user input to guess a number. After submitting the guess, the hint message is not helpful.
  The secret number is already displayed, so the user does not need to take any guesses. When "New Game" is clicked, the score still remains the same.
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. Guess numbers are not checked/ can be out of range
  2. The hint is always "go higher" unless it is the exact number
  3. The New Game does not reset the entire game, it only resets the number of attempts left and the secret number
  4. The difficulty level of normal and hard is switched
  
  

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  <br> Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  <br> Bugs: fix the guess input range and data type
  <br> Copilot Agent help me to set the input range base on the difficulties.
  <br> During the testing part, there are a few tests that always fail. I asked AI to explain the reason for its failure. AI suggest to move all the reusable functions out of app.py and into logic_utils.py, which has no Stremlit imports. I was unsure, so I moved it to the logic_utils.py and tested it. All tests passed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  <br> When I try to ask AI to add the limit for the input range, it sets the limit to 1 - 100, it does not adjust the range based on the difficulty level.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  <br> By runing pytest, and manually testing on the website
- Describe at least one test you ran (manual or using pytest) 
  and what it showed you about your code.
   <br> I switch around the difficulties of the level, and test the upper range, for example, if the range is 1 - 20, I test 21 and 20. Then, switch to "hard" level, and test 100 and 101. Do the same to the normal level. Then, try to test with negative number, empty input, and characters. 

   The error message displays correctly. The input range is limited based on the difficulty level.
- Did AI help you design or understand any tests? How?
   <br> Yes, it helps me understand the test_winning_guess function in test_game_logic.py 

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  <br> Because New Game is pressed, so need to change another guessing target
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  <br> "reruns" is like refreshing a page, restart a page
  <br> session state is a temporary memory that even after reruns, it does not change, remains the same
- What change did you make that finally gave the game a stable secret number?
  <br> The number was stable for secret number, unless the "New Game" button is clicked
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  <br> ( This could be a testing habit, a prompting strategy, or a way you used Git. )
  <br> Manual test the app first
  <br> When reading the code, any unclear block, ask AI to explain the logic, and see if the logic is it correct
  <br> Mark "FIXME" on the code that looks buggy
- What is one thing you would do differently next time you work with AI on a coding task?
  <br> I will ask for the suggestion on how to solve and issue
  ask AI to explain the cause of the error, and try to understand the reason rather than just let AI solve it without  
  understanding.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  <br> I think when integrating all blocks of code, the blocks do not connect, so it causes all the bugs. Some of the functions do 
  not need to be used, such as the even/odd feature that changes the number to a string. And logical issues, such as the hint message after each guess.
  The suggestion of "Go HIGHER" and "Go LOWER" flip around.
