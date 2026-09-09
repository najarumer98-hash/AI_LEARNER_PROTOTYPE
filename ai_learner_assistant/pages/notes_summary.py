"""
Notes & Summary Generator Page
"""
import streamlit as st
from llm_service import LLMService
from prompts import SUMMARY_PROMPT

def show_notes_summary(agent):
    st.markdown('<div class="main-header">📝 Notes & Summary Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Generate concise study notes from your materials</div>', unsafe_allow_html=True)

    st.markdown("""
    Paste your academic text, lecture notes, or reading materials below.
    The AI will generate a structured summary with key points, important terms, and exam-focused insights.
    """)

    st.markdown("---")

    # Input area
    text_input = st.text_area(
        "Paste your academic text here:",
        height=250,
        placeholder="Enter lecture notes, textbook excerpts, or any study material..."
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        include_summary = st.checkbox("Brief Summary", value=True)
    with col2:
        include_key_points = st.checkbox("Key Points", value=True)
    with col3:
        include_terms = st.checkbox("Important Terms", value=True)

    include_exam_focus = st.checkbox("Exam-Focused Points", value=True)

    if st.button("📄 Generate Summary", type="primary", use_container_width=True):
        if not text_input or len(text_input.strip()) < 50:
            st.error("Please enter at least 50 characters of text to summarize!")
        else:
            with st.spinner("📝 Analyzing and summarizing your text..."):
                llm_service = LLMService()

                if llm_service.is_demo_mode():
                    # Demo response
                    st.success("✅ Summary Generated!")
                    st.markdown("---")

                    if include_summary:
                        st.markdown("## 📋 Brief Summary")
                        st.info("""
                        Database normalization is a systematic approach to organizing data in a database to reduce redundancy
                        and improve data integrity. The process involves dividing large tables into smaller ones and defining
                        relationships between them. The main goal is to eliminate duplicate data and ensure data dependencies
                        make sense, ultimately leading to more efficient database operations and easier maintenance.
                        """)

                    if include_key_points:
                        st.markdown("## 🎯 Key Points")
                        st.markdown("""
                        - **Purpose**: Reduce data redundancy and improve integrity
                        - **Process**: Decompose tables into smaller, related tables
                        - **Normal Forms**: Progressive levels (1NF, 2NF, 3NF, BCNF)
                        - **1NF**: Atomic values, no repeating groups
                        - **2NF**: No partial dependencies on primary key
                        - **3NF**: No transitive dependencies
                        - **Benefits**: Data consistency, easier updates, reduced storage
                        - **Trade-offs**: May require more joins, can impact query performance
                        """)

                    if include_terms:
                        st.markdown("## 📚 Important Terms")
                        st.markdown("""
                        **Normalization**: The process of organizing database schema to minimize redundancy

                        **Redundancy**: Duplicate storage of the same data in multiple places

                        **Functional Dependency**: When one attribute uniquely determines another

                        **Primary Key**: Unique identifier for each record in a table

                        **Partial Dependency**: Non-key attribute depends on part of a composite key

                        **Transitive Dependency**: Non-key attribute depends on another non-key attribute

                        **Atomic Value**: Indivisible data unit, cannot be broken down further

                        **Candidate Key**: Minimal set of attributes that uniquely identify a record
                        """)

                    if include_exam_focus:
                        st.markdown("## 🎓 Exam-Focused Points")
                        st.markdown("""
                        **Most Likely to be Tested:**

                        1. **Define each normal form** - Be able to explain 1NF, 2NF, and 3NF with examples

                        2. **Identify violations** - Given a table, identify which normal form is violated

                        3. **Normalization process** - Convert unnormalized tables to 3NF step-by-step

                        4. **Functional dependencies** - Determine FDs from table data

                        5. **Benefits vs Trade-offs** - Explain when to normalize and when denormalization is acceptable

                        6. **Real-world scenarios** - Apply normalization to practical database design problems

                        **Common Exam Questions:**
                        - "Normalize the following table to 3NF"
                        - "What normal form is this table in and why?"
                        - "Identify all functional dependencies"
                        - "Explain the purpose of normalization"
                        """)

                    # Log analytics
                    agent.analytics.log_summary()

                else:
                    # Real API call
                    prompt = SUMMARY_PROMPT.format(text=text_input)
                    response = llm_service.generate_response(prompt, "Summarize this academic text")

                    st.success("✅ Summary Generated!")
                    st.markdown("---")
                    st.markdown(response)

                    # Log analytics
                    agent.analytics.log_summary()

    # Example text
    st.markdown("---")
    with st.expander("💡 Try with Example Text"):
        example_text = """
Database normalization is a database schema design technique, by which an existing schema is modified to minimize redundancy and dependency of data. Normalization split a large table into smaller tables and define relationships between them to increases the clarity in organizing data.

The main purpose of normalization is to reduce data redundancy and improve data integrity. This also helps in reducing the space used by the database and making it more efficient. Normalization is typically done in stages called normal forms.

First Normal Form (1NF) requires that the values in each column of a table are atomic, meaning they cannot be divided. For example, if a table has a column for phone numbers, each cell in that column should contain only one phone number.

Second Normal Form (2NF) requires that the table is in 1NF and that all non-key attributes are fully dependent on the primary key. This means removing partial dependencies where a non-key attribute depends on only part of a composite primary key.

Third Normal Form (3NF) requires that the table is in 2NF and that all the attributes are directly dependent on the primary key. This means removing transitive dependencies where a non-key attribute depends on another non-key attribute.

The benefits of normalization include data consistency, as changes to data only need to be made in one place. It also reduces data redundancy, which saves storage space. Updates, insertions, and deletions become easier and less error-prone.

However, normalization can also have drawbacks. Highly normalized databases may require more complex queries with multiple joins, which can impact performance. Therefore, sometimes a balance must be struck between normalization and performance requirements.
        """

        st.text_area("Example text (click button below to use):", value=example_text, height=200, disabled=True)

        if st.button("📋 Use This Example"):
            st.session_state.example_text = example_text
            st.rerun()

    # Tips
    with st.expander("📖 Tips for Best Results"):
        st.markdown("""
        **For Best Summaries:**
        - Provide complete paragraphs rather than bullet points
        - Include at least 100-200 words of text
        - Use properly formatted academic text
        - Include context (subject, topic) if available
        - Paste lecture notes, textbook sections, or articles

        **What Works Well:**
        - Lecture transcripts
        - Textbook chapters
        - Research paper sections
        - Study guides
        - Course handouts

        **What Doesn't Work Well:**
        - Very short text (< 50 words)
        - Code snippets without explanation
        - Lists of definitions only
        - Fragmented notes
        """)
