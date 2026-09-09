"""
Query classifier for categorizing student questions
"""
from llm_service import LLMService
from prompts import CLASSIFICATION_PROMPT, get_demo_response
from config import DEMO_MODE

class QueryClassifier:
    """Classifies student queries into categories"""

    def __init__(self):
        self.llm_service = LLMService()

    def classify(self, query):
        """
        Classify the query into a category
        Returns: (category, reason)
        """
        if DEMO_MODE:
            return self._demo_classify(query)

        try:
            prompt = CLASSIFICATION_PROMPT.format(query=query)
            response = self.llm_service.generate_response(prompt, query)

            # Parse response: "CATEGORY | Reason"
            if "|" in response:
                parts = response.split("|", 1)
                category = parts[0].strip()
                reason = parts[1].strip() if len(parts) > 1 else "Automated classification"
                return category, reason
            else:
                return "General", "Unable to classify clearly"

        except Exception as e:
            return "General", f"Classification error: {str(e)}"

    def _demo_classify(self, query):
        """Demo mode classification"""
        query_lower = query.lower()
        demo_data = get_demo_response(query_lower)
        category = demo_data.get("category", "General")

        # Generate reason based on query
        if "normalization" in query_lower or "explain" in query_lower or "what is" in query_lower:
            reason = "Student is asking for conceptual explanation"
        elif "study plan" in query_lower:
            reason = "Student wants to create a structured study schedule"
        elif "quiz" in query_lower:
            reason = "Student is requesting practice questions"
        elif "grade" in query_lower or "marks" in query_lower:
            reason = "Query involves grading matters requiring faculty attention"
        elif "resource" in query_lower or "recommend" in query_lower:
            reason = "Student is looking for learning materials"
        else:
            reason = "General academic inquiry"

        return category, reason
