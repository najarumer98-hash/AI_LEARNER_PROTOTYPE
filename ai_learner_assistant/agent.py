"""
Main AI Agent that orchestrates the learning assistant
"""
from classifier import QueryClassifier
from escalation import EscalationEngine
from resource_recommender import ResourceRecommender
from llm_service import LLMService
from analytics import Analytics
from prompts import get_assistant_prompt
from config import DEMO_MODE

class LearnerAgent:
    """Main AI Agent for academic assistance"""

    def __init__(self):
        self.classifier = QueryClassifier()
        self.escalation_engine = EscalationEngine()
        self.resource_recommender = ResourceRecommender()
        self.llm_service = LLMService()
        self.analytics = Analytics()
        self.conversation_history = []

    def process_query(self, query, difficulty="Intermediate", response_style="Detailed Explanation", subject="General"):
        """
        Main agent workflow:
        1. Analyze query
        2. Classify intent
        3. Assess escalation risk
        4. Retrieve resources
        5. Decide action
        6. Generate response
        """

        # Step 1: Classify query
        category, classification_reason = self.classifier.classify(query)

        # Step 2: Assess escalation
        should_escalate, escalation_reason, suggested_action = self.escalation_engine.analyze(query, category)

        # Step 3: Recommend resources
        recommended_resources = self.resource_recommender.recommend(query, category)

        # Step 4: Decide action
        action = self._decide_action(category, should_escalate, query)

        # Step 5: Generate response
        if should_escalate:
            response = self._generate_escalation_response(query, escalation_reason, suggested_action)
            escalation_ticket = self.escalation_engine.generate_escalation_ticket(query, category, escalation_reason)
        else:
            response = self._generate_ai_response(query, difficulty, response_style)
            escalation_ticket = None

        # Step 6: Log analytics
        self.analytics.log_query(query, category, action, should_escalate, subject)
        if recommended_resources:
            self.analytics.log_resource_recommendation(len(recommended_resources))

        # Store in conversation history
        self.conversation_history.append({
            "query": query,
            "category": category,
            "response": response,
            "escalated": should_escalate
        })

        return {
            "query": query,
            "category": category,
            "classification_reason": classification_reason,
            "action": action,
            "response": response,
            "should_escalate": should_escalate,
            "escalation_reason": escalation_reason if should_escalate else None,
            "suggested_action": suggested_action if should_escalate else None,
            "escalation_ticket": escalation_ticket,
            "recommended_resources": recommended_resources,
            "demo_mode": DEMO_MODE
        }

    def _decide_action(self, category, should_escalate, query):
        """Decide what action to take"""
        if should_escalate:
            return "ESCALATE"

        query_lower = query.lower()

        if "study plan" in query_lower:
            return "GENERATE_STUDY_PLAN"
        elif "quiz" in query_lower:
            return "GENERATE_QUIZ"
        elif "summarize" in query_lower or "summary" in query_lower:
            return "SUMMARIZE"
        elif category == "Resource Request":
            return "RESOURCE_RECOMMENDATION"
        else:
            return "ANSWER"

    def _generate_ai_response(self, query, difficulty, response_style):
        """Generate AI response using LLM"""
        prompt = get_assistant_prompt(difficulty, response_style)
        response = self.llm_service.generate_response(prompt, query)
        return response

    def _generate_escalation_response(self, query, reason, suggested_action):
        """Generate escalation response"""
        return f"""**⚠️ Faculty Intervention Required**

I've analyzed your query and determined that it requires human intervention from faculty or academic staff.

**Reason for Escalation:**
{reason}

**Recommended Action:**
{suggested_action}

**What You Should Do:**
Please reach out to the appropriate faculty member or academic office to address this matter. They will be able to provide the official guidance or decision you need.

**Contact Options:**
- Your course instructor
- Academic advisor
- Department office
- Student services center

I'm here to help with educational content and learning support, but certain matters require official human judgment and institutional authority."""

    def get_conversation_history(self):
        """Get conversation history"""
        return self.conversation_history

    def clear_conversation_history(self):
        """Clear conversation history"""
        self.conversation_history = []

    def get_analytics(self):
        """Get analytics summary"""
        return self.analytics.get_summary()
