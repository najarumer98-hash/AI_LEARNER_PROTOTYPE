"""
Configuration settings for AI Learner Assistant
"""
import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# Demo Mode Configuration
DEMO_MODE = not bool(OPENAI_API_KEY)

# Application Settings
APP_TITLE = "🎓 AI Learner Assistant"
APP_DESCRIPTION = "Your Intelligent Academic Support Agent"

# Query Categories
QUERY_CATEGORIES = [
    "Concept Explanation",
    "Problem Solving",
    "Resource Request",
    "Exam Preparation",
    "Assignment Help",
    "Administrative",
    "Faculty Escalation",
    "General"
]

# Agent Actions
AGENT_ACTIONS = [
    "ANSWER",
    "RESOURCE_RECOMMENDATION",
    "GENERATE_STUDY_PLAN",
    "GENERATE_QUIZ",
    "SUMMARIZE",
    "ESCALATE"
]

# Difficulty Levels
DIFFICULTY_LEVELS = ["Beginner", "Intermediate", "Advanced"]

# Response Styles
RESPONSE_STYLES = [
    "Simple Explanation",
    "Detailed Explanation",
    "Exam Answer",
    "Step-by-Step",
    "Quick Revision"
]

# Subjects
SUBJECTS = [
    "Python",
    "Data Structures",
    "DBMS",
    "Artificial Intelligence",
    "Machine Learning",
    "Computer Networks",
    "Operating Systems",
    "Mathematics",
    "General"
]
