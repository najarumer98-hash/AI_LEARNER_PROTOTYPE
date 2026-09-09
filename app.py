"""
AI Learner Assistant - Main Streamlit Application
"""
import streamlit as st
from agent import LearnerAgent
from config import APP_TITLE, APP_DESCRIPTION, DEMO_MODE, DIFFICULTY_LEVELS, RESPONSE_STYLES, SUBJECTS
import json

# Page configuration
st.set_page_config(
    page_title="AI Learner Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .demo-badge {
        background-color: #ff6b6b;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 5px;
        font-weight: bold;
        text-align: center;
        margin: 1rem 0;
    }
    .agent-decision {
        background-color: #f0f8ff;
        border-left: 4px solid #1f77b4;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .escalation-warning {
        background-color: #fff3cd;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .resource-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border: 1px solid #dee2e6;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 2rem;
    }
    .assistant-message {
        background-color: #f5f5f5;
        margin-right: 2rem;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'agent' not in st.session_state:
    st.session_state.agent = LearnerAgent()
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Sidebar
with st.sidebar:
    st.markdown("## 🎓 AI Learner Assistant")
    st.markdown("---")

    # Demo mode warning
    if DEMO_MODE:
        st.warning("⚠️ **DEMO MODE**\n\nAdd your OpenAI API key in `.env` file for live AI responses.")

    st.markdown("### Navigation")
    page = st.radio(
        "Go to",
        ["💬 Chat", "📚 Study Planner", "❓ Quiz Generator", "📝 Notes & Summary", "📖 Resources", "📊 Analytics", "ℹ️ About"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Settings
    st.markdown("### Settings")
    difficulty = st.selectbox("Difficulty Level", DIFFICULTY_LEVELS, index=1)
    response_style = st.selectbox("Response Style", RESPONSE_STYLES, index=1)
    subject = st.selectbox("Subject", SUBJECTS, index=8)

    st.markdown("---")

    # Limitations
    with st.expander("⚠️ Limitations & Safety"):
        st.markdown("""
        **Important Limitations:**
        - AI may hallucinate or provide incorrect information
        - Always verify critical academic information
        - Cannot access your university records
        - Cannot make official academic decisions
        - Cannot change grades or policies
        - Responses may be outdated

        **When to Contact Faculty:**
        - Grading disputes
        - Official academic decisions
        - Institution-specific policies
        - Personal academic records
        - Academic integrity concerns
        """)

# Main content area
if page == "💬 Chat":
    st.markdown('<div class="main-header">💬 AI Learning Chat</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Ask me anything about your studies!</div>', unsafe_allow_html=True)

    # Example questions
    st.markdown("### Try asking:")
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📚 Explain DBMS normalization"):
            st.session_state.example_query = "What is normalization in DBMS?"
    with col2:
        if st.button("🐍 Help with Python OOP"):
            st.session_state.example_query = "Explain object-oriented programming in Python"
    with col3:
        if st.button("🤖 Explain Machine Learning"):
            st.session_state.example_query = "What is machine learning?"

    # Chat interface
    st.markdown("---")

    # Display chat history
    for chat in st.session_state.chat_history:
        with st.container():
            st.markdown(f'<div class="chat-message user-message">👤 **You:** {chat["query"]}</div>', unsafe_allow_html=True)

            # Agent decision box
            st.markdown(f"""
            <div class="agent-decision">
                <strong>🤖 Agent Analysis:</strong><br>
                📂 Category: {chat["category"]}<br>
                ⚡ Action: {chat["action"]}<br>
                {"⚠️ Escalation: Required" if chat.get("should_escalate") else "✅ AI Handling: Approved"}
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f'<div class="chat-message assistant-message">🤖 **Assistant:**\n\n{chat["response"]}</div>', unsafe_allow_html=True)

            # Show recommended resources
            if chat.get("recommended_resources"):
                with st.expander("📚 Recommended Resources"):
                    for resource in chat["recommended_resources"]:
                        st.markdown(f"""
                        **{resource['title']}** ({resource['difficulty']})
                        *{resource['subject']} - {resource['topic']}*
                        {resource['description']}
                        [🔗 Access Resource]({resource['url']})
                        """)

            # Show escalation ticket if escalated
            if chat.get("escalation_ticket"):
                with st.expander("🎫 Escalation Ticket"):
                    ticket = chat["escalation_ticket"]
                    st.json(ticket)

    # Input area
    st.markdown("---")

    # Pre-fill if example clicked
    default_query = st.session_state.get('example_query', '')
    if default_query:
        query = st.text_area("Your question:", value=default_query, height=100, key=f"query_{len(st.session_state.chat_history)}")
        st.session_state.example_query = ''
    else:
        query = st.text_area("Your question:", height=100, key=f"query_{len(st.session_state.chat_history)}")

    col1, col2 = st.columns([1, 5])
    with col1:
        submit = st.button("🚀 Ask", type="primary", use_container_width=True)
    with col2:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.chat_history = []
            st.session_state.agent.clear_conversation_history()
            st.rerun()

    if submit and query:
        with st.spinner("🤔 Analyzing your question..."):
            result = st.session_state.agent.process_query(
                query,
                difficulty=difficulty,
                response_style=response_style,
                subject=subject
            )
            st.session_state.chat_history.append(result)
            st.rerun()

elif page == "📚 Study Planner":
    from pages.study_planner import show_study_planner
    show_study_planner(st.session_state.agent)

elif page == "❓ Quiz Generator":
    from pages.quiz_generator import show_quiz_generator
    show_quiz_generator(st.session_state.agent)

elif page == "📝 Notes & Summary":
    from pages.notes_summary import show_notes_summary
    show_notes_summary(st.session_state.agent)

elif page == "📖 Resources":
    from pages.resources import show_resources
    show_resources()

elif page == "📊 Analytics":
    from pages.analytics_page import show_analytics
    show_analytics(st.session_state.agent)

elif page == "ℹ️ About":
    st.markdown('<div class="main-header">ℹ️ About AI Learner Assistant</div>', unsafe_allow_html=True)

    st.markdown("""
    ## 🎯 Purpose

    The AI Learner Assistant is an intelligent academic support agent designed to help students with their learning journey.
    It goes beyond simple chatbots by implementing agentic AI behavior with decision-making, classification, and escalation capabilities.

    ## 🚀 Key Features

    - **Intelligent Chat**: Context-aware academic assistance
    - **Query Classification**: Automatically categorizes student questions
    - **Smart Escalation**: Identifies when faculty intervention is needed
    - **Resource Recommendations**: Suggests relevant learning materials
    - **Study Planning**: Creates personalized study schedules
    - **Quiz Generation**: Generates practice questions
    - **Note Summarization**: Extracts key points from study materials
    - **Analytics Dashboard**: Tracks learning interactions

    ## 🤖 Agentic Behavior

    This is not just a chatbot! The system implements true agentic AI:

    1. **Query Understanding**: Analyzes student intent
    2. **Classification**: Categorizes queries into types
    3. **Risk Assessment**: Detects queries requiring human intervention
    4. **Decision Making**: Chooses appropriate action
    5. **Resource Retrieval**: Finds relevant learning materials
    6. **Response Generation**: Creates tailored educational responses
    7. **Escalation**: Routes sensitive queries to faculty

    ## 👥 Target Users

    - College and university students
    - Online learners
    - Exam preparation students
    - Course participants

    ## 📚 Supported Subjects

    - Python Programming
    - Data Structures & Algorithms
    - Database Management Systems (DBMS)
    - Artificial Intelligence
    - Machine Learning
    - Computer Networks
    - Operating Systems
    - Mathematics
    - And more...

    ## ⚠️ When Faculty Intervention is Needed

    The system escalates to faculty when:
    - Grading disputes or grade changes requested
    - Access to personal academic records needed
    - Official academic decisions required
    - Institution-specific policy questions
    - Academic integrity concerns
    - Complaints or grievances

    ## 🔒 Privacy & Ethics

    - No personal data is collected or stored permanently
    - Cannot access university systems or databases
    - Cannot make official academic decisions
    - Recommends human intervention when appropriate
    - Transparent about AI limitations

    ## 🛠️ Technology Stack

    - **Frontend**: Streamlit
    - **AI**: OpenAI GPT Models
    - **Language**: Python 3.8+
    - **Architecture**: Modular agent-based system

    ## 📝 Assignment Requirement Mapping

    | Requirement | Implementation |
    |-------------|----------------|
    | Use Case & Problem | Academic learning support for students |
    | Working Implementation | Full Streamlit application with multiple features |
    | Use of GenAI | OpenAI GPT for responses, classification, generation |
    | Agentic Behaviour | Query classification, decision making, escalation engine |
    | Example Input/Output | Chat interface with visible agent decisions |
    | Limitation/Risk | Documented in UI and README |
    | Human/Faculty Intervention | Escalation engine with ticket generation |
    | Technology | Python, Streamlit, OpenAI API, modular architecture |

    ## 🔮 Future Improvements

    - Integration with Learning Management Systems (LMS)
    - RAG (Retrieval Augmented Generation) with course PDFs
    - Student authentication and profiles
    - Faculty dashboard for escalated queries
    - Vector database for better resource matching
    - Multi-language support
    - Voice interface
    - Mobile application

    ---

    **Version**: 1.0.0
    **Developed for**: Academic Assignment
    **License**: MIT
    """)
