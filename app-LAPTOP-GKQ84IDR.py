import streamlit as st
import pandas as pd
import re

from courses import courses

from coding_profiles import (
    get_leetcode_profile,
    get_codeforces_profile,
    get_codechef_profile
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SkillHackAI",
    page_icon="🚀",
    layout="wide"
)


# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fb;
}

.block-container {
    padding-top: 2rem;
}

.title {
    font-size: 42px;
    font-weight: 800;
    color: #4f46e5;
}

.subtitle {
    font-size: 18px;
    color: #64748b;
}

.card {
    background: white;
    padding: 22px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}

.metric-card {
    background: linear-gradient(135deg, #eef2ff, #ffffff);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

.metric-title {
    font-size: 15px;
    color: #64748b;
}

.metric-value {
    font-size: 30px;
    font-weight: 800;
    color: #4f46e5;
}

.skill-badge {
    display: inline-block;
    padding: 8px 14px;
    margin: 5px;
    border-radius: 20px;
    background: #eef2ff;
    color: #4338ca;
    font-weight: 600;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    color: #1e293b;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🚀 SkillHackAI")

st.sidebar.markdown("### 🧭 Career Command Center")

page = st.sidebar.radio(
    "Choose a feature",
    [
        "🏠 Career Analysis",
        "💻 Coding Profiles"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "SkillHackAI analyzes your resume, "
    "skills, career path and coding profiles."
)


# =========================================================
# CODING PROFILES
# =========================================================

if page == "💻 Coding Profiles":

    st.markdown(
        '<div class="title">💻 Coding Profile Analyzer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Analyze your competitive programming and coding journey.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")


    # =====================================================
    # LEETCODE
    # =====================================================

    st.markdown(
        '<div class="section-title">🟡 LeetCode</div>',
        unsafe_allow_html=True
    )

    leetcode_username = st.text_input(
        "LeetCode Username",
        placeholder="Enter your LeetCode username",
        key="leetcode_username"
    )

    analyze_leetcode = st.button(
        "🔍 Analyze LeetCode",
        key="analyze_leetcode"
    )


    if analyze_leetcode:

        if not leetcode_username.strip():

            st.warning(
                "Please enter a LeetCode username."
            )

        else:

            with st.spinner(
                "Fetching LeetCode profile..."
            ):

                leetcode_data = get_leetcode_profile(
                    leetcode_username
                )


            if leetcode_data is None:

                st.error(
                    "❌ Unable to fetch this LeetCode profile. "
                    "Please check the username."
                )

            else:

                st.success(
                    f"Profile loaded: "
                    f"{leetcode_data['username']}"
                )


                # =========================================
                # MAIN PROFILE
                # =========================================

                st.markdown("### 📊 Profile Overview")

                col1, col2, col3, col4 = st.columns(4)


                with col1:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">
                                🧩 Problems Solved
                            </div>
                            <div class="metric-value">
                                {leetcode_data['total']}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                with col2:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">
                                ⭐ Contest Rating
                            </div>
                            <div class="metric-value">
                                {leetcode_data['rating']}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                with col3:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">
                                🌍 Global Ranking
                            </div>
                            <div class="metric-value">
                                {leetcode_data['ranking']}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                with col4:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">
                                👍 Reputation
                            </div>
                            <div class="metric-value">
                                {leetcode_data['reputation']}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                st.markdown("---")


                # =========================================
                # DIFFICULTY
                # =========================================

                st.markdown(
                    "### 🧩 Problems Solved by Difficulty"
                )


                easy = leetcode_data["easy"]
                medium = leetcode_data["medium"]
                hard = leetcode_data["hard"]
                total = leetcode_data["total"]


                col1, col2, col3, col4 = st.columns(4)


                with col1:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">
                                🟢 Easy
                            </div>
                            <div class="metric-value">
                                {easy}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                with col2:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">
                                🟡 Medium
                            </div>
                            <div class="metric-value">
                                {medium}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                with col3:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">
                                🔴 Hard
                            </div>
                            <div class="metric-value">
                                {hard}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                with col4:

                    st.markdown(
                        f"""
                        <div class="metric-card">
                            <div class="metric-title">
                                🔵 Total
                            </div>
                            <div class="metric-value">
                                {total}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )


                # =========================================
                # GRAPH
                # =========================================

                st.markdown(
                    "### 📈 Difficulty Visualization"
                )


                difficulty_df = pd.DataFrame(
                    {
                        "Difficulty": [
                            "Easy",
                            "Medium",
                            "Hard"
                        ],
                        "Problems": [
                            easy,
                            medium,
                            hard
                        ]
                    }
                )


                st.bar_chart(
                    difficulty_df.set_index(
                        "Difficulty"
                    )
                )


                # =========================================
                # CONTEST
                # =========================================

                st.markdown("---")

                st.markdown(
                    "### 🏆 Contest Performance"
                )


                col1, col2, col3, col4 = st.columns(4)


                with col1:

                    st.metric(
                        "Contest Rating",
                        leetcode_data["rating"]
                    )


                with col2:

                    st.metric(
                        "Global Contest Rank",
                        leetcode_data["contest_rank"]
                    )


                with col3:

                    st.metric(
                        "Top Percentage",
                        leetcode_data["top_percentage"]
                    )


                with col4:

                    st.metric(
                        "Contests Attended",
                        leetcode_data["contests"]
                    )


                # =========================================
                # LANGUAGES
                # =========================================

                st.markdown("---")

                st.markdown(
                    "### 💻 Programming Languages"
                )


                languages = leetcode_data["languages"]


                if languages:

                    language_df = pd.DataFrame(
                        languages
                    )


                    language_df = language_df.rename(
                        columns={
                            "language": "Language",
                            "problems": "Problems Solved"
                        }
                    )


                    col1, col2 = st.columns(2)


                    with col1:

                        st.dataframe(
                            language_df,
                            use_container_width=True,
                            hide_index=True
                        )


                    with col2:

                        st.bar_chart(
                            language_df.set_index(
                                "Language"
                            )
                        )

                else:

                    st.info(
                        "No programming language data available."
                    )


                # =========================================
                # BADGES
                # =========================================

                st.markdown("---")

                st.markdown(
                    "### 🏅 Badges"
                )


                badges = leetcode_data["badges"]


                if badges:

                    for badge in badges:

                        st.markdown(
                            f"""
                            <span class="skill-badge">
                                🏅 {badge}
                            </span>
                            """,
                            unsafe_allow_html=True
                        )

                else:

                    st.info(
                        "No badges found."
                    )


    # =====================================================
    # CODEFORCES
    # =====================================================

    st.markdown("---")

    st.markdown(
        '<div class="section-title">🔵 Codeforces</div>',
        unsafe_allow_html=True
    )


    codeforces_username = st.text_input(
        "Codeforces Username",
        placeholder="Enter your Codeforces username",
        key="codeforces_username"
    )


    analyze_codeforces = st.button(
        "🔍 Analyze Codeforces",
        key="analyze_codeforces"
    )


    if analyze_codeforces:

        if not codeforces_username.strip():

            st.warning(
                "Please enter a Codeforces username."
            )

        else:

            with st.spinner(
                "Fetching Codeforces profile..."
            ):

                codeforces_data = get_codeforces_profile(
                    codeforces_username
                )


            if codeforces_data is None:

                st.error(
                    "❌ Unable to fetch Codeforces profile."
                )

            else:

                st.success(
                    f"Profile loaded: "
                    f"{codeforces_data['username']}"
                )


                col1, col2, col3, col4 = st.columns(4)


                with col1:

                    st.metric(
                        "Current Rating",
                        codeforces_data["rating"]
                    )


                with col2:

                    st.metric(
                        "Maximum Rating",
                        codeforces_data["max_rating"]
                    )


                with col3:

                    st.metric(
                        "Current Rank",
                        codeforces_data["rank"]
                    )


                with col4:

                    st.metric(
                        "Maximum Rank",
                        codeforces_data["max_rank"]
                    )


                st.markdown(
                    "### 📊 Rating Visualization"
                )


                rating_df = pd.DataFrame(
                    {
                        "Rating Type": [
                            "Current Rating",
                            "Maximum Rating"
                        ],
                        "Rating": [
                            codeforces_data["rating"],
                            codeforces_data["max_rating"]
                        ]
                    }
                )


                st.bar_chart(
                    rating_df.set_index(
                        "Rating Type"
                    )
                )


    # =====================================================
    # CODECHEF
    # =====================================================

    st.markdown("---")

    st.markdown(
        '<div class="section-title">🟣 CodeChef</div>',
        unsafe_allow_html=True
    )


    codechef_username = st.text_input(
        "CodeChef Username",
        placeholder="Enter your CodeChef username",
        key="codechef_username"
    )


    analyze_codechef = st.button(
        "🔍 Analyze CodeChef",
        key="analyze_codechef"
    )


    if analyze_codechef:

        if not codechef_username.strip():

            st.warning(
                "Please enter a CodeChef username."
            )

        else:

            codechef_data = get_codechef_profile(
                codechef_username
            )


            st.success(
                f"CodeChef profile found: "
                f"{codechef_data['username']}"
            )


            st.markdown(
                f"🔗 CodeChef Profile: "
                f"{codechef_data['profile_url']}"
            )


            st.info(
                "Detailed CodeChef statistics will be added "
                "in the next development step."
            )


    st.markdown("---")

    st.info(
        "🚀 SkillHackAI Coding Analyzer"
    )

    st.stop()


# =========================================================
# CAREER ANALYSIS
# =========================================================

st.markdown(
    '<div class="title">🚀 SkillHackAI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI Career Command Center — Resume, Skills, Jobs and Learning'
    '</div>',
    unsafe_allow_html=True
)

st.markdown("---")


# =========================================================
# RESUME
# =========================================================

st.markdown("## 📄 Upload Your Resume")


uploaded_file = st.file_uploader(
    "Upload PDF or DOCX",
    type=["pdf", "docx"]
)


resume_text = ""


if uploaded_file:

    file_name = uploaded_file.name.lower()


    if file_name.endswith(".pdf"):

        from pypdf import PdfReader

        reader = PdfReader(
            uploaded_file
        )

        for page_content in reader.pages:

            text = page_content.extract_text()

            if text:

                resume_text += text + "\n"


    elif file_name.endswith(".docx"):

        from docx import Document

        document = Document(
            uploaded_file
        )

        for paragraph in document.paragraphs:

            resume_text += (
                paragraph.text + "\n"
            )


    if resume_text.strip():

        st.success(
            "✅ Resume uploaded successfully."
        )


        with st.expander(
            "👀 View Extracted Resume Text"
        ):

            st.write(
                resume_text
            )


# =========================================================
# SKILLS
# =========================================================

st.markdown(
    "## 🧠 Skill Extraction"
)


skill_list = [

    "python",
    "java",
    "sql",
    "machine learning",
    "deep learning",
    "data science",
    "data analysis",
    "html",
    "css",
    "javascript",
    "react",
    "node.js",
    "git",
    "github",
    "docker",
    "kubernetes",
    "aws",
    "azure",
    "c++",
    "c#",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch"

]


def extract_skills(text):

    found_skills = []

    text_lower = text.lower()


    for skill in skill_list:

        pattern = (
            r"\b"
            + re.escape(skill)
            + r"\b"
        )


        if re.search(
            pattern,
            text_lower
        ):

            found_skills.append(
                skill
            )


    return found_skills


if resume_text:

    detected_skills = extract_skills(
        resume_text
    )


    if detected_skills:

        st.success(
            f"Detected {len(detected_skills)} skills."
        )


        for skill in detected_skills:

            st.markdown(
                f"""
                <span class="skill-badge">
                    {skill.title()}
                </span>
                """,
                unsafe_allow_html=True
            )

    else:

        st.warning(
            "No matching skills detected."
        )


# =========================================================
# CAREER PREDICTION
# =========================================================

st.markdown("---")

st.markdown(
    "## 🎯 Career Prediction"
)


job_roles = [

    "Data Scientist",
    "Machine Learning Engineer",
    "Software Developer",
    "Web Developer",
    "Data Analyst"

]


selected_role = st.selectbox(
    "Select your target career role",
    job_roles
)


if st.button(
    "🤖 Analyze Career"
):

    st.success(
        f"Your selected career path is: "
        f"**{selected_role}**"
    )


# =========================================================
# JOB DESCRIPTION
# =========================================================

st.markdown("---")

st.markdown(
    "## 💼 Job Description Matching"
)


job_description = st.text_area(
    "Paste the Job Description",
    placeholder="Paste the job description here..."
)


if job_description and resume_text:

    jd_skills = extract_skills(
        job_description
    )

    resume_skills = extract_skills(
        resume_text
    )


    matched_skills = list(
        set(resume_skills)
        & set(jd_skills)
    )


    missing_skills = list(
        set(jd_skills)
        - set(resume_skills)
    )


    if jd_skills:

        match_percentage = (
            len(matched_skills)
            / len(jd_skills)
        ) * 100


        st.markdown(
            "### 📊 Job Match Score"
        )


        st.progress(
            int(match_percentage)
        )


        st.success(
            f"{match_percentage:.1f}% Match"
        )


        col1, col2 = st.columns(2)


        with col1:

            st.markdown(
                "### ✅ Matched Skills"
            )


            for skill in matched_skills:

                st.markdown(
                    f"""
                    <span class="skill-badge">
                        ✅ {skill.title()}
                    </span>
                    """,
                    unsafe_allow_html=True
                )


        with col2:

            st.markdown(
                "### ❌ Missing Skills"
            )


            for skill in missing_skills:

                st.markdown(
                    f"""
                    <span class="skill-badge">
                        ❌ {skill.title()}
                    </span>
                    """,
                    unsafe_allow_html=True
                )


        # =============================================
        # SKILL GAP
        # =============================================

        st.markdown(
            "### 📈 Skill Gap Visualization"
        )


        skill_gap_df = pd.DataFrame(
            {
                "Category": [
                    "Matched",
                    "Missing"
                ],
                "Skills": [
                    len(matched_skills),
                    len(missing_skills)
                ]
            }
        )


        st.bar_chart(
            skill_gap_df.set_index(
                "Category"
            )
        )


        # =============================================
        # COURSES
        # =============================================

        st.markdown("---")

        st.markdown(
            "## 📚 Personalized Learning"
        )


        skill_course_mapping = {

            "python":
                "python",

            "sql":
                "sql",

            "machine learning":
                "machine learning",

            "html":
                "web development",

            "css":
                "web development",

            "javascript":
                "web development",

            "git":
                "git",

            "github":
                "git",

            "docker":
                "docker"

        }


        recommended_courses = []


        for skill in missing_skills:

            course_key = (
                skill_course_mapping.get(
                    skill
                )
            )


            if course_key:

                if (
                    course_key
                    not in recommended_courses
                ):

                    recommended_courses.append(
                        course_key
                    )


        if recommended_courses:

            st.success(
                "🎯 Courses selected based "
                "on your skill gaps."
            )


            for course_key in recommended_courses:

                course = courses[
                    course_key
                ]


                st.markdown(
                    f"""
                    <div class="card">
                        <h3>
                            📘 {course['title']}
                        </h3>
                        <p>
                            {course['description']}
                        </p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


                progress_key = (
                    f"progress_{course_key}"
                )


                if (
                    progress_key
                    not in st.session_state
                ):

                    st.session_state[
                        progress_key
                    ] = 0


                total_lessons = len(
                    course["lessons"]
                )


                completed_lessons = (
                    st.session_state[
                        progress_key
                    ]
                )


                st.write(
                    f"Progress: "
                    f"{completed_lessons}/"
                    f"{total_lessons} lessons"
                )


                progress = (
                    completed_lessons
                    / total_lessons
                )


                st.progress(
                    progress
                )


                if (
                    completed_lessons
                    < total_lessons
                ):

                    if st.button(
                        "▶️ Complete Next Lesson",
                        key=f"lesson_{course_key}"
                    ):

                        st.session_state[
                            progress_key
                        ] += 1

                        st.rerun()


                else:

                    st.success(
                        "🎉 Course Completed!"
                    )


        else:

            st.info(
                "No matching in-app course is "
                "currently available."
            )


# =========================================================
# ROADMAP
# =========================================================

st.markdown("---")

st.markdown(
    "## 🗺️ Career Roadmap"
)


roadmap = [

    "📄 Upload Resume",
    "🧠 Extract Skills",
    "🎯 Identify Career Goal",
    "💼 Compare Job Description",
    "📊 Find Skill Gaps",
    "📚 Complete Personalized Courses",
    "💻 Improve Coding Profiles",
    "🚀 Become Job Ready"

]


for index, step in enumerate(
    roadmap,
    start=1
):

    st.markdown(
        f"""
        <div class="card">
            <b>Step {index}</b> — {step}
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#64748b;">
        🚀 <b>SkillHackAI</b> — AI Career Command Center
        <br>
        Resume • Skills • Jobs • Courses • Coding Profiles
    </div>
    """,
    unsafe_allow_html=True
)