# 🎓 AI Learner Assistant

## Intelligent Academic Support Agent

A comprehensive AI-powered learning assistant that helps students with academic questions, generates study materials, recommends resources, and intelligently escalates queries requiring faculty intervention.

---

## 📋 Table of Contents

1. [Problem Statement](#problem-statement)
2. [Intended Users](#intended-users)
3. [Proposed Solution](#proposed-solution)
4. [Features](#features)
5. [Technology Stack](#technology-stack)
6. [GenAI Usage](#genai-usage)
7. [Agentic Behaviour](#agentic-behaviour)
8. [Architecture](#architecture)
9. [Installation](#installation)
10. [Configuration](#configuration)
11. [Running the Application](#running-the-application)
12. [Usage Examples](#usage-examples)
13. [Human Intervention](#human-intervention)
14. [Limitations and Risks](#limitations-and-risks)
15. [Assignment Requirement Mapping](#assignment-requirement-mapping)
16. [Future Improvements](#future-improvements)

---

## 1. Problem Statement

Students often face challenges when learning:

- **Overwhelming information**: Too many resources, unclear where to start
- **No immediate help**: Waiting hours/days for instructor responses
- **Lack of personalization**: Generic resources don't match individual learning needs
- **Unclear escalation**: Students don't know when to contact faculty
- **No practice materials**: Limited access to quizzes and study plans
- **Time management**: Difficulty organizing study schedules

Traditional learning support systems are often limited to simple Q&A chatbots that cannot make intelligent decisions about when human intervention is needed or provide comprehensive learning support.

---

## 2. Intended Users

### Primary Users:
- **College/University Students**: Need help understanding course concepts
- **Online Learners**: Require self-paced learning support
- **Exam Preparation Students**: Need quizzes and study plans
- **Course Participants**: Want organized learning resources

### Secondary Users:
- **Faculty Members**: Receive escalated queries requiring expert judgment
- **Academic Support Teams**: Monitor student learning patterns

### Supported Subjects:
- Python Programming
- Data Structures & Algorithms
- Database Management Systems (DBMS)
- Artificial Intelligence
- Machine Learning
- Computer Networks
- Operating Systems
- Mathematics
- General Academic Topics

---

## 3. Proposed Solution

The **AI Learner Assistant** is an intelligent agent that provides comprehensive academic support through:

- **Smart Query Classification**: Automatically categorizes student questions
- **AI-Powered Responses**: Generates educational explanations adapted to student level
- **Resource Recommendation**: Suggests relevant learning materials from curated database
- **Escalation Engine**: Identifies queries requiring faculty intervention
- **Study Planning**: Creates personalized learning schedules
- **Quiz Generation**: Produces practice questions with explanations
- **Note Summarization**: Extracts key points from study materials
- **Analytics Dashboard**: Tracks learning interactions and patterns

**Key Differentiator**: This is not just a chatbot - it's an AI agent that makes decisions, classifies queries, retrieves resources, and escalates appropriately.

---

## 4. Features

### Core Features:

#### 💬 **Intelligent Chat Interface**
- Context-aware conversations
- Multi-turn dialogue support
- Visible agent decision-making process
- Query classification display
- Escalation warnings

#### 🎯 **Query Classification**
Automatically categorizes questions into:
- Concept Explanation
- Problem Solving
- Resource Request
- Exam Preparation
- Assignment Help
- Administrative
- Faculty Escalation
- General

#### ⚠️ **Smart Escalation Engine**
Detects when faculty intervention is required:
- Grading disputes
- Personal academic records
- Official policy questions
- Academic integrity concerns
- Institution-specific decisions

Generates structured escalation tickets with:
- Student query
- Detected category
- Escalation reason
- Priority level
- Suggested faculty action
- Timestamp

#### 📚 **Resource Recommender**
- 20+ curated learning resources
- Smart keyword matching
- Subject and difficulty filtering
- Resource search functionality
- Direct links to materials

#### 📅 **Study Plan Generator**
Creates personalized study schedules:
- Day-by-day breakdown
- Customizable duration (1-30 days)
- Flexible daily study hours
- Difficulty-adjusted content
- Break recommendations
- Progress tracking suggestions

#### ❓ **Quiz Generator**
Generates practice quizzes:
- Multiple choice questions
- Customizable question count (2-10)
- Difficulty levels (Beginner/Intermediate/Advanced)
- Detailed explanations
- Instant scoring
- Performance feedback

#### 📝 **Notes & Summary Generator**
Extracts from academic text:
- Brief summaries
- Key points
- Important terms with definitions
- Exam-focused insights
- Structured format

#### 📊 **Analytics Dashboard**
Tracks:
- Total queries and response types
- AI success rate
- Escalation patterns
- Category distribution
- Subject focus areas
- Resource recommendations
- Quiz attempts
- Study plans created
- Recent activity log

#### ⚙️ **Customization Options**
- Difficulty Level (Beginner/Intermediate/Advanced)
- Response Style (Simple/Detailed/Exam Answer/Step-by-Step/Quick Revision)
- Subject Selection
- Query-specific preferences

---

## 5. Technology Stack

**Frontend & UI:**
- **Streamlit** 1.31.0 - Web application framework
- Custom CSS for professional styling
- Responsive layout design

**AI & LLM:**
- **OpenAI API** - GPT models for text generation
- **python-openai** 1.12.0 - Official OpenAI client

**Backend & Processing:**
- **Python** 3.8+ - Core programming language
- **pandas** 2.2.0 - Data manipulation and analytics

**Configuration:**
- **python-dotenv** 1.0.1 - Environment variable management

**Architecture:**
- Modular agent-based design
- Separation of concerns (classification, escalation, resources)
- JSON-based resource storage
- Session-based analytics

---

## 6. GenAI Usage

### How Generative AI is Used:

#### 1. **Academic Question Answering**
- **Model**: OpenAI GPT (gpt-4o-mini or gpt-4)
- **Purpose**: Generate educational explanations
- **Input**: Student query + context (difficulty, style)
- **Output**: Tailored academic response

#### 2. **Query Classification**
- **Model**: GPT for intent detection
- **Purpose**: Categorize student questions
- **Input**: Raw student query
- **Output**: Category + classification reason

#### 3. **Escalation Analysis**
- **Model**: GPT for risk assessment
- **Purpose**: Detect queries needing human intervention
- **Input**: Student query + category
- **Output**: Escalation decision + reason + suggested action

#### 4. **Study Plan Generation**
- **Model**: GPT for structured content creation
- **Purpose**: Create personalized learning schedules
- **Input**: Subject, topics, duration, hours, difficulty
- **Output**: Day-by-day study plan with activities

#### 5. **Quiz Generation**
- **Model**: GPT with JSON output
- **Purpose**: Create practice questions
- **Input**: Topic, question count, difficulty
- **Output**: MCQ questions with options, answers, explanations

#### 6. **Text Summarization**
- **Model**: GPT for extraction and condensation
- **Purpose**: Generate study notes
- **Input**: Academic text
- **Output**: Summary, key points, terms, exam focus

### Prompt Engineering:

All prompts are carefully designed in `prompts.py` with:
- Clear role definitions
- Specific output formats
- Safety guidelines
- Context awareness
- Difficulty adaptation

### Demo Mode:

When no API key is configured:
- Application runs in **DEMO MODE**
- Predefined responses for common queries
- Clearly labeled as demo
- Allows UI demonstration without API costs
- Never misrepresents demo responses as live AI

---

## 7. Agentic Behaviour

### Why This is NOT Just a Chatbot:

The AI Learner Assistant implements **true agentic behavior** with autonomous decision-making:

### Agent Workflow:

```
USER QUERY
    ↓
1. QUERY UNDERSTANDING
   - Parse student input
   - Extract intent and context
    ↓
2. CLASSIFICATION
   - Categorize query type
   - Determine primary intent
   - Generate classification reason
    ↓
3. RISK ASSESSMENT
   - Analyze escalation need
   - Evaluate query sensitivity
   - Check for policy violations
    ↓
4. RESOURCE RETRIEVAL
   - Search resource database
   - Match keywords and topics
   - Rank by relevance
    ↓
5. DECISION MAKING
   - Choose action: ANSWER / ESCALATE / GENERATE
   - Determine response strategy
   - Select appropriate tools
    ↓
6. RESPONSE GENERATION
   - Generate AI response (if appropriate)
   - Create escalation ticket (if needed)
   - Compile resource recommendations
    ↓
7. OUTPUT WITH TRANSPARENCY
   - Display response
   - Show agent decisions
   - Provide reasoning
   - Log analytics
```

### Autonomous Capabilities:

1. **Classification Module** (`classifier.py`)
   - Analyzes query semantics
   - Maps to predefined categories
   - Provides reasoning

2. **Escalation Engine** (`escalation.py`)
   - Evaluates query risk
   - Detects sensitive topics
   - Generates structured tickets
   - Determines priority levels

3. **Resource Recommender** (`resource_recommender.py`)
   - Scores resources by relevance
   - Retrieves from knowledge base
   - Ranks recommendations

4. **Decision Orchestrator** (`agent.py`)
   - Coordinates all modules
   - Makes action decisions
   - Routes to appropriate handler
   - Manages conversation context

### Agent Actions:

- `ANSWER` - Provide AI-generated response
- `RESOURCE_RECOMMENDATION` - Suggest learning materials
- `GENERATE_STUDY_PLAN` - Create learning schedule
- `GENERATE_QUIZ` - Produce practice questions
- `SUMMARIZE` - Extract key information
- `ESCALATE` - Route to faculty

### Visible Decision-Making:

The UI explicitly shows:
- **Category**: What type of query this is
- **Action**: What the agent decided to do
- **Escalation Status**: Whether human intervention is needed
- **Reasoning**: Why these decisions were made

This transparency demonstrates true agentic behavior beyond simple response generation.

---

## 8. Architecture

### System Architecture Diagram:

```
┌─────────────────────────────────────────────────────────────┐
│                         STUDENT                              │
│                           ↓                                  │
│                   [Streamlit UI]                             │
│                 (app.py + pages/)                            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                   LEARNER AGENT (agent.py)                   │
│                   [Main Orchestrator]                        │
└─────────────────────────────────────────────────────────────┘
         ↓              ↓              ↓              ↓
    ┌────────┐    ┌─────────┐   ┌──────────┐   ┌──────────┐
    │CLASSIFY│    │ESCALATE │   │RESOURCES │   │ANALYTICS │
    │(class  │    │(escala  │   │(resource │   │(analyt   │
    │ifier.  │    │tion.py) │   │_recomm   │   │ics.py)   │
    │py)     │    │         │   │ender.py) │   │          │
    └────────┘    └─────────┘   └──────────┘   └──────────┘
         ↓              ↓              ↓              ↓
    ┌──────────────────────────────────────────────────────┐
    │              LLM SERVICE (llm_service.py)            │
    │              [OpenAI API Integration]                │
    └──────────────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────────────┐
    │                  PROMPTS (prompts.py)                │
    │              [Prompt Engineering Layer]               │
    └──────────────────────────────────────────────────────┘
                            ↓
    ┌──────────────────────────────────────────────────────┐
    │                OpenAI GPT Models                     │
    │              (gpt-4o-mini / gpt-4)                   │
    └──────────────────────────────────────────────────────┘
                            ↓
                     [AI Response]
                            ↓
              [Back to Student via UI]
```

### Module Responsibilities:

**`app.py`**: Main Streamlit application, routing, UI rendering
**`agent.py`**: Core agent logic, decision orchestration
**`classifier.py`**: Query classification and intent detection
**`escalation.py`**: Risk assessment and escalation logic
**`resource_recommender.py`**: Resource matching and recommendation
**`llm_service.py`**: OpenAI API communication, demo mode
**`prompts.py`**: Prompt templates and engineering
**`analytics.py`**: Usage tracking and statistics
**`config.py`**: Configuration and constants
**`pages/`**: Individual page modules (study planner, quiz, etc.)
**`data/resources.json`**: Curated learning resources database

---

## 9. Installation

### Prerequisites:

- **Python 3.8 or higher**
- **pip** (Python package installer)
- **OpenAI API key** (optional - runs in demo mode without it)

### Step 1: Extract the Project

```bash
unzip AI_Learner_Assistant.zip
cd ai_learner_assistant
```

### Step 2: Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- streamlit
- openai
- python-dotenv
- pandas

---

## 10. Configuration

### Environment Variables:

1. **Copy the example environment file:**

```bash
copy .env.example .env       # Windows
cp .env.example .env         # macOS/Linux
```

2. **Edit `.env` file:**

```env
OPENAI_API_KEY=your_actual_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

### Getting an OpenAI API Key:

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to **API Keys** section
4. Click **"Create new secret key"**
5. Copy the key and paste it into your `.env` file

### Model Options:

- `gpt-4o-mini` - **Recommended** (fast, cost-effective)
- `gpt-4o` - More capable but more expensive
- `gpt-4-turbo` - High performance

### Demo Mode:

If you **don't** configure an API key:
- Application runs in **DEMO MODE**
- Uses predefined responses
- Clearly labeled as demo
- Perfect for demonstration/testing
- No API costs

---

## 11. Running the Application

### Start the Application:

```bash
streamlit run app.py
```

### What Happens:

1. Streamlit starts a local web server
2. Browser automatically opens to `http://localhost:8501`
3. Application loads with sidebar navigation
4. Demo mode warning appears if no API key configured

### Stopping the Application:

Press `Ctrl+C` in the terminal

### Troubleshooting:

**Port already in use:**
```bash
streamlit run app.py --server.port 8502
```

**Module not found:**
```bash
pip install -r requirements.txt --upgrade
```

**API key errors:**
Check your `.env` file configuration and ensure the key is valid

---

## 12. Usage Examples

### Example 1: Concept Explanation

**Input:**
```
What is normalization in DBMS?
```

**Expected Output:**

**Agent Analysis:**
- 📂 Category: Concept Explanation
- ⚡ Action: ANSWER
- ✅ AI Handling: Approved

**Response:**
Detailed explanation of database normalization including:
- Definition and purpose
- 1NF, 2NF, 3NF with examples
- Benefits and use cases
- When to use/avoid normalization

**Recommended Resources:**
- DBMS Normalization (Intermediate)
- SQL Fundamentals (Beginner)
- Database Design Principles (Intermediate)

---

### Example 2: Faculty Escalation

**Input:**
```
My teacher gave me 5 marks but I think I deserve 10. Can you change my grade?
```

**Expected Output:**

**Agent Analysis:**
- 📂 Category: Faculty Escalation
- ⚡ Action: ESCALATE
- ⚠️ Escalation: Required

**Response:**
⚠️ **Faculty Intervention Required**

**Reason for Escalation:**
Grading disputes require faculty review and official academic decision-making

**Recommended Action:**
Please contact your course instructor or academic advisor to discuss this matter

**Escalation Ticket Generated:**
- Ticket ID: ESC-20260909120000
- Priority: MEDIUM
- Status: PENDING_REVIEW
- Suggested Faculty Action: Review student's graded work and discuss grading criteria

---

### Example 3: Study Plan Generation

**Input (via Study Planner page):**
- Subject: Python
- Topics: Functions, Classes, Inheritance, Polymorphism
- Days: 7
- Daily Hours: 2
- Difficulty: Intermediate

**Expected Output:**

**7-Day Python OOP Study Plan**

Day 1: Foundations (2 hours)
- Introduction to OOP concepts
- Classes and Objects basics
- Practice: Create simple class definitions

Day 2: Attributes and Methods (2 hours)
- Instance variables and methods
- Constructor (__init__)
- Practice: Build a Student class

[... continuing through Day 7]

---

### Example 4: Quiz Generation

**Input (via Quiz Generator page):**
- Topic: Python OOP
- Questions: 5
- Difficulty: Intermediate

**Expected Output:**

5 multiple-choice questions with:
- Question text
- 4 options (A, B, C, D)
- Correct answer
- Detailed explanation

Interactive quiz with:
- Answer selection
- Instant scoring
- Performance feedback
- Question-by-question review

---

## 13. Human Intervention

### When Faculty Intervention is Required:

The escalation engine detects the following scenarios requiring human judgment:

#### 1. **Grading Disputes**
- Student disagrees with assigned grade
- Requests grade changes
- Questions grading criteria
- **Action**: Instructor reviews work and discusses criteria

#### 2. **Personal Academic Records**
- Requests for transcripts
- Grade history access
- Attendance records
- **Action**: Verify identity, provide official records

#### 3. **Official Academic Decisions**
- Admission decisions
- Course enrollment issues
- Academic standing determinations
- **Action**: Refer to appropriate academic office

#### 4. **Institution-Specific Policies**
- Campus-specific rules
- Department procedures
- University regulations
- **Action**: Provide official policy documentation

#### 5. **Academic Integrity Concerns**
- Suspected plagiarism
- Cheating allegations
- Honor code violations
- **Action**: Initiate formal review process

#### 6. **Complaints or Grievances**
- Faculty complaints
- Course quality concerns
- Harassment reports
- **Action**: Follow institutional grievance procedures

#### 7. **Personal Counseling**
- Mental health concerns
- Personal crises
- Stress management
- **Action**: Refer to counseling services

### Escalation Ticket Structure:

Generated tickets include:
- **Ticket ID**: Unique identifier
- **Timestamp**: When escalation occurred
- **Student Query**: Original question
- **Detected Category**: Query classification
- **Escalation Reason**: Why faculty review is needed
- **Priority**: HIGH / MEDIUM / NORMAL
- **Suggested Faculty Action**: Recommended next steps
- **Status**: PENDING_REVIEW

### Faculty Dashboard (Future):

Planned features:
- View all escalated queries
- Respond directly to students
- Mark tickets as resolved
- Analytics on escalation patterns
- Student interaction history

---

## 14. Limitations and Risks

### Technical Limitations:

#### 1. **AI Hallucination**
- **Risk**: LLM may generate incorrect or fabricated information
- **Mitigation**: 
  - Clear disclaimers in UI
  - Encourage verification of critical information
  - Provide resource links for validation

#### 2. **Outdated Information**
- **Risk**: AI training data has knowledge cutoff
- **Mitigation**:
  - Recommend checking current documentation
  - Link to official resources
  - Acknowledge uncertainty

#### 3. **API Dependency**
- **Risk**: Service unavailable if API down
- **Mitigation**:
  - Demo mode fallback
  - Graceful error handling
  - Clear error messages

#### 4. **Context Limitations**
- **Risk**: May lose context in long conversations
- **Mitigation**:
  - Session-based conversation history
  - Clear conversation button
  - Context summary in prompts

### Privacy & Security Risks:

#### 5. **Data Privacy**
- **Risk**: Queries sent to OpenAI API
- **Concern**: Student questions may contain personal information
- **Mitigation**:
  - No personal data stored permanently
  - Queries not used for training (OpenAI policy)
  - Clear privacy disclaimer

#### 6. **No Authentication**
- **Risk**: Anyone can access the application
- **Limitation**: No user identity verification
- **Future**: Add authentication system

#### 7. **Cannot Access University Systems**
- **Risk**: Students may expect access to institutional data
- **Mitigation**:
  - Clear communication of limitations
  - Escalation to appropriate offices

### Academic Integrity Risks:

#### 8. **Assignment Completion**
- **Risk**: Students may use AI to complete assignments
- **Concern**: Potential academic dishonesty
- **Mitigation**:
  - Designed for learning, not assignment completion
  - Encourages understanding over answers
  - Faculty awareness recommended

#### 9. **Overreliance on AI**
- **Risk**: Students may not develop critical thinking
- **Mitigation**:
  - Encourages independent verification
  - Promotes learning over answer-getting
  - Recommends traditional resources

### Operational Limitations:

#### 10. **Institution-Specific Information**
- **Cannot Provide**:
  - Campus-specific policies
  - Local procedures
  - Specific faculty information
  - Current semester schedules
- **Solution**: Escalation to appropriate offices

#### 11. **No Real-Time Learning**
- **Risk**: Cannot learn from current session
- **Limitation**: No adaptive personalization
- **Future**: Implement user profiles and learning tracking

#### 12. **Cost Considerations**
- **Risk**: API usage costs money
- **Concern**: Heavy usage may incur significant costs
- **Mitigation**:
  - Efficient prompt design
  - Model selection (gpt-4o-mini)
  - Usage monitoring

### Safety Disclaimers:

**The application displays:**

> ⚠️ **Important Limitations:**
> - AI may hallucinate or provide incorrect information
> - Always verify critical academic information
> - Cannot access your university records
> - Cannot make official academic decisions
> - Cannot change grades or policies
> - Responses may be outdated
>
> **When to Contact Faculty:**
> - Grading disputes
> - Official academic decisions
> - Institution-specific policies
> - Personal academic records
> - Academic integrity concerns

---

## 15. Assignment Requirement Mapping

### Comprehensive Requirement Fulfillment:

| Assignment Requirement | Implementation | Location |
|------------------------|----------------|----------|
| **Use Case & Problem Statement** | Academic learning support for students facing information overload, delayed help, and lack of personalization | README Section 1 |
| **Working Implementation** | Full Streamlit web application with 7 functional pages | `app.py`, `pages/` |
| **Use of Generative AI** | OpenAI GPT for responses, classification, quiz generation, summarization, study planning | `llm_service.py`, `prompts.py` |
| **Agentic Behaviour** | Query classification, decision making, risk assessment, escalation engine, resource retrieval | `agent.py`, `classifier.py`, `escalation.py` |
| **Example Input/Output** | 4 detailed examples with visible agent decisions | README Section 12 |
| **Limitation/Risk Discussion** | 12 identified limitations with mitigation strategies | README Section 14 |
| **Human/Faculty Intervention** | Escalation engine with 7 trigger scenarios, ticket generation | `escalation.py`, README Section 13 |
| **Technology Stack** | Python, Streamlit, OpenAI API, Pandas - modular architecture | README Section 5 |
| **Demo Mode** | Functional without API key, clearly labeled | `llm_service.py`, `prompts.py` |
| **Resource Recommendation** | 20+ curated resources with smart matching | `resource_recommender.py`, `data/resources.json` |
| **Analytics & Tracking** | Comprehensive dashboard with 8 metrics | `analytics.py`, `pages/analytics_page.py` |

### Additional Features Beyond Requirements:

- ✅ Study Plan Generator
- ✅ Interactive Quiz Generator with scoring
- ✅ Notes & Summary Generator
- ✅ Resource Search and Filtering
- ✅ Multiple Response Styles
- ✅ Difficulty Level Adaptation
- ✅ Escalation Ticket System
- ✅ Recent Activity Log
- ✅ Analytics Export

---

## 16. Future Improvements

### Short-term Enhancements:

1. **RAG Implementation**
   - Upload course PDFs
   - Vector database (Pinecone, Chroma)
   - Document-aware responses

2. **User Authentication**
   - Login system
   - User profiles
   - Personalized history

3. **Enhanced Analytics**
   - Learning progress tracking
   - Topic mastery indicators
   - Personalized recommendations

4. **Resource Expansion**
   - More learning materials
   - Video resources
   - Interactive tutorials

### Medium-term Features:

5. **LMS Integration**
   - Connect to Canvas, Moodle, Blackboard
   - Sync course materials
   - Assignment integration

6. **Faculty Dashboard**
   - View escalated queries
   - Respond to students
   - Track patterns
   - Analytics for instructors

7. **Mobile Application**
   - Native iOS/Android apps
   - Push notifications
   - Offline mode

8. **Voice Interface**
   - Speech-to-text input
   - Text-to-speech output
   - Voice conversations

### Long-term Vision:

9. **Advanced Personalization**
   - Learning style detection
   - Adaptive difficulty
   - Personalized learning paths
   - Spaced repetition system

10. **Collaborative Features**
    - Study groups
    - Peer learning
    - Discussion forums
    - Shared resources

11. **Multi-language Support**
    - International student support
    - Translation capabilities
    - Localized content

12. **Advanced AI Features**
    - Computer vision for diagram explanation
    - Code execution and debugging
    - Interactive simulations
    - Virtual tutoring sessions

13. **Institutional Integration**
    - SSO authentication
    - Official grade access (with permission)
    - Campus event integration
    - Official policy database

14. **Gamification**
    - Points and badges
    - Leaderboards
    - Learning streaks
    - Achievement system

---

## 📄 License

MIT License - Free for educational and personal use

---

## 👥 Contributors

Developed for academic assignment demonstration

---

## 📞 Support

For issues or questions:
- Check the **ℹ️ About** page in the application
- Review this README
- Contact your course instructor

---

## 🎓 Educational Purpose

This project is developed as an academic assignment to demonstrate:
- Generative AI integration
- Agentic AI behavior
- Full-stack application development
- UI/UX design
- Software engineering principles

**Not for production use without proper security, authentication, and institutional approval.**

---

## ✅ Quick Start Checklist

- [ ] Extract ZIP file
- [ ] Create virtual environment
- [ ] Install dependencies (`pip install -r requirements.txt`)
- [ ] (Optional) Configure `.env` with OpenAI API key
- [ ] Run application (`streamlit run app.py`)
- [ ] Test chat interface
- [ ] Try study planner
- [ ] Generate a quiz
- [ ] Check analytics dashboard
- [ ] Review escalation examples

---

**Version:** 1.0.0  
**Last Updated:** September 2026  
**Status:** Ready for Demonstration

🎓 **Ready to learn? Start the application and explore!**
