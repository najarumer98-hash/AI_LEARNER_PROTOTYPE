"""
Prompt templates for AI Learner Assistant
"""


def get_assistant_prompt(
    difficulty="Intermediate",
    response_style="Detailed Explanation"
):
    return f"""
You are an intelligent academic learning assistant.

Your purpose:
- Explain academic concepts clearly
- Solve problems step by step
- Help with exam preparation
- Recommend learning resources
- Generate quizzes
- Generate study plans
- Summarize study materials

Student difficulty level: {difficulty}
Response style: {response_style}

Guidelines:
1. Adapt explanations to the student's level.
2. Explain concepts instead of only giving answers.
3. Encourage learning and critical thinking.
4. Do not claim access to private university records.
5. Do not make official academic decisions.
6. Do not invent university policies.
7. For grading disputes or private records, recommend contacting faculty.
8. Be honest when information is uncertain.

Always provide clear, accurate and educational responses.
"""


CLASSIFICATION_PROMPT = """
Classify the following student query into ONE category.

Categories:
1. Concept Explanation
2. Problem Solving
3. Resource Request
4. Exam Preparation
5. Assignment Help
6. Administrative
7. Faculty Escalation
8. General

Student Query:
{query}

Return only:
CATEGORY | Brief reason
"""


ESCALATION_ANALYSIS_PROMPT = """
Analyze whether this student query requires faculty or human intervention.

Query:
{query}

Escalation is needed for:
- Grading disputes
- Grade changes
- Private academic records
- Official academic decisions
- University policies requiring human judgment
- Academic integrity concerns
- Complaints or grievances
- Sensitive personal issues
- Questions about specific faculty
- Official documentation

Return exactly:

ESCALATE: Yes/No
REASON: Brief explanation
SUGGESTED_ACTION: What the student should do
"""


RESOURCE_RECOMMENDATION_PROMPT = """
Recommend relevant learning resources for the student.

Student Query:
{query}

Available Resources:
{resources}

Provide:
- Top 3 to 5 relevant resources
- Why each resource is useful
- Suggested order of study

If no resources match, suggest the type of resource the student needs.
"""


STUDY_PLAN_PROMPT = """
Create a detailed study plan.

Subject:
{subject}

Topics:
{topics}

Number of Days:
{days}

Daily Study Hours:
{hours}

Difficulty:
{difficulty}

Requirements:
- Distribute topics logically
- Start with fundamentals
- Progress toward advanced topics
- Include revision
- Include practice
- Include breaks
- Include useful study activities

Return a clear day-by-day study plan.
"""


# =========================================================
# QUIZ GENERATION
# =========================================================

QUIZ_GENERATION_PROMPT = """
You are an expert academic quiz generator.

Create a multiple-choice quiz.

Topic:
{topic}

Number of Questions:
{num_questions}

Difficulty:
{difficulty}

Rules:
1. Generate exactly {num_questions} questions.
2. Each question must have four options.
3. Options must be A, B, C and D.
4. Only one answer can be correct.
5. correct_answer must be A, B, C or D.
6. Questions should test understanding.
7. Questions must match the requested difficulty.
8. Include a short explanation.
9. Return ONLY valid JSON.
10. Do NOT return Markdown.
11. Do NOT use code fences.

Use exactly this JSON structure:

{{
    "questions": [
        {{
            "question": "Example question?",
            "options": {{
                "A": "First option",
                "B": "Second option",
                "C": "Third option",
                "D": "Fourth option"
            }},
            "correct_answer": "B",
            "explanation": "Explanation of why B is correct."
        }}
    ]
}}
"""


# =========================================================
# SUMMARY
# =========================================================

SUMMARY_PROMPT = """
Create concise exam-friendly study notes from the following text.

Text:
{text}

Include:

1. Brief Summary
2. Key Points
3. Important Terms and Definitions
4. Exam-Focused Points

Keep the explanation clear and useful for students.
"""


# =========================================================
# DEMO MODE
# =========================================================

def get_demo_response(query_lower):
    """
    Return predefined responses when API is not available.
    """

    query_lower = query_lower.lower()

    # DBMS NORMALIZATION
    if "normalization" in query_lower and "dbms" in query_lower:
        return {
            "category": "Concept Explanation",
            "action": "ANSWER",
            "response": """
**Database Normalization**

Normalization is the process of organizing data in a database
to reduce redundancy and improve data integrity.

### 1NF
- Each column contains atomic values.
- No repeating groups.
- Each row is unique.

### 2NF
- Table must be in 1NF.
- No partial dependency.

### 3NF
- Table must be in 2NF.
- No transitive dependency.

### Benefits
- Reduces data redundancy
- Improves data consistency
- Easier database maintenance
- Better data organization
""",
            "escalate": False,
            "resources": [
                "DBMS Normalization",
                "SQL Fundamentals"
            ]
        }

    # PYTHON OOP
    elif (
        "python" in query_lower
        and (
            "oop" in query_lower
            or "inheritance" in query_lower
            or "object" in query_lower
        )
    ):
        return {
            "category": "Concept Explanation",
            "action": "ANSWER",
            "response": """
**Python OOP**

Object-Oriented Programming is a programming approach based
on classes and objects.

### Main Concepts

1. Classes
2. Objects
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction

Example:

class Student:

    def __init__(self, name):
        self.name = name

    def study(self):
        print(self.name, "is studying")

student = Student("Ali")
student.study()

OOP helps make programs reusable, organized and easier to maintain.
""",
            "escalate": False,
            "resources": [
                "Python OOP",
                "Python Basics"
            ]
        }

    # MACHINE LEARNING
    elif "machine learning" in query_lower:
        return {
            "category": "Concept Explanation",
            "action": "ANSWER",
            "response": """
**Machine Learning**

Machine Learning is a branch of Artificial Intelligence
where computers learn patterns from data.

### Types of Machine Learning

**1. Supervised Learning**
Uses labelled data.

Examples:
- Classification
- Regression

**2. Unsupervised Learning**
Uses unlabeled data.

Examples:
- Clustering
- Dimensionality Reduction

**3. Reinforcement Learning**
Learns through rewards and penalties.

Examples:
- Robotics
- Game AI

### Important Terms

Training Data:
Data used to train a model.

Features:
Input variables.

Labels:
Expected outputs.

Overfitting:
The model performs very well on training data but poorly
on new data.

Underfitting:
The model is too simple to learn the patterns.

### Applications

- Image recognition
- Recommendation systems
- Fraud detection
- NLP
- Predictive analytics
""",
            "escalate": False,
            "resources": [
                "Machine Learning Basics",
                "AI Fundamentals"
            ]
        }

    # GRADING DISPUTE
    elif (
        "grade" in query_lower
        or "marks" in query_lower
        or "score" in query_lower
    ):
        if any(
            word in query_lower
            for word in [
                "change",
                "wrong",
                "unfair",
                "dispute",
                "incorrect"
            ]
        ):
            return {
                "category": "Faculty Escalation",
                "action": "ESCALATE",
                "response": """
I cannot change or access official academic grades.

Please contact your course instructor or faculty member.

They can:
- Review your marks
- Explain the grading criteria
- Correct errors if necessary
- Make official grade decisions
""",
                "escalate": True,
                "escalation_reason": (
                    "Grading disputes require faculty review."
                )
            }

    # STUDY PLAN
    elif "study plan" in query_lower:
        return {
            "category": "Exam Preparation",
            "action": "GENERATE_STUDY_PLAN",
            "response": """
**7-Day Study Plan**

Day 1:
Learn the basic concepts.

Day 2:
Study important definitions and examples.

Day 3:
Practice basic questions.

Day 4:
Study intermediate concepts.

Day 5:
Solve practice problems.

Day 6:
Revise difficult topics.

Day 7:
Take a mock test and review mistakes.

Take short breaks while studying and practice regularly.
""",
            "escalate": False,
            "resources": [
                "Study Planning",
                "Practice Questions"
            ]
        }

    # DEFAULT
    else:
        return {
            "category": "General",
            "action": "ANSWER",
            "response": """
I'm your AI Learner Assistant.

I can help you with:

- Concept explanations
- Problem solving
- DBMS
- Python
- Artificial Intelligence
- Machine Learning
- Study plans
- Practice quizzes
- Notes and summaries
- Learning resources

Try asking:

"Explain normalization in DBMS"

"Explain Python OOP"

"Create a study plan for Machine Learning"

"Generate a quiz on Machine Learning"
""",
            "escalate": False,
            "resources": []
        }