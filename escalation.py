"""
Escalation engine for detecting when faculty intervention is needed
"""
from llm_service import LLMService
from prompts import ESCALATION_ANALYSIS_PROMPT, get_demo_response
from config import DEMO_MODE
import datetime

class EscalationEngine:
    """Determines when queries need faculty/human intervention"""

    def __init__(self):
        self.llm_service = LLMService()

    def analyze(self, query, category):
        """
        Analyze if query needs escalation
        Returns: (should_escalate, reason, suggested_action)
        """
        if DEMO_MODE:
            return self._demo_analyze(query)

        try:
            prompt = ESCALATION_ANALYSIS_PROMPT.format(query=query)
            response = self.llm_service.generate_response(prompt, query)

            # Parse response
            should_escalate = "Yes" in response.split("\n")[0]

            lines = response.split("\n")
            reason = "Requires human judgment"
            suggested_action = "Contact faculty or academic office"

            for line in lines:
                if line.startswith("REASON:"):
                    reason = line.replace("REASON:", "").strip()
                elif line.startswith("SUGGESTED_ACTION:"):
                    suggested_action = line.replace("SUGGESTED_ACTION:", "").strip()

            return should_escalate, reason, suggested_action

        except Exception as e:
            return False, f"Escalation analysis error: {str(e)}", "Continue with AI response"

    def _demo_analyze(self, query):
        """Demo mode escalation analysis"""
        query_lower = query.lower()
        demo_data = get_demo_response(query_lower)

        if demo_data.get("escalate", False):
            reason = demo_data.get("escalation_reason", "Requires faculty intervention")
            action = "Please contact your course instructor or academic advisor to discuss this matter"
            return True, reason, action

        return False, "Query can be handled by AI", "AI will provide response"

    def generate_escalation_ticket(self, query, category, reason):
        """Generate structured escalation ticket"""
        ticket = {
            "ticket_id": f"ESC-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "student_query": query,
            "detected_category": category,
            "escalation_reason": reason,
            "priority": self._determine_priority(query),
            "suggested_faculty_action": self._suggest_faculty_action(query, category),
            "status": "PENDING_REVIEW"
        }
        return ticket

    def _determine_priority(self, query):
        """Determine priority level"""
        query_lower = query.lower()

        # High priority keywords
        high_priority = ["urgent", "emergency", "immediately", "complaint", "harassment"]
        if any(word in query_lower for word in high_priority):
            return "HIGH"

        # Medium priority keywords
        medium_priority = ["grade", "exam", "assignment", "deadline"]
        if any(word in query_lower for word in medium_priority):
            return "MEDIUM"

        return "NORMAL"

    def _suggest_faculty_action(self, query, category):
        """Suggest what faculty should do"""
        query_lower = query.lower()

        if "grade" in query_lower or "marks" in query_lower:
            return "Review student's graded work and discuss grading criteria"
        elif "policy" in query_lower:
            return "Clarify institutional policy and provide official documentation"
        elif "record" in query_lower:
            return "Verify student identity and provide access to appropriate records"
        elif "complaint" in query_lower:
            return "Initiate formal complaint review process"
        else:
            return "Review query and provide appropriate guidance or referral"
