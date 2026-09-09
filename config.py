import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# ==========================================
# APP SETTINGS
# ==========================================

APP_TITLE = "AI Learner Assistant"

APP_DESCRIPTION = (
    "An intelligent academic support agent that helps learners "
    "understand concepts, create study plans, generate quizzes, "
    "summarize notes, and recommend learning resources."
)

# ==========================================
# ACADEMIC SETTINGS
# ==========================================

SUBJECTS = [
    "Computer Science",
    "DBMS",
    "Python",
    "Data Structures",
    "Artificial Intelligence",
    "Machine Learning",
    "Computer Networks",
    "Operating Systems",
    "Software Engineering",
    "Mathematics",
    "Other"
]

DIFFICULTY_LEVELS = [
    "Beginner",
    "Intermediate",
    "Advanced"
]

RESPONSE_STYLES = [
    "Simple",
    "Detailed",
    "Exam-Oriented"
]

# ==========================================
# OMNIROUTE SETTINGS
# ==========================================

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    ""
).strip()

OPENAI_BASE_URL = os.getenv(
    "OPENAI_BASE_URL",
    "https://omnirouter.li/v1"
).strip()

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "pu/claude-haiku-4-5"
).strip()

# ==========================================
# DEMO MODE
# ==========================================

DEMO_MODE = not bool(OPENAI_API_KEY)