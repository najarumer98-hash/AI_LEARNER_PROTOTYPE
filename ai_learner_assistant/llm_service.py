"""
LLM Service for interacting with OpenAI API
"""
import openai
from config import OPENAI_API_KEY, OPENAI_MODEL, DEMO_MODE
from prompts import get_demo_response
import json

class LLMService:
    """Service for LLM interactions"""

    def __init__(self):
        self.demo_mode = DEMO_MODE
        if not self.demo_mode:
            openai.api_key = OPENAI_API_KEY
            self.model = OPENAI_MODEL

    def generate_response(self, prompt, query=""):
        """Generate response from LLM or demo mode"""
        if self.demo_mode:
            return self._get_demo_response(query)

        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": query}
                ],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}\n\nPlease check your API key configuration."

    def generate_json_response(self, prompt, query=""):
        """Generate JSON response from LLM"""
        if self.demo_mode:
            return self._get_demo_json_response(query)

        try:
            response = openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": query}
                ],
                temperature=0.7,
                max_tokens=2000,
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            return {"error": f"Error generating JSON response: {str(e)}"}

    def _get_demo_response(self, query):
        """Get demo response for common queries"""
        query_lower = query.lower()
        demo_data = get_demo_response(query_lower)
        return demo_data.get("response", "Demo mode active. Please configure your API key for live responses.")

    def _get_demo_json_response(self, query):
        """Get demo JSON response"""
        query_lower = query.lower()

        # Quiz generation
        if "quiz" in query_lower:
            return {
                "questions": [
                    {
                        "question": "What is the main purpose of normalization in databases?",
                        "options": {
                            "A": "To increase database size",
                            "B": "To reduce data redundancy and improve integrity",
                            "C": "To make queries slower",
                            "D": "To delete data"
                        },
                        "correct_answer": "B",
                        "explanation": "Normalization organizes data to minimize redundancy and dependency, improving data integrity."
                    },
                    {
                        "question": "Which normal form eliminates partial dependencies?",
                        "options": {
                            "A": "1NF",
                            "B": "2NF",
                            "C": "3NF",
                            "D": "BCNF"
                        },
                        "correct_answer": "B",
                        "explanation": "Second Normal Form (2NF) removes partial dependencies on the primary key."
                    }
                ]
            }

        return {"content": "Demo mode - JSON response"}

    def is_demo_mode(self):
        """Check if running in demo mode"""
        return self.demo_mode
