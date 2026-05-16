import streamlit as st

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
        "answer": "C) Paris"
    },
    {
        "question": "Which planet is closest to the sun?",
        "options": ["A) Venus", "B) Saturn", "C) Mercury", "D) Earth"],
        "answer": "C) Mercury"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["A) 5", "B) 7", "C) 8", "D) 6"],
        "answer": "D) 6"        
    },
    {
        "question": "What is 12 x 12?",
        "options": ["A) 144", "B) 124", "C) 148", "D) 132"],
        "answer": "A) 144"
    },
    {
        "question": "Which language runs in a web browser?",
        "options": ["A) Python", "B) Java", "C) C++", "D) JavaScript"],
        "answer": "D) JavaScript" 
    },
]

# Initialize session state
if "current" not in st.session_state:
    st.session_state.current = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "finished" not in st.session_state:
    st.session_state.finished = False

st.title("SP Trivia Quiz")

if st.session_state.finished:
    total = len(questions)
    score = st.session_state.score
    percentage= round((score / total) * 100)
    st.success(f"Quiz complete! You got {score} out of {total} correct ({percentage}%).")
    if st.button("Play Again"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.finished = False
        st.rerun()
    
else:
    q = questions[st.session_state.current]
    st.subheader(f"Question {st.session_state.current + 1} of {len(questions)}")
    st.write(q["question"])

    answer = st.radio("Choose your answer:", q["options"], index=None)

    if st.button("Submit"):
        if answer is None:
            st.warning("Please select an answer before submitting.")
        else:
            if answer == q["answer"]:
                st.session_state.score += 1
            st.session_state.current += 1
            if st.session_state.current >= len(questions):
                st.session_state.finished = True
            st.rerun()

            

