"""
Analytics Dashboard Page
"""
import streamlit as st
import pandas as pd

def show_analytics(agent):
    st.markdown('<div class="main-header">📊 Analytics Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Track your learning interactions</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Get analytics data
    analytics_data = agent.get_analytics()

    # Key metrics
    st.markdown("## 📈 Key Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Queries", analytics_data['total_queries'], help="Total questions asked")

    with col2:
        st.metric("AI Answered", analytics_data['ai_answered'], help="Questions answered by AI")

    with col3:
        st.metric("Escalated", analytics_data['escalated'], help="Questions requiring faculty intervention")

    with col4:
        ai_percentage = (analytics_data['ai_answered'] / analytics_data['total_queries'] * 100) if analytics_data['total_queries'] > 0 else 0
        st.metric("AI Success Rate", f"{ai_percentage:.1f}%", help="Percentage of queries handled by AI")

    # Additional metrics
    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Resources Recommended", analytics_data['resources_recommended'])

    with col2:
        st.metric("Quizzes Generated", analytics_data['quizzes_generated'])

    with col3:
        st.metric("Study Plans Created", analytics_data['study_plans_created'])

    with col4:
        st.metric("Summaries Generated", analytics_data['summaries_generated'])

    # Top category and subject
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 Most Common Category")
        st.info(f"**{analytics_data['top_category']}**")

    with col2:
        st.markdown("### 📚 Most Queried Subject")
        st.info(f"**{analytics_data['top_subject']}**")

    # Categories breakdown
    st.markdown("---")
    st.markdown("## 📂 Queries by Category")

    if analytics_data['categories']:
        categories_df = pd.DataFrame(
            list(analytics_data['categories'].items()),
            columns=['Category', 'Count']
        ).sort_values('Count', ascending=False)

        col1, col2 = st.columns([2, 1])

        with col1:
            st.bar_chart(categories_df.set_index('Category'))

        with col2:
            st.dataframe(categories_df, hide_index=True, use_container_width=True)
    else:
        st.info("No data available yet. Start asking questions to see analytics!")

    # Subjects breakdown
    st.markdown("---")
    st.markdown("## 📚 Queries by Subject")

    if analytics_data['subjects']:
        subjects_df = pd.DataFrame(
            list(analytics_data['subjects'].items()),
            columns=['Subject', 'Count']
        ).sort_values('Count', ascending=False)

        col1, col2 = st.columns([2, 1])

        with col1:
            st.bar_chart(subjects_df.set_index('Subject'))

        with col2:
            st.dataframe(subjects_df, hide_index=True, use_container_width=True)
    else:
        st.info("No subject data available yet.")

    # Recent queries
    st.markdown("---")
    st.markdown("## 🕒 Recent Activity")

    recent_queries = agent.analytics.get_recent_queries(limit=10)

    if recent_queries:
        for query_data in reversed(recent_queries):
            with st.expander(f"📝 {query_data['timestamp']} - {query_data['category']}"):
                st.markdown(f"**Query:** {query_data['query']}")
                st.markdown(f"**Category:** {query_data['category']}")
                st.markdown(f"**Action:** {query_data['action']}")
                st.markdown(f"**Escalated:** {'Yes' if query_data['escalated'] else 'No'}")
                st.markdown(f"**Subject:** {query_data['subject']}")
    else:
        st.info("No recent activity to display.")

    # Insights
    st.markdown("---")
    st.markdown("## 💡 Insights & Recommendations")

    total = analytics_data['total_queries']

    if total == 0:
        st.info("Start using the AI Learner Assistant to see personalized insights!")
    else:
        insights = []

        # Escalation rate
        escalation_rate = (analytics_data['escalated'] / total * 100) if total > 0 else 0
        if escalation_rate > 30:
            insights.append("⚠️ **High escalation rate detected.** Many of your queries require faculty intervention. Consider asking more concept-focused questions that the AI can answer directly.")
        elif escalation_rate < 10:
            insights.append("✅ **Great query pattern!** Most of your questions can be answered by the AI, showing good use of the assistant for learning.")

        # Resource usage
        if analytics_data['resources_recommended'] == 0 and total > 5:
            insights.append("📚 **Explore resources!** You haven't checked recommended resources yet. Visit the Resources page for curated learning materials.")

        # Quiz usage
        if analytics_data['quizzes_generated'] == 0 and total > 5:
            insights.append("❓ **Test your knowledge!** Try generating quizzes to assess your understanding of topics you've learned.")

        # Study planning
        if analytics_data['study_plans_created'] == 0 and total > 5:
            insights.append("📅 **Plan your learning!** Create a study plan to organize your learning journey effectively.")

        # Top subject
        if analytics_data['top_subject'] != "None":
            insights.append(f"📖 **Focus area:** You're primarily learning about **{analytics_data['top_subject']}**. Consider exploring related topics to broaden your knowledge.")

        # Display insights
        if insights:
            for insight in insights:
                st.markdown(insight)
        else:
            st.success("🎯 You're using the assistant effectively! Keep up the great learning!")

    # Reset analytics
    st.markdown("---")

    col1, col2, col3 = st.columns([1, 1, 3])

    with col1:
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.rerun()

    with col2:
        if st.button("🗑️ Reset Analytics", type="secondary", use_container_width=True):
            agent.analytics.reset_analytics()
            st.success("Analytics data has been reset!")
            st.rerun()

    # Export data
    st.markdown("---")
    with st.expander("📥 Export Analytics Data"):
        st.markdown("Download your analytics data as JSON")

        import json

        export_data = {
            "summary": analytics_data,
            "recent_queries": recent_queries
        }

        st.download_button(
            label="Download JSON",
            data=json.dumps(export_data, indent=2),
            file_name="learning_analytics.json",
            mime="application/json"
        )

    # Learning statistics
    st.markdown("---")
    with st.expander("📊 Detailed Statistics"):
        st.json(analytics_data)
