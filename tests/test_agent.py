"""
Test suite for AI Learner Assistant
"""
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classifier import QueryClassifier
from escalation import EscalationEngine
from resource_recommender import ResourceRecommender
from analytics import Analytics

def test_classifier():
    """Test query classification"""
    print("Testing Query Classifier...")
    classifier = QueryClassifier()

    # Test concept explanation
    query1 = "What is normalization in DBMS?"
    category1, reason1 = classifier.classify(query1)
    assert category1 == "Concept Explanation", f"Expected 'Concept Explanation', got '{category1}'"
    print(f"✓ Test 1 passed: '{query1}' → {category1}")

    # Test escalation
    query2 = "Can you change my grade?"
    category2, reason2 = classifier.classify(query2)
    assert category2 == "Faculty Escalation", f"Expected 'Faculty Escalation', got '{category2}'"
    print(f"✓ Test 2 passed: '{query2}' → {category2}")

    print("✅ Classifier tests passed!\n")

def test_escalation():
    """Test escalation detection"""
    print("Testing Escalation Engine...")
    escalation_engine = EscalationEngine()

    # Test should escalate
    query1 = "My teacher marked my assignment incorrectly"
    should_escalate1, reason1, action1 = escalation_engine.analyze(query1, "Faculty Escalation")
    assert should_escalate1 == True, "Expected escalation for grading dispute"
    print(f"✓ Test 1 passed: Grading dispute detected → Escalate")

    # Test should not escalate
    query2 = "Explain Python functions"
    should_escalate2, reason2, action2 = escalation_engine.analyze(query2, "Concept Explanation")
    assert should_escalate2 == False, "Expected no escalation for concept question"
    print(f"✓ Test 2 passed: Concept question → No escalation")

    # Test ticket generation
    ticket = escalation_engine.generate_escalation_ticket(
        "Change my grade",
        "Faculty Escalation",
        "Grading dispute"
    )
    assert "ticket_id" in ticket, "Ticket should have ID"
    assert ticket["priority"] in ["HIGH", "MEDIUM", "NORMAL"], "Invalid priority"
    print(f"✓ Test 3 passed: Escalation ticket generated")

    print("✅ Escalation tests passed!\n")

def test_resource_recommender():
    """Test resource recommendation"""
    print("Testing Resource Recommender...")
    recommender = ResourceRecommender()

    # Test resource loading
    assert len(recommender.resources) > 0, "Resources should be loaded"
    print(f"✓ Test 1 passed: Loaded {len(recommender.resources)} resources")

    # Test recommendation
    query = "Python OOP"
    recommendations = recommender.recommend(query, top_n=3)
    assert len(recommendations) > 0, "Should get recommendations for Python OOP"
    assert any("Python" in r['subject'] for r in recommendations), "Should recommend Python resources"
    print(f"✓ Test 2 passed: Found {len(recommendations)} relevant resources for '{query}'")

    # Test subject filtering
    python_resources = recommender.get_resources_by_subject("Python")
    assert len(python_resources) > 0, "Should find Python resources"
    print(f"✓ Test 3 passed: Found {len(python_resources)} Python resources")

    # Test difficulty filtering
    beginner_resources = recommender.get_resources_by_difficulty("Beginner")
    assert len(beginner_resources) > 0, "Should find beginner resources"
    print(f"✓ Test 4 passed: Found {len(beginner_resources)} beginner resources")

    print("✅ Resource recommender tests passed!\n")

def test_analytics():
    """Test analytics tracking"""
    print("Testing Analytics...")

    # Create temporary analytics with unique filename
    import tempfile
    temp_file = tempfile.mktemp(suffix=".json")
    analytics = Analytics(data_file=temp_file)

    # Test logging
    analytics.log_query("Test query", "Concept Explanation", "ANSWER", False, "Python")
    analytics.log_query("Test escalation", "Faculty Escalation", "ESCALATE", True, "General")

    summary = analytics.get_summary()
    assert summary["total_queries"] == 2, "Should have 2 queries"
    assert summary["ai_answered"] == 1, "Should have 1 AI answered"
    assert summary["escalated"] == 1, "Should have 1 escalated"
    print(f"✓ Test 1 passed: Query logging works")

    # Test category tracking
    assert "Concept Explanation" in summary["categories"], "Should track categories"
    print(f"✓ Test 2 passed: Category tracking works")

    # Test subject tracking
    assert "Python" in summary["subjects"], "Should track subjects"
    print(f"✓ Test 3 passed: Subject tracking works")

    # Cleanup
    if os.path.exists(temp_file):
        os.remove(temp_file)

    print("✅ Analytics tests passed!\n")

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("AI Learner Assistant - Test Suite")
    print("=" * 60 + "\n")

    try:
        test_classifier()
        test_escalation()
        test_resource_recommender()
        test_analytics()

        print("=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        return True

    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        return False
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
