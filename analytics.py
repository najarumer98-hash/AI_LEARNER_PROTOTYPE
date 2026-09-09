"""
Analytics tracker for student interactions
"""
import json
import os
from datetime import datetime
from collections import Counter

class Analytics:
    """Track and analyze student interactions"""

    def __init__(self, data_file="analytics_data.json"):
        self.data_file = data_file
        self.session_data = {
            "total_queries": 0,
            "queries_by_category": {},
            "queries_answered_by_ai": 0,
            "queries_escalated": 0,
            "resources_recommended": 0,
            "quizzes_generated": 0,
            "study_plans_created": 0,
            "summaries_generated": 0,
            "subjects_queried": {},
            "query_history": []
        }
        self._load_data()

    def _load_data(self):
        """Load existing analytics data"""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    self.session_data = json.load(f)
        except Exception as e:
            print(f"Could not load analytics data: {e}")

    def _save_data(self):
        """Save analytics data"""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(self.session_data, f, indent=2)
        except Exception as e:
            print(f"Could not save analytics data: {e}")

    def log_query(self, query, category, action, escalated=False, subject="General"):
        """Log a student query"""
        self.session_data["total_queries"] += 1

        # Update category count
        if category not in self.session_data["queries_by_category"]:
            self.session_data["queries_by_category"][category] = 0
        self.session_data["queries_by_category"][category] += 1

        # Update action counts
        if escalated:
            self.session_data["queries_escalated"] += 1
        else:
            self.session_data["queries_answered_by_ai"] += 1

        # Update subject count
        if subject not in self.session_data["subjects_queried"]:
            self.session_data["subjects_queried"][subject] = 0
        self.session_data["subjects_queried"][subject] += 1

        # Log to history
        self.session_data["query_history"].append({
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "query": query[:100],  # Store first 100 chars
            "category": category,
            "action": action,
            "escalated": escalated,
            "subject": subject
        })

        self._save_data()

    def log_resource_recommendation(self, count=1):
        """Log resource recommendation"""
        self.session_data["resources_recommended"] += count
        self._save_data()

    def log_quiz_generation(self):
        """Log quiz generation"""
        self.session_data["quizzes_generated"] += 1
        self._save_data()

    def log_study_plan(self):
        """Log study plan creation"""
        self.session_data["study_plans_created"] += 1
        self._save_data()

    def log_summary(self):
        """Log summary generation"""
        self.session_data["summaries_generated"] += 1
        self._save_data()

    def get_summary(self):
        """Get analytics summary"""
        return {
            "total_queries": self.session_data["total_queries"],
            "ai_answered": self.session_data["queries_answered_by_ai"],
            "escalated": self.session_data["queries_escalated"],
            "resources_recommended": self.session_data["resources_recommended"],
            "quizzes_generated": self.session_data["quizzes_generated"],
            "study_plans_created": self.session_data["study_plans_created"],
            "summaries_generated": self.session_data["summaries_generated"],
            "top_category": self._get_top_category(),
            "top_subject": self._get_top_subject(),
            "categories": self.session_data["queries_by_category"],
            "subjects": self.session_data["subjects_queried"]
        }

    def _get_top_category(self):
        """Get most common category"""
        if not self.session_data["queries_by_category"]:
            return "None"
        return max(self.session_data["queries_by_category"].items(), key=lambda x: x[1])[0]

    def _get_top_subject(self):
        """Get most queried subject"""
        if not self.session_data["subjects_queried"]:
            return "None"
        return max(self.session_data["subjects_queried"].items(), key=lambda x: x[1])[0]

    def get_recent_queries(self, limit=10):
        """Get recent queries"""
        return self.session_data["query_history"][-limit:]

    def reset_analytics(self):
        """Reset all analytics data"""
        self.session_data = {
            "total_queries": 0,
            "queries_by_category": {},
            "queries_answered_by_ai": 0,
            "queries_escalated": 0,
            "resources_recommended": 0,
            "quizzes_generated": 0,
            "study_plans_created": 0,
            "summaries_generated": 0,
            "subjects_queried": {},
            "query_history": []
        }
        self._save_data()
