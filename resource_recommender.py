"""
Resource recommender for suggesting learning materials
"""
import json
import os
from typing import List, Dict

class ResourceRecommender:
    """Recommends relevant learning resources based on queries"""

    def __init__(self, resources_file="data/resources.json"):
        self.resources_file = resources_file
        self.resources = self._load_resources()

    def _load_resources(self):
        """Load resources from JSON file"""
        try:
            file_path = os.path.join(os.path.dirname(__file__), self.resources_file)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            else:
                return []
        except Exception as e:
            print(f"Error loading resources: {e}")
            return []

    def recommend(self, query, category="", top_n=3):
        """
        Recommend resources based on query
        Returns list of relevant resources
        """
        if not self.resources:
            return []

        query_lower = query.lower()
        scored_resources = []

        for resource in self.resources:
            score = self._calculate_relevance_score(query_lower, resource)
            if score > 0:
                scored_resources.append((score, resource))

        # Sort by score and return top N
        scored_resources.sort(reverse=True, key=lambda x: x[0])
        return [resource for score, resource in scored_resources[:top_n]]

    def _calculate_relevance_score(self, query_lower, resource):
        """Calculate relevance score for a resource"""
        score = 0

        # Check title
        if any(word in resource['title'].lower() for word in query_lower.split()):
            score += 10

        # Check subject
        if any(word in resource['subject'].lower() for word in query_lower.split()):
            score += 8

        # Check topic
        if any(word in resource['topic'].lower() for word in query_lower.split()):
            score += 6

        # Check description
        if any(word in resource['description'].lower() for word in query_lower.split()):
            score += 3

        # Keyword matching
        keywords = query_lower.split()
        for keyword in keywords:
            if keyword in resource['title'].lower():
                score += 5
            if keyword in resource['topic'].lower():
                score += 3

        return score

    def get_resources_by_subject(self, subject):
        """Get all resources for a specific subject"""
        return [r for r in self.resources if r['subject'].lower() == subject.lower()]

    def get_resources_by_difficulty(self, difficulty):
        """Get resources by difficulty level"""
        return [r for r in self.resources if r['difficulty'].lower() == difficulty.lower()]

    def search_resources(self, search_term):
        """Search resources by any field"""
        search_lower = search_term.lower()
        results = []

        for resource in self.resources:
            if (search_lower in resource['title'].lower() or
                search_lower in resource['subject'].lower() or
                search_lower in resource['topic'].lower() or
                search_lower in resource['description'].lower()):
                results.append(resource)

        return results
