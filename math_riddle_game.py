import streamlit as st
import random

# Full list of questions (all 10)
math_mcq_riddles = [
    {
        "question": "Which quadratic equation represents the area of a square with side length x, if the area is 289 m²?",
        "choices": ["x² - 17x = 289", "x² + 17² = 0", "(x + 17)² = 0", "x² - 289 = 0"],
        "answer": "x² - 289 = 0",
        "hint": "Area of square is x². Rearranged to standard form.",
        "explanation": "Area = x² → x² = 289 → x² - 289 = 0 is the correct form."
    },
    {
        "question": "Solve the quadratic: (x + 1)(x + 2) = -2x(x + 2)",
        "choices": ["x = 1, x = -2/3", "x = -1, x = -2/3", "x = -1, x = 2/3", "x = 1, x = 2/3"],
        "answer": "x = 1, x = -2/3",
        "hint": "Expand both sides and simplify before solving.",
        "explanation": "x² + 3x + 2 = -2x² - 4x → move everything to one side and solve: x = 1 and -2/3."
    },
    {
        "question": "Convert binary number 1101₂ to base 10.",
        "choices": ["14", "11", "13", "15"],
        "answer": "13",
        "hint": "Use place values: 1×8 + 1×4 + 0×2 + 1×1.",
        "explanation": "1×8 + 1×4 + 0×2 + 1×1 = 13."
    },
    {
        "question": "Given P = {1,3,5,7,9} and R = {1,4,9}, what is P ∩ R?",
        "choices": ["1, 4", "3, 7", "1, 9", "4, 9"],
        "answer": "1, 9",
        "hint": "Intersection = common elements.",
        "explanation": "Common elements in both sets: {1, 9}."
    },
    {
        "question": "In a graph, a vertex has a loop. What is the degree of that vertex?",
        "choices": ["1", "2", "3", "0"],
        "answer": "2",
        "hint": "A loop adds 2 to the degree.",
        "explanation": "In graph theory, a loop contributes two to the degree."
    },
    {
        "question": "What is the range of this data set: 10, 5, 8, 18, 22, 12?",
        "choices": ["15", "17", "13", "12"],
        "answer": "17",
        "hint": "Range = Max - Min.",
        "explanation": "Range = 22 - 5 = 17."
    },
    {
        "question": "A fair coin and a die are tossed. How many total outcomes are there?",
        "choices": ["6", "10", "12", "14"],
        "answer": "12",
        "hint": "2 outcomes × 6 outcomes.",
        "explanation": "Coin (2) × Die (6) = 12 outcomes."
    },
    {
        "question": "Find the roots of the equation x² + x - 6 = 0",
        "choices": ["x = 3, x = -2", "x = 2, x = -3", "x = -3, x = -2", "x = 1, x = -6"],
        "answer": "x = 2, x = -3",
        "hint": "Factor: (x + 3)(x - 2).",
        "explanation": "x² + x - 6 = (x + 3)(x - 2) → x = -3, 2."
    },
    {
        "question": "Express 2(64) + 24 + 6 in base 7.",
        "choices": ["10423", "7044", "5066", "3524"],
        "answer": "5066",
        "hint": "Convert total from base 10 to base 7.",
        "explanation": "2×64 + 24 + 6 = 158 → 5066 (base 7)."
    },
    {
        "question": "The arrow follows a quadratic path: f(x) = -13/200 x² + 39/20 x. What is its maximum height?",
        "choices": ["1.6", "2.1", "1.95", "2.5"],
        "answer": "1.95",
        "hint": "Find vertex: x = -b/2a, then compute f(x).",
        "explanation": "x = 1.5 → f(1.5) = 1.95 (max height)."
    }
]

# Streamlit setup
st.set_page_config(page_title="Math Riddle Game", layout="centered")
st.title("🧠 Math Riddle Game")
st.markdown("Solve math puzzles and earn points! Get bonus points for streaks!")

# Session state
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.hints_used = 0
    st.session_state.used_hint = False
    st.session_state.correct_streak = 0
    st.session_state.questions = random.sample(math_mcq_riddles, len(math_mcq_riddles))

# Quiz logic
if st.session_state.index < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.index]
    st.markdown(f"### Q{st.session_state.index + 1}: {q['question']}")
    choice = st.radio("Choose one:", q["choices"], key=st.session_state.index)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Submit Answer"):
            if choice == q["answer"]:
                points = 5 if st.session_state.used_hint else 10
                st.session_state.correct_streak += 1
                if st.session_state.correct_streak == 3:
                    points += 5
                    st.success(f"🔥 Streak Bonus! Correct! +{points} points")
                    st.session_state.correct_streak = 0
                else:
                    st.success(f"✅ Correct! +{points} points")
                st.session_state.score += points
            else:
                st.error(f"❌ Wrong! Correct answer: {q['answer']}")
                st.info(f"📘 {q['explanation']}")
                st.session_state.correct_streak = 0

            st.session_state.index += 1
            st.session_state.used_hint = False
            st.experimental_rerun()

    with col2:
        if st.button("💡 Show Hint"):
            if st.session_state.hints_used < 3:
                st.session_state.hints_used += 1
                st.session_state.used_hint = True
                st.info(f"Hint: {q['hint']}")
            else:
                st.warning("⚠️ No more hints available.")

    st.markdown(f"🎯 Score: `{st.session_state.score}` &nbsp;&nbsp;&nbsp; 💬 Hints used: `{st.session_state.hints_used}/3`")

else:
    st.balloons()
    st.success(f"🎉 Quiz Complete! Your final score is: {st.session_state.score}")
    if st.button("🔁 Restart Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.experimental_rerun()
