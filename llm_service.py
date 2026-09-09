"""
LLM Service for AI Learner Assistant.

Uses OmniRoute's OpenAI-compatible API.
Also supports Demo Mode when no API key is available.
"""

import json

from openai import OpenAI

from config import (
    OPENAI_API_KEY,
    OPENAI_BASE_URL,
    OPENAI_MODEL,
    DEMO_MODE,
)

from prompts import get_demo_response


class LLMService:
    """Handles AI responses through OmniRoute or Demo Mode."""

    def __init__(self):
        self.demo_mode = DEMO_MODE
        self.model = OPENAI_MODEL

        if not self.demo_mode:
            self.client = OpenAI(
                api_key=OPENAI_API_KEY,
                base_url=OPENAI_BASE_URL,
            )
        else:
            self.client = None

    # =========================================================
    # NORMAL TEXT RESPONSE
    # =========================================================

    def generate_response(self, prompt, query=""):
        """
        Generate a normal text response from the LLM.

        Parameters:
            prompt: System/instruction prompt.
            query: User's question.

        Returns:
            AI-generated text response.
        """

        # -------------------------
        # DEMO MODE
        # -------------------------
        if self.demo_mode:
            return self._get_demo_response(query)

        # -------------------------
        # LIVE OMNIROUTE
        # -------------------------
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": prompt,
                    },
                    {
                        "role": "user",
                        "content": query,
                    },
                ],
                temperature=0.7,
                max_tokens=1200,
            )

            return response.choices[0].message.content

        except Exception as e:
            return (
                "⚠️ Unable to generate the AI response.\n\n"
                f"Error: {str(e)}\n\n"
                "Please check your OmniRoute API key, "
                "model name, and account balance."
            )

    # =========================================================
    # JSON RESPONSE
    # =========================================================

    def generate_json_response(self, prompt, query=""):
        """
        Generate a structured JSON response.

        Used by:
        - Quiz Generator
        - Structured academic features
        - Other JSON-based components
        """

        # -------------------------
        # DEMO MODE
        # -------------------------
        if self.demo_mode:
            return {
                "questions": [
                    {
                        "question": "What is Python?",
                        "options": [
                            "A programming language",
                            "A database",
                            "An operating system",
                            "A web browser",
                        ],
                        "answer": "A programming language",
                        "explanation": (
                            "Python is a high-level, "
                            "general-purpose programming language."
                        ),
                    }
                ]
            }

        # -------------------------
        # LIVE OMNIROUTE
        # -------------------------
        try:

            full_prompt = prompt

            if query:
                full_prompt = (
                    f"{prompt}\n\n"
                    f"User Request:\n{query}"
                )

            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an academic assistant. "
                            "Return ONLY valid JSON. "
                            "Do not use Markdown. "
                            "Do not use ```json or ```."
                        ),
                    },
                    {
                        "role": "user",
                        "content": full_prompt,
                    },
                ],
                temperature=0.5,
                max_tokens=2500,
            )

            content = response.choices[0].message.content.strip()

            # ---------------------------------
            # Remove Markdown code fences
            # ---------------------------------

            if content.startswith("```json"):
                content = content[7:]

            elif content.startswith("```"):
                content = content[3:]

            if content.endswith("```"):
                content = content[:-3]

            content = content.strip()

            # ---------------------------------
            # Convert JSON string to Python dict
            # ---------------------------------

            return json.loads(content)

        except json.JSONDecodeError as e:
            raise Exception(
                f"AI returned invalid JSON: {str(e)}"
            )

        except Exception as e:
            raise Exception(
                f"JSON generation failed: {str(e)}"
            )

    # =========================================================
    # DEMO RESPONSE
    # =========================================================

    def _get_demo_response(self, query):
        """Return a predefined response in Demo Mode."""

        try:
            return get_demo_response(query)

        except Exception:
            return (
                "Demo Mode is active, but no demo response "
                "was found for this question."
            )

    # =========================================================
    # MODEL INFORMATION
    # =========================================================

    def get_current_model(self):
        """Return the currently selected model."""

        return self.model

    # =========================================================
    # DEMO MODE STATUS
    # =========================================================

    def is_demo_mode(self):
        """Return whether Demo Mode is active."""

        return self.demo_mode