"""
Prompt templates for AI Learner Assistant
"""

def get_assistant_prompt(difficulty="Intermediate", response_style="Detailed Explanation"):
    """Main academic assistant prompt"""
    return f"""You are an intelligent academic learning assistant designed to help students understand course concepts and succeed in their studies.

Your purpose:
- Help students understand academic concepts clearly
- Provide step-by-step explanations for problems
- Recommend relevant learning resources
- Support exam preparation
- Generate educational content (quizzes, study plans, summaries)

Student Context:
- Difficulty Level: {difficulty}
- Response Style: {response_style}

Important Guidelines:
1. Adapt your explanation complexity to the student's difficulty level
2. Use the specified response style
3. Prioritize educational understanding over just giving answers
4. Encourage learning and critical thinking
5. Do NOT claim access to private university records or systems
6. Do NOT make official academic decisions (grades, admissions, etc.)
7. Do NOT fabricate university policies or specific institutional information
8. When asked about private records, grading disputes, or institutional policies, acknowledge you cannot help and recommend contacting the appropriate faculty/office
9. Be honest about uncertainty - it's okay to say "I'm not certain" or "This requires expert verification"
10. Focus on concepts, explanations, and learning strategies

Always provide clear, accurate, and educationally valuable responses."""

CLASSIFICATION_PROMPT = """Analyze the following student query and classify it into ONE of these categories:

Categories:
1. Concept Explanation - Student wants to understand a topic/concept
2. Problem Solving - Student needs help solving a specific problem
3. Resource Request - Student is looking for learning materials/resources
4. Exam Preparation - Student is preparing for exams/tests
5. Assignment Help - Student needs guidance on assignments
6. Administrative - Student has questions about policies, procedures, schedules
7. Faculty Escalation - Requires faculty/human intervention (grading disputes, personal records, policy decisions)
8. General - General conversation or unclear intent

Student Query: {query}

Respond with ONLY the category name and a brief one-sentence reason.
Format: CATEGORY | Reason"""

ESCALATION_ANALYSIS_PROMPT = """Analyze whether this student query requires faculty/human intervention.

Query: {query}

Escalation is needed when:
- Grading disputes or grade changes
- Access to personal/private academic records
- Official academic decisions (admissions, transfers, etc.)
- Institution-specific policies requiring human judgment
- Academic integrity concerns
- Complaints or grievances
- Personal counseling or sensitive issues
- Questions about specific faculty members
- Requests for official documentation

Respond in this format:
ESCALATE: Yes/No
REASON: Brief explanation
SUGGESTED_ACTION: What the student should do"""

RESOURCE_RECOMMENDATION_PROMPT = """Based on this student query, recommend relevant learning resources from the provided resource database.

Query: {query}
Available Resources: {resources}

Respond with:
- Top 3-5 most relevant resources
- Brief explanation of why each resource is relevant
- Suggested order of study

If no resources match well, suggest what type of resources would be helpful."""

STUDY_PLAN_PROMPT = """Generate a detailed study plan based on the following requirements:

Subject: {subject}
Topics: {topics}
Number of Days: {days}
Daily Study Hours: {hours}
Difficulty Level: {difficulty}

Create a day-by-day study plan that:
- Distributes topics logically across days
- Includes time for review and practice
- Progresses from fundamentals to advanced topics
- Includes break recommendations
- Suggests specific activities (reading, practice, projects)

Format as a structured day-by-day plan."""

QUIZ_GENERATION_PROMPT = """Generate a quiz with the following specifications:

Topic: {topic}
Number of Questions: {num_questions}
Difficulty: {difficulty}
Question Type: Multiple Choice

For each question provide:
1. Question text
2. Four options (A, B, C, D)
3. Correct answer
4. Brief explanation of why the answer is correct

Make questions test understanding, not just memorization.
Format as structured JSON."""

SUMMARY_PROMPT = """Generate comprehensive study notes from the following academic text:

Text: {text}

Provide:
1. Brief Summary (2-3 sentences)
2. Key Points (bullet list of main concepts)
3. Important Terms (definitions)
4. Exam-Focused Points (what's most likely to be tested)

Make it concise and exam-preparation friendly."""

def get_demo_response(query_lower):
    """Predefined responses for demo mode"""

    # Normalization
    if "normalization" in query_lower and "dbms" in query_lower:
        return {
            "category": "Concept Explanation",
            "action": "ANSWER",
            "response": """**Database Normalization Explained**

Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.

**1st Normal Form (1NF):**
- Each column contains atomic (indivisible) values
- Each column contains values of a single type
- Each column has a unique name
- No repeating groups

Example:
❌ Not 1NF: Student(ID, Name, Courses: "Math, Physics, Chemistry")
✓ 1NF: Student(ID, Name) and Enrollment(StudentID, Course)

**2nd Normal Form (2NF):**
- Must be in 1NF
- No partial dependencies (non-key attributes fully depend on the entire primary key)

**3rd Normal Form (3NF):**
- Must be in 2NF
- No transitive dependencies (non-key attributes depend only on primary key, not on other non-key attributes)

**Why Normalize?**
- Eliminates data redundancy
- Ensures data consistency
- Makes database maintenance easier
- Reduces storage space

**When NOT to normalize:**
- Read-heavy systems where performance is critical
- Data warehousing scenarios""",
            "escalate": False,
            "resources": ["DBMS Normalization", "SQL Fundamentals"]
        }

    # Python OOP
    elif "python" in query_lower and ("oop" in query_lower or "inheritance" in query_lower or "object" in query_lower):
        return {
            "category": "Concept Explanation",
            "action": "ANSWER",
            "response": """**Python Object-Oriented Programming (OOP)**

OOP is a programming paradigm based on objects that contain data (attributes) and code (methods).

**Key Concepts:**

**1. Classes and Objects**
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(f"{self.name} is studying")

# Create object
student1 = Student("Alice", 20)
```

**2. Encapsulation**
- Bundling data and methods together
- Hiding internal details using private variables (_variable)

**3. Inheritance**
```python
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):  # Inherits from Person
    def __init__(self, name, student_id):
        super().__init__(name)
        self.student_id = student_id
```

**4. Polymorphism**
- Same method name, different behaviors
- Method overriding

**5. Abstraction**
- Hiding complex implementation details
- Showing only essential features

**Benefits:**
- Code reusability
- Better organization
- Easier maintenance
- Models real-world scenarios""",
            "escalate": False,
            "resources": ["Python OOP", "Python Basics"]
        }

    # Machine Learning
    elif "machine learning" in query_lower:
        return {
            "category": "Concept Explanation",
            "action": "ANSWER",
            "response": """**Machine Learning Overview**

Machine Learning is a subset of AI that enables systems to learn and improve from experience without being explicitly programmed.

**Types of Machine Learning:**

**1. Supervised Learning**
- Learns from labeled data
- Examples: Classification, Regression
- Algorithms: Linear Regression, Decision Trees, Neural Networks

**2. Unsupervised Learning**
- Learns from unlabeled data
- Examples: Clustering, Dimensionality Reduction
- Algorithms: K-Means, PCA, Hierarchical Clustering

**3. Reinforcement Learning**
- Learns through trial and error
- Rewards and penalties
- Examples: Game AI, Robotics

**Key Concepts:**
- **Training Data**: Data used to train the model
- **Features**: Input variables
- **Labels**: Output/target variable (in supervised learning)
- **Model**: Mathematical representation learned from data
- **Overfitting**: Model performs well on training data but poorly on new data
- **Underfitting**: Model is too simple to capture patterns

**Common Applications:**
- Image recognition
- Natural language processing
- Recommendation systems
- Fraud detection
- Predictive analytics""",
            "escalate": False,
            "resources": ["Machine Learning Basics", "AI Fundamentals"]
        }

    # Grading dispute
    elif "grade" in query_lower or "marks" in query_lower or "score" in query_lower:
        if any(word in query_lower for word in ["change", "wrong", "unfair", "dispute", "incorrect"]):
            return {
                "category": "Faculty Escalation",
                "action": "ESCALATE",
                "response": """I understand you have concerns about your grades. However, I cannot:
- Change or modify grades
- Make official academic decisions
- Access your grade records
- Mediate grading disputes

**Recommended Action:**
Please contact your course instructor or faculty member directly to discuss your grading concerns. They can:
- Review your assignment/exam
- Explain the grading criteria
- Address any discrepancies
- Make official grade adjustments if warranted

You may also reach out to:
- Academic advisor
- Department head
- Student services office

It's important to address grading concerns through official channels.""",
                "escalate": True,
                "escalation_reason": "Grading dispute requires faculty review and official academic decision-making"
            }

    # Study plan
    elif "study plan" in query_lower:
        return {
            "category": "Exam Preparation",
            "action": "GENERATE_STUDY_PLAN",
            "response": """**7-Day Python OOP Study Plan**

**Day 1: Foundations (2 hours)**
- Introduction to OOP concepts
- Classes and Objects basics
- Practice: Create simple class definitions

**Day 2: Attributes and Methods (2 hours)**
- Instance variables and methods
- Constructor (__init__)
- Practice: Build a Student class with attributes

**Day 3: Encapsulation (2 hours)**
- Public vs Private attributes
- Getters and Setters
- Practice: Add data protection to classes

**Day 4: Inheritance (2 hours)**
- Parent and child classes
- Method overriding
- super() function
- Practice: Create inheritance hierarchies

**Day 5: Polymorphism (2 hours)**
- Method overloading and overriding
- Duck typing
- Practice: Implement polymorphic behavior

**Day 6: Advanced Concepts (2 hours)**
- Abstract classes
- Multiple inheritance
- Class methods and static methods

**Day 7: Review and Practice (2 hours)**
- Solve coding problems
- Review all concepts
- Build a mini-project combining all concepts

**Daily Tips:**
- Take 10-minute breaks every hour
- Code along with examples
- Don't just read - practice coding!""",
            "escalate": False,
            "resources": ["Python OOP", "Python Basics"]
        }

    # Default response
    else:
        return {
            "category": "General",
            "action": "ANSWER",
            "response": """I'm here to help you with your academic questions! I can assist with:

- 📚 Explaining concepts (DBMS, Python, AI, ML, etc.)
- 💡 Solving problems step-by-step
- 📖 Recommending learning resources
- 📝 Generating study plans
- ❓ Creating practice quizzes
- 📄 Summarizing study materials

Try asking me something like:
- "Explain normalization in DBMS"
- "How does inheritance work in Python?"
- "Create a study plan for Data Structures"
- "Generate a quiz on Machine Learning"

What would you like to learn about today?""",
            "escalate": False,
            "resources": []
        }
