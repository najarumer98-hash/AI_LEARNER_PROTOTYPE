"""
Resources Page
"""
import streamlit as st
from resource_recommender import ResourceRecommender
from config import SUBJECTS, DIFFICULTY_LEVELS

def show_resources():
    st.markdown('<div class="main-header">📖 Learning Resources</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Explore curated learning materials</div>', unsafe_allow_html=True)

    recommender = ResourceRecommender()

    st.markdown("---")

    # Search and filter
    col1, col2, col3 = st.columns(3)

    with col1:
        search_term = st.text_input("🔍 Search resources", placeholder="e.g., Python, SQL, Machine Learning")

    with col2:
        filter_subject = st.selectbox("Filter by Subject", ["All"] + SUBJECTS)

    with col3:
        filter_difficulty = st.selectbox("Filter by Difficulty", ["All"] + DIFFICULTY_LEVELS)

    st.markdown("---")

    # Get resources
    if search_term:
        resources = recommender.search_resources(search_term)
        st.markdown(f"### 🔍 Search Results for '{search_term}'")
    else:
        resources = recommender.resources

    # Apply filters
    if filter_subject != "All":
        resources = [r for r in resources if r['subject'] == filter_subject]

    if filter_difficulty != "All":
        resources = [r for r in resources if r['difficulty'] == filter_difficulty]

    # Display resource count
    st.info(f"📚 Showing {len(resources)} resources")

    # Display resources
    if resources:
        for resource in resources:
            with st.container():
                st.markdown(f"""
                <div class="resource-card">
                    <h3>📘 {resource['title']}</h3>
                    <p><strong>Subject:</strong> {resource['subject']} |
                    <strong>Topic:</strong> {resource['topic']} |
                    <strong>Difficulty:</strong> {resource['difficulty']} |
                    <strong>Type:</strong> {resource['type']}</p>
                    <p>{resource['description']}</p>
                    <a href="{resource['url']}" target="_blank">🔗 Access Resource →</a>
                </div>
                """, unsafe_allow_html=True)
                st.markdown("")

    else:
        st.warning("No resources found matching your criteria. Try adjusting your filters.")

    # Statistics
    st.markdown("---")
    st.markdown("## 📊 Resource Statistics")

    col1, col2, col3 = st.columns(3)

    all_resources = recommender.resources

    with col1:
        st.metric("Total Resources", len(all_resources))

    with col2:
        subjects_count = len(set(r['subject'] for r in all_resources))
        st.metric("Subjects Covered", subjects_count)

    with col3:
        beginner_count = len([r for r in all_resources if r['difficulty'] == 'Beginner'])
        st.metric("Beginner Resources", beginner_count)

    # Resources by subject
    st.markdown("---")
    with st.expander("📚 Resources by Subject"):
        subject_counts = {}
        for r in all_resources:
            subject = r['subject']
            subject_counts[subject] = subject_counts.get(subject, 0) + 1

        for subject, count in sorted(subject_counts.items(), key=lambda x: x[1], reverse=True):
            st.markdown(f"**{subject}**: {count} resources")

    # Add resource suggestion
    st.markdown("---")
    st.markdown("## 💡 Suggest a Resource")

    with st.form("suggest_resource"):
        st.markdown("Have a great learning resource to recommend? Let us know!")

        col1, col2 = st.columns(2)
        with col1:
            suggest_title = st.text_input("Resource Title")
            suggest_subject = st.selectbox("Subject", SUBJECTS)
        with col2:
            suggest_url = st.text_input("URL")
            suggest_difficulty = st.selectbox("Difficulty", DIFFICULTY_LEVELS)

        suggest_description = st.text_area("Description")

        submitted = st.form_submit_button("Submit Suggestion")

        if submitted:
            if suggest_title and suggest_url and suggest_description:
                st.success("✅ Thank you for your suggestion! (Note: This is a demo - submissions are not actually saved)")
            else:
                st.error("Please fill in all fields")

    # Quick access
    st.markdown("---")
    st.markdown("## ⚡ Quick Access by Subject")

    quick_subjects = ["Python", "DBMS", "Data Structures", "Machine Learning", "Artificial Intelligence"]

    cols = st.columns(len(quick_subjects))

    for idx, subject in enumerate(quick_subjects):
        with cols[idx]:
            if st.button(f"📚 {subject}", use_container_width=True):
                st.session_state.quick_subject = subject
                st.rerun()

    # Tips
    with st.expander("💡 How to Use Resources Effectively"):
        st.markdown("""
        **Study Tips:**
        - Start with Beginner resources if you're new to a topic
        - Follow a structured learning path: Documentation → Tutorials → Practice
        - Don't just read - practice by coding/solving problems
        - Use multiple resources for difficult topics
        - Bookmark resources you find helpful

        **Resource Types:**
        - **Documentation**: Official references, best for looking up specific features
        - **Tutorial**: Step-by-step guides, best for learning new topics
        - **Course**: Structured learning paths, best for comprehensive understanding
        - **Article**: Quick reads on specific topics
        - **Book**: In-depth coverage, best for mastery

        **Learning Path Example:**
        1. Start with basic tutorials
        2. Practice with coding exercises
        3. Read official documentation
        4. Build small projects
        5. Tackle advanced topics
        6. Contribute to open source or build portfolio projects
        """)
