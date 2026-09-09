"""
Quiz Generator Page
"""
import streamlit as st
from llm_service import LLMService
from prompts import QUIZ_GENERATION_PROMPT
from config import SUBJECTS, DIFFICULTY_LEVELS
import json

def show_quiz_generator(agent):
    st.markdown('<div class="main-header">❓ Quiz Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Generate practice quizzes to test your knowledge</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Input form
    col1, col2, col3 = st.columns(3)

    with col1:
        subject = st.selectbox("Subject", SUBJECTS[:-1])
    with col2:
        num_questions = st.slider("Number of questions", 2, 10, 5)
    with col3:
        difficulty = st.selectbox("Difficulty", DIFFICULTY_LEVELS, index=1)

    topic = st.text_input("Specific Topic", placeholder="e.g., Python OOP, Database Normalization, Machine Learning")

    if st.button("🎲 Generate Quiz", type="primary", use_container_width=True):
        if not topic:
            st.error("Please enter a topic for the quiz!")
        else:
            with st.spinner("🎯 Generating quiz questions..."):
                llm_service = LLMService()

                if llm_service.is_demo_mode():
                    # Demo quiz
                    quiz_data = {
                        "questions": [
                            {
                                "question": "What is the main purpose of normalization in databases?",
                                "options": {
                                    "A": "To increase database size",
                                    "B": "To reduce data redundancy and improve integrity",
                                    "C": "To make queries slower",
                                    "D": "To delete unnecessary data"
                                },
                                "correct_answer": "B",
                                "explanation": "Normalization is the process of organizing data to minimize redundancy and dependency, thereby improving data integrity."
                            },
                            {
                                "question": "Which normal form eliminates partial dependencies?",
                                "options": {
                                    "A": "First Normal Form (1NF)",
                                    "B": "Second Normal Form (2NF)",
                                    "C": "Third Normal Form (3NF)",
                                    "D": "Boyce-Codd Normal Form (BCNF)"
                                },
                                "correct_answer": "B",
                                "explanation": "Second Normal Form (2NF) removes partial dependencies, where non-key attributes depend on only part of the primary key."
                            },
                            {
                                "question": "In Python OOP, what is inheritance?",
                                "options": {
                                    "A": "A way to hide data",
                                    "B": "A mechanism where a class acquires properties from another class",
                                    "C": "A method to delete objects",
                                    "D": "A type of variable"
                                },
                                "correct_answer": "B",
                                "explanation": "Inheritance allows a class (child) to inherit attributes and methods from another class (parent), promoting code reuse."
                            },
                            {
                                "question": "What type of learning uses labeled data?",
                                "options": {
                                    "A": "Unsupervised Learning",
                                    "B": "Reinforcement Learning",
                                    "C": "Supervised Learning",
                                    "D": "Transfer Learning"
                                },
                                "correct_answer": "C",
                                "explanation": "Supervised learning trains models on labeled data where the correct output is known for each input."
                            },
                            {
                                "question": "Which data structure follows LIFO principle?",
                                "options": {
                                    "A": "Queue",
                                    "B": "Stack",
                                    "C": "Array",
                                    "D": "Linked List"
                                },
                                "correct_answer": "B",
                                "explanation": "A Stack follows Last-In-First-Out (LIFO) principle, where the last element added is the first one removed."
                            }
                        ]
                    }

                    display_quiz(quiz_data, agent, num_questions)

                else:
                    # Real API call
                    prompt = QUIZ_GENERATION_PROMPT.format(
                        topic=topic,
                        num_questions=num_questions,
                        difficulty=difficulty
                    )

                    try:
                        quiz_data = llm_service.generate_json_response(prompt, f"Generate quiz on {topic}")

                        if "error" in quiz_data:
                            st.error(quiz_data["error"])
                        else:
                            display_quiz(quiz_data, agent, num_questions)

                    except Exception as e:
                        st.error(f"Error generating quiz: {str(e)}")

def display_quiz(quiz_data, agent, num_questions):
    """Display the generated quiz"""
    st.success(f"✅ Quiz Generated! ({num_questions} questions)")
    st.markdown("---")

    # Initialize session state for answers
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    questions = quiz_data.get("questions", [])[:num_questions]

    # Display questions
    for idx, q in enumerate(questions, 1):
        st.markdown(f"### Question {idx}")
        st.markdown(f"**{q['question']}**")

        # Answer options
        answer_key = f"q_{idx}"
        options_list = [f"{k}: {v}" for k, v in q['options'].items()]

        selected = st.radio(
            f"Select your answer for Question {idx}:",
            options_list,
            key=answer_key,
            disabled=st.session_state.quiz_submitted
        )

        if selected:
            st.session_state.quiz_answers[idx] = selected[0]  # Store just the letter (A, B, C, D)

        st.markdown("---")

    # Submit button
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("✅ Submit Quiz", disabled=st.session_state.quiz_submitted):
            st.session_state.quiz_submitted = True
            agent.analytics.log_quiz_generation()
            st.rerun()

    with col2:
        if st.button("🔄 Generate New Quiz"):
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.rerun()

    # Show results if submitted
    if st.session_state.quiz_submitted:
        st.markdown("---")
        st.markdown("## 📊 Quiz Results")

        correct_count = 0
        total_questions = len(questions)

        for idx, q in enumerate(questions, 1):
            user_answer = st.session_state.quiz_answers.get(idx, "")
            correct_answer = q['correct_answer']

            is_correct = user_answer == correct_answer
            if is_correct:
                correct_count += 1

            # Display result for each question
            if is_correct:
                st.success(f"✅ Question {idx}: Correct!")
            else:
                st.error(f"❌ Question {idx}: Incorrect")
                st.info(f"**Correct Answer:** {correct_answer}")

            st.markdown(f"**Explanation:** {q['explanation']}")
            st.markdown("---")

        # Overall score
        score_percentage = (correct_count / total_questions) * 100
        st.markdown(f"### 🎯 Final Score: {correct_count}/{total_questions} ({score_percentage:.1f}%)")

        if score_percentage >= 80:
            st.balloons()
            st.success("🌟 Excellent work! You have a strong understanding of this topic!")
        elif score_percentage >= 60:
            st.info("👍 Good job! Review the explanations to strengthen your understanding.")
        else:
            st.warning("📚 Keep practicing! Review the topic and try again.")

    # Example topics
    st.markdown("---")
    with st.expander("💡 Example Quiz Topics"):
        st.markdown("""
        **Python:**
        - Python Basics
        - Python OOP
        - Python Data Structures
        - Exception Handling
        - File Operations

        **DBMS:**
        - Database Normalization
        - SQL Queries and Joins
        - Transactions and Concurrency
        - Indexing and Optimization

        **Data Structures:**
        - Arrays and Linked Lists
        - Stacks and Queues
        - Trees and Graphs
        - Sorting Algorithms
        - Searching Algorithms

        **Machine Learning:**
        - ML Fundamentals
        - Supervised Learning
        - Classification vs Regression
        - Neural Networks Basics
        """)
