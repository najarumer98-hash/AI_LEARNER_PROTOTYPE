"""
Study Planner Page
"""
import streamlit as st
from llm_service import LLMService
from prompts import STUDY_PLAN_PROMPT
from config import SUBJECTS, DIFFICULTY_LEVELS

def show_study_planner(agent):
    st.markdown('<div class="main-header">📚 Study Planner</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Create a personalized study plan</div>', unsafe_allow_html=True)

    st.markdown("""
    Generate a structured study plan tailored to your learning needs.
    Specify your subject, topics, and time constraints to get a day-by-day study schedule.
    """)

    st.markdown("---")

    # Input form
    col1, col2 = st.columns(2)

    with col1:
        subject = st.selectbox("Subject", SUBJECTS[:-1])  # Exclude "General"
        topics = st.text_area(
            "Topics to cover (comma-separated)",
            placeholder="e.g., Functions, Classes, Inheritance, Polymorphism",
            height=100
        )
        num_days = st.slider("Number of days", 1, 30, 7)

    with col2:
        daily_hours = st.slider("Daily study hours", 1, 8, 2)
        difficulty = st.selectbox("Difficulty Level", DIFFICULTY_LEVELS, index=1)

    if st.button("🎯 Generate Study Plan", type="primary", use_container_width=True):
        if not topics:
            st.error("Please enter the topics you want to study!")
        else:
            with st.spinner("📝 Creating your personalized study plan..."):
                llm_service = LLMService()

                if llm_service.is_demo_mode():
                    # Demo response
                    st.success("✅ Study Plan Generated!")
                    st.markdown("---")

                    st.markdown(f"""
                    ## {num_days}-Day Study Plan: {subject}
                    **Daily Study Time**: {daily_hours} hours | **Level**: {difficulty}

                    ### Day 1: Foundations
                    - Introduction to core concepts
                    - Setup and environment preparation
                    - **Duration**: {daily_hours} hours
                    - **Activities**: Reading, setup, basic exercises

                    ### Day 2: Fundamentals
                    - Deep dive into basic principles
                    - Hands-on practice with examples
                    - **Duration**: {daily_hours} hours
                    - **Activities**: Tutorial completion, coding practice

                    ### Day 3: Intermediate Concepts
                    - Build on foundational knowledge
                    - Work on practical problems
                    - **Duration**: {daily_hours} hours
                    - **Activities**: Problem-solving, mini-projects

                    ### Day 4: Advanced Topics
                    - Explore complex concepts
                    - Integration and application
                    - **Duration**: {daily_hours} hours
                    - **Activities**: Advanced exercises, reading

                    ### Day 5: Practice & Application
                    - Apply learned concepts
                    - Build small projects
                    - **Duration**: {daily_hours} hours
                    - **Activities**: Project work, coding challenges

                    ### Day 6: Review & Reinforcement
                    - Review all covered topics
                    - Fill knowledge gaps
                    - **Duration**: {daily_hours} hours
                    - **Activities**: Revision, practice tests

                    ### Day 7: Assessment & Project
                    - Final review
                    - Complete a comprehensive project
                    - Self-assessment
                    - **Duration**: {daily_hours} hours
                    - **Activities**: Project completion, testing

                    ### 📝 Study Tips:
                    - Take 10-minute breaks every hour
                    - Practice coding daily, don't just read
                    - Join online communities for help
                    - Document your learning journey
                    - Review previous day's content before starting new topics

                    ### 🎯 Success Metrics:
                    - Complete all daily activities
                    - Finish at least 2-3 mini-projects
                    - Test knowledge with quizzes
                    - Build confidence in applying concepts
                    """)

                    # Log analytics
                    agent.analytics.log_study_plan()

                else:
                    # Real API call
                    prompt = STUDY_PLAN_PROMPT.format(
                        subject=subject,
                        topics=topics,
                        days=num_days,
                        hours=daily_hours,
                        difficulty=difficulty
                    )

                    response = llm_service.generate_response(prompt, f"Create a {num_days}-day study plan")

                    st.success("✅ Study Plan Generated!")
                    st.markdown("---")
                    st.markdown(response)

                    # Log analytics
                    agent.analytics.log_study_plan()

    # Show example
    st.markdown("---")
    with st.expander("💡 Example Study Plan Topics"):
        st.markdown("""
        **Python:**
        - Variables, Data Types, Operators
        - Control Flow, Loops
        - Functions, Lambda Functions
        - OOP: Classes, Objects, Inheritance
        - File Handling, Exception Handling

        **DBMS:**
        - ER Modeling
        - Relational Model
        - Normalization (1NF, 2NF, 3NF)
        - SQL Queries, Joins
        - Transactions, Concurrency

        **Data Structures:**
        - Arrays, Linked Lists
        - Stacks, Queues
        - Trees (Binary, BST, AVL)
        - Graphs, Graph Traversal
        - Sorting and Searching Algorithms

        **Machine Learning:**
        - Supervised vs Unsupervised Learning
        - Linear Regression
        - Classification Algorithms
        - Neural Networks Basics
        - Model Evaluation
        """)
