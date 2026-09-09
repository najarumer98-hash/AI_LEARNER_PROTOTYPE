"""
Quiz Generator Page
"""

import streamlit as st
from llm_service import LLMService
from prompts import QUIZ_GENERATION_PROMPT
from config import SUBJECTS, DIFFICULTY_LEVELS


def show_quiz_generator(agent):
    """Display the Quiz Generator page."""

    st.markdown(
        '<div class="main-header">❓ Quiz Generator</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sub-header">'
        'Generate practice quizzes to test your knowledge'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    # =========================================================
    # INITIALIZE SESSION STATE
    # =========================================================

    if "quiz_data" not in st.session_state:
        st.session_state.quiz_data = None

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    if "quiz_answers" not in st.session_state:
        st.session_state.quiz_answers = {}

    # =========================================================
    # QUIZ SETTINGS
    # =========================================================

    col1, col2, col3 = st.columns(3)

    with col1:
        subject = st.selectbox(
            "Subject",
            SUBJECTS[:-1],
            key="quiz_subject"
        )

    with col2:
        num_questions = st.slider(
            "Number of questions",
            2,
            10,
            5,
            key="quiz_num_questions"
        )

    with col3:
        difficulty = st.selectbox(
            "Difficulty",
            DIFFICULTY_LEVELS,
            index=1,
            key="quiz_difficulty"
        )

    topic = st.text_input(
        "Specific Topic",
        placeholder=(
            "e.g., Python OOP, Database Normalization, "
            "Machine Learning"
        ),
        key="quiz_topic"
    )

    # =========================================================
    # GENERATE QUIZ
    # =========================================================

    if st.button(
        "🎲 Generate Quiz",
        type="primary",
        use_container_width=True
    ):

        if not topic.strip():
            st.error("Please enter a topic for the quiz!")

        else:
            with st.spinner("🎯 Generating quiz questions..."):

                llm_service = LLMService()

                # -------------------------------------------------
                # DEMO MODE
                # -------------------------------------------------

                if llm_service.is_demo_mode():

                    quiz_data = {
                        "questions": [
                            {
                                "question": (
                                    "What is the main purpose "
                                    "of normalization in databases?"
                                ),
                                "options": {
                                    "A": "To increase database size",
                                    "B": (
                                        "To reduce data redundancy "
                                        "and improve integrity"
                                    ),
                                    "C": "To make queries slower",
                                    "D": "To delete unnecessary data"
                                },
                                "correct_answer": "B",
                                "explanation": (
                                    "Normalization organizes database "
                                    "tables to reduce redundancy and "
                                    "improve data integrity."
                                )
                            },
                            {
                                "question": (
                                    "Which normal form eliminates "
                                    "partial dependencies?"
                                ),
                                "options": {
                                    "A": "First Normal Form (1NF)",
                                    "B": "Second Normal Form (2NF)",
                                    "C": "Third Normal Form (3NF)",
                                    "D": (
                                        "Boyce-Codd Normal Form (BCNF)"
                                    )
                                },
                                "correct_answer": "B",
                                "explanation": (
                                    "2NF removes partial dependencies "
                                    "of non-key attributes on part of "
                                    "a composite key."
                                )
                            },
                            {
                                "question": (
                                    "In Python OOP, what is inheritance?"
                                ),
                                "options": {
                                    "A": "A way to hide data",
                                    "B": (
                                        "A mechanism where a class "
                                        "acquires properties from "
                                        "another class"
                                    ),
                                    "C": "A method to delete objects",
                                    "D": "A type of variable"
                                },
                                "correct_answer": "B",
                                "explanation": (
                                    "Inheritance allows a child class "
                                    "to acquire attributes and methods "
                                    "from a parent class."
                                )
                            },
                            {
                                "question": (
                                    "What type of learning uses "
                                    "labeled data?"
                                ),
                                "options": {
                                    "A": "Unsupervised Learning",
                                    "B": "Reinforcement Learning",
                                    "C": "Supervised Learning",
                                    "D": "Transfer Learning"
                                },
                                "correct_answer": "C",
                                "explanation": (
                                    "Supervised learning uses labeled "
                                    "training data where the expected "
                                    "output is known."
                                )
                            },
                            {
                                "question": (
                                    "Which data structure follows "
                                    "the LIFO principle?"
                                ),
                                "options": {
                                    "A": "Queue",
                                    "B": "Stack",
                                    "C": "Array",
                                    "D": "Linked List"
                                },
                                "correct_answer": "B",
                                "explanation": (
                                    "A stack follows Last-In-First-Out "
                                    "(LIFO)."
                                )
                            }
                        ]
                    }

                # -------------------------------------------------
                # LIVE OMNIROUTE
                # -------------------------------------------------

                else:

                    prompt = QUIZ_GENERATION_PROMPT.format(
                        topic=topic,
                        num_questions=num_questions,
                        difficulty=difficulty
                    )

                    try:

                        quiz_data = (
                            llm_service.generate_json_response(
                                prompt,
                                f"Generate quiz on {topic}"
                            )
                        )

                        if not isinstance(quiz_data, dict):
                            st.error(
                                "The AI returned an invalid quiz format."
                            )
                            return

                        if "error" in quiz_data:
                            st.error(quiz_data["error"])
                            return

                    except Exception as e:
                        st.error(
                            f"Error generating quiz: {str(e)}"
                        )
                        return

                # -------------------------------------------------
                # SAVE QUIZ IN SESSION STATE
                # -------------------------------------------------

                st.session_state.quiz_data = quiz_data
                st.session_state.quiz_submitted = False
                st.session_state.quiz_answers = {}

                st.rerun()

    # =========================================================
    # DISPLAY SAVED QUIZ
    # =========================================================

    if st.session_state.quiz_data:

        display_quiz(
            st.session_state.quiz_data,
            agent,
            num_questions
        )


# =============================================================
# DISPLAY QUIZ
# =============================================================

def display_quiz(quiz_data, agent, num_questions):
    """Display generated quiz and handle submission."""

    st.success(
        f"✅ Quiz Generated! ({num_questions} questions)"
    )

    st.markdown("---")

    questions = quiz_data.get("questions", [])

    if not questions:
        st.error("No quiz questions were generated.")
        return

    questions = questions[:num_questions]

    # =========================================================
    # SUBMITTED STATE
    # =========================================================

    if st.session_state.quiz_submitted:

        show_quiz_results(
            questions,
            agent
        )

    # =========================================================
    # ACTIVE QUIZ
    # =========================================================

    else:

        # -----------------------------------------------------
        # FORM
        # -----------------------------------------------------

        with st.form("quiz_answer_form"):

            for idx, q in enumerate(questions, 1):

                st.markdown(f"### Question {idx}")

                st.markdown(
                    f"**{q.get('question', 'Question unavailable')}**"
                )

                options = q.get("options", {})

                # Convert dictionary options into display list
                if isinstance(options, dict):

                    options_list = [
                        f"{key}: {value}"
                        for key, value in options.items()
                    ]

                else:

                    options_list = options

                # Make sure there are options
                if not options_list:
                    st.warning(
                        f"No options available for Question {idx}."
                    )
                    continue

                # -------------------------------------------------
                # RADIO BUTTON
                # -------------------------------------------------

                selected = st.radio(
                    f"Select your answer for Question {idx}:",
                    options_list,
                    index=None,
                    key=f"quiz_question_{idx}"
                )

                # Save answer only when user selected one
                if selected:
                    st.session_state.quiz_answers[idx] = selected

                st.markdown("---")

            # -------------------------------------------------
            # SUBMIT BUTTON
            # -------------------------------------------------

            submitted = st.form_submit_button(
                "✅ Submit Quiz",
                use_container_width=True
            )

        # -----------------------------------------------------
        # PROCESS SUBMISSION
        # -----------------------------------------------------

        if submitted:

            # Check if all questions are answered
            unanswered = []

            for idx in range(1, len(questions) + 1):

                if idx not in st.session_state.quiz_answers:
                    unanswered.append(idx)

            if unanswered:

                st.warning(
                    "⚠️ Please answer all questions before submitting."
                )

            else:

                st.session_state.quiz_submitted = True

                try:
                    agent.analytics.log_quiz_generation()
                except Exception:
                    pass

                st.rerun()

    # =========================================================
    # GENERATE NEW QUIZ
    # =========================================================

    st.markdown("---")

    if st.button(
        "🔄 Generate New Quiz",
        use_container_width=True
    ):

        st.session_state.quiz_data = None
        st.session_state.quiz_answers = {}
        st.session_state.quiz_submitted = False

        # Remove old radio selections
        for key in list(st.session_state.keys()):
            if key.startswith("quiz_question_"):
                del st.session_state[key]

        st.rerun()


# =============================================================
# QUIZ RESULTS
# =============================================================

def show_quiz_results(questions, agent):
    """Display quiz results after submission."""

    st.markdown("---")

    st.markdown("## 📊 Quiz Results")

    correct_count = 0
    total_questions = len(questions)

    # =========================================================
    # CHECK EACH QUESTION
    # =========================================================

    for idx, q in enumerate(questions, 1):

        user_answer = st.session_state.quiz_answers.get(
            idx,
            ""
        )

        # Extract only option letter
        if user_answer:
            user_letter = user_answer.split(":")[0].strip()
        else:
            user_letter = ""

        correct_answer = str(
            q.get("correct_answer", "")
        ).strip()

        is_correct = (
            user_letter.upper() ==
            correct_answer.upper()
        )

        if is_correct:

            correct_count += 1

            st.success(
                f"✅ Question {idx}: Correct!"
            )

        else:

            st.error(
                f"❌ Question {idx}: Incorrect"
            )

            correct_text = q.get(
                "options",
                {}
            ).get(
                correct_answer,
                correct_answer
            )

            st.info(
                f"**Correct Answer:** "
                f"{correct_answer}: {correct_text}"
            )

        explanation = q.get(
            "explanation",
            "No explanation available."
        )

        st.markdown(
            f"**Explanation:** {explanation}"
        )

        st.markdown("---")

    # =========================================================
    # FINAL SCORE
    # =========================================================

    if total_questions > 0:

        score_percentage = (
            correct_count / total_questions
        ) * 100

    else:

        score_percentage = 0

    st.markdown(
        f"### 🎯 Final Score: "
        f"{correct_count}/{total_questions} "
        f"({score_percentage:.1f}%)"
    )

    # =========================================================
    # PERFORMANCE MESSAGE
    # =========================================================

    if score_percentage >= 80:

        st.balloons()

        st.success(
            "🌟 Excellent work! You have a strong "
            "understanding of this topic!"
        )

    elif score_percentage >= 60:

        st.info(
            "👍 Good job! Review the explanations "
            "to strengthen your understanding."
        )

    else:

        st.warning(
            "📚 Keep practicing! Review the topic "
            "and try again."
        )


# =============================================================
# EXAMPLE TOPICS
# =============================================================

    st.markdown("---")

    with st.expander("💡 Example Quiz Topics"):

        st.markdown(
            """
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
"""
        )