import streamlit as st
import pandas as pd
import re
from pathlib import Path

from courses import courses
from course_content import course_content, get_course
from coding_profiles import (
    get_leetcode_profile,
    get_codeforces_profile,
    get_codechef_profile,
)

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SkillHackAI - AI Career Command Center",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>
.main { background: #f8f9ff; }
.block-container { padding-top: 1.2rem; padding-bottom: 3rem; }
.hero {
    padding: 28px;
    border-radius: 24px;
    background: linear-gradient(135deg,#ede9fe,#dbeafe,#fce7f3);
    margin-bottom: 22px;
    border: 1px solid #ddd6fe;
}
.card {
    padding: 20px;
    border-radius: 20px;
    background: white;
    border: 1px solid #e5e7eb;
    margin-bottom: 16px;
    box-shadow: 0 6px 18px rgba(79,70,229,.07);
}
.skill-card {
    padding: 14px;
    border-radius: 16px;
    background: linear-gradient(135deg,#ede9fe,#e0e7ff);
    border: 1px solid #ddd6fe;
    margin-bottom: 10px;
    text-align: center;
}
.gap-card {
    padding: 16px;
    border-radius: 16px;
    background: linear-gradient(135deg,#fff7ed,#fee2e2);
    border: 1px solid #fed7aa;
    margin-bottom: 10px;
}
.course-card {
    padding: 22px;
    border-radius: 22px;
    background: linear-gradient(135deg,#eef2ff,#f5f3ff,#fdf2f8);
    border: 1px solid #ddd6fe;
    margin-bottom: 18px;
}
.success-box {
    padding: 22px;
    border-radius: 20px;
    background: linear-gradient(135deg,#dcfce7,#d1fae5);
    border: 1px solid #86efac;
}
.metric-card {
    padding: 18px;
    border-radius: 18px;
    background: linear-gradient(135deg,#eef2ff,#f5f3ff);
    text-align: center;
}
.small-muted { color:#64748b; font-size:.9rem; }
.badge {
    display:inline-block;
    padding:7px 13px;
    border-radius:999px;
    background:#7c3aed;
    color:white;
    font-weight:700;
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SESSION STATE
# ============================================================

def init_state():
    defaults = {
        "resume_uploaded": False,
        "resume_text": "",
        "resume_skills": [],
        "job_description": "",
        "target_role": "Software Developer",
        "required_skills": [],
        "matched_skills": [],
        "missing_skills": [],
        "course_progress": {},
        "topic_scores": {},
        "final_scores": {},
        "completed_courses": set(),
        "completed_course_skills": set(),
        "selected_course": None,
        "analysis_done": False,
        "page": "🏠 Overview",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value.copy() if isinstance(value, (list, dict, set)) else value

init_state()

# ============================================================
# SKILL LIBRARY / COURSE MAPPING
# ============================================================

skill_list = [
    "python", "java", "c++", "javascript", "html", "css", "sql",
    "machine learning", "deep learning", "data science", "pandas", "numpy",
    "scikit-learn", "tensorflow", "pytorch", "git", "github", "docker",
    "aws", "azure", "react", "node.js", "flask", "django", "mongodb",
    "kubernetes", "cybersecurity", "software testing", "power bi", "excel",
    "rest api", "restful api", "data visualization", "statistics",
]

# A skill may point to one course. Some courses teach multiple related skills.
skill_course_mapping = {
    "python": "python",
    "sql": "sql",
    "machine learning": "machine-learning",
    "html": "web development",
    "css": "web development",
    "javascript": "web development",
    "git": "git",
    "github": "git",
    "docker": "docker",
    "java": "java",
    "c++": "cpp",
    "react": "react",
    "mongodb": "mongodb",
    "data science": "data-science",
    "deep learning": "deep-learning",
    "aws": "aws",
    "kubernetes": "kubernetes",
    "cybersecurity": "cybersecurity",
    "software testing": "software-testing",
    "power bi": "power-bi",
    "excel": "excel",
}

course_skill_map = {
    "python": {"python"},
    "sql": {"sql"},
    "machine-learning": {"machine learning"},
    "web development": {"html", "css", "javascript"},
    "git": {"git", "github"},
    "docker": {"docker"},
    "java": {"java"},
    "cpp": {"c++"},
    "react": {"react"},
    "mongodb": {"mongodb"},
    "data-science": {"data science", "pandas", "numpy"},
    "deep-learning": {"deep learning", "tensorflow", "pytorch"},
    "aws": {"aws"},
    "kubernetes": {"kubernetes"},
    "cybersecurity": {"cybersecurity"},
    "software-testing": {"software testing"},
    "power-bi": {"power bi"},
    "excel": {"excel"},
}

# ============================================================
# HELPERS
# ============================================================

def extract_skills(text):
    # Normalize common JD/resume formatting differences so that
    # "scikit learn", "scikit-learn", REST/API, etc. are detected reliably.
    text = (text or "").lower()
    text = text.replace("scikit learn", "scikit-learn")
    text = text.replace("restful apis", "rest api")
    text = text.replace("rest apis", "rest api")
    text = re.sub(r"[\u2010\u2011\u2012\u2013\u2014]", "-", text)

    found = []
    for skill in skill_list:
        if skill == "c++":
            pattern = r"(?<!\w)c\+\+(?!\w)"
        else:
            # Allow spaces, hyphens and punctuation between words where useful.
            parts = skill.split()
            if len(parts) > 1:
                pattern = r"(?<!\w)" + r"[\s\-]+".join(re.escape(p) for p in parts) + r"(?!\w)"
            else:
                pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"
        if re.search(pattern, text):
            found.append(skill)
    return list(dict.fromkeys(found))


def load_resume(file):
    text = ""
    name = file.name.lower()
    if name.endswith(".pdf"):
        from pypdf import PdfReader
        reader = PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    elif name.endswith(".docx"):
        from docx import Document
        document = Document(file)
        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"
    return text


def role_skills(role):
    defaults = {
        "Software Developer": ["python", "java", "sql", "git"],
        "Data Scientist": ["python", "sql", "machine learning", "pandas", "numpy"],
        "Machine Learning Engineer": ["python", "machine learning", "docker", "git"],
        "Web Developer": ["html", "css", "javascript", "react", "git"],
        "DevOps Engineer": ["docker", "git", "aws", "kubernetes", "python"],
    }
    return defaults.get(role, [])


def calculate_match(required, current):
    if not required:
        return 0, [], []
    matched = [s for s in required if s in current]
    missing = [s for s in required if s not in current]
    return int(len(matched) * 100 / len(required)), matched, missing


def current_skills():
    return sorted(set(st.session_state.resume_skills) | set(st.session_state.completed_course_skills))


def recommendations_for_gaps(missing):
    result = []
    for skill in missing:
        key = skill_course_mapping.get(skill)
        if key and key not in result:
            result.append(key)
    return result


def course_title(key):
    if key in course_content:
        return course_content[key].get("title", key.title())
    if key in courses:
        return courses[key].get("title", key.title())
    return key.title()


def course_icon(key):
    if key in course_content:
        return course_content[key].get("icon", "📚")
    if key in courses:
        return courses[key].get("icon", "📚")
    return "📚"


def detailed_course(key):
    return course_content.get(key)


def course_progress(key):
    course = detailed_course(key)
    if course:
        modules = course.get("modules", [])
        total = sum(len(m.get("topics", [])) for m in modules)
        done = len(st.session_state.course_progress.get(key, set()))
        return int(done * 100 / total) if total else 0
    if key in courses:
        total = len(courses[key].get("lessons", []))
        done = len(st.session_state.course_progress.get(key, set()))
        return int(done * 100 / total) if total else 0
    return 0


def video_url(video):
    if isinstance(video, str):
        return video.strip()
    if isinstance(video, dict):
        for k in ("url", "video_url", "link", "youtube_url"):
            value = video.get(k)
            if isinstance(value, str) and value.strip():
                return value.strip()
    return ""


def complete_course(key):
    st.session_state.completed_courses.add(key)
    for skill in course_skill_map.get(key, set()):
        st.session_state.completed_course_skills.add(skill)
    # Recalculate the current job gap immediately.
    required = st.session_state.required_skills
    percentage, matched, missing = calculate_match(required, current_skills())
    st.session_state.matched_skills = matched
    st.session_state.missing_skills = missing
    st.session_state.analysis_done = True


def read_job_skills(job_text, selected_role):
    extracted = extract_skills(job_text)
    if extracted:
        return extracted
    # If the pasted JD contains no recognized skill names, use the
    # selected role's standard skill set instead of producing a misleading 0-skill match.
    return role_skills(selected_role)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
<div class="hero">
<h1>🚀 SkillHackAI</h1>
<h3>AI Career Command Center</h3>
<p>Resume → Job Requirements → Skill Gaps → Recommended Courses → Course Completion → New Skills</p>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🧭 SkillHackAI")

pages = [
    "🏠 Overview",
    "📄 Resume Analysis",
    "🎯 Career Match",
    "🧠 My Skills",
    "🚨 Skill Gaps",
    "📚 Recommended Courses",
    "🗺️ Career Roadmap",
    "💻 Coding Profiles",
    "🔗 LinkedIn",
    "📊 Progress Dashboard",
    "🏆 Certificates",
]

page = st.sidebar.radio("Choose a feature", pages, index=pages.index(st.session_state.page) if st.session_state.page in pages else 0)
st.session_state.page = page

st.sidebar.divider()
if st.session_state.resume_uploaded:
    st.sidebar.success("📄 Resume uploaded")
else:
    st.sidebar.info("📄 Upload your resume first")

st.sidebar.metric("Current Skills", len(current_skills()))
st.sidebar.metric("Skill Gaps", len(st.session_state.missing_skills))
st.sidebar.metric("Completed Courses", len(st.session_state.completed_courses))

# ============================================================
# OVERVIEW
# ============================================================

# ============================================================
# CODING PROFILE DONUT CHARTS
# ============================================================

def coding_difficulty_donut(easy, medium, hard):
    values = [max(0, int(easy)), max(0, int(medium)), max(0, int(hard))]
    labels = ["Easy", "Medium", "Hard"]
    total = sum(values)
    if total <= 0:
        st.info("No solved-problem data available for the donut chart.")
        return

    easy_pct = values[0] / total * 100
    medium_pct = values[1] / total * 100
    gradient = (
        f"conic-gradient(#22c55e 0% {easy_pct:.2f}%, "
        f"#f59e0b {easy_pct:.2f}% {easy_pct + medium_pct:.2f}%, "
        f"#ef4444 {easy_pct + medium_pct:.2f}% 100%)"
    )

    st.markdown(f"""
    <div style="text-align:center;margin:18px 0 26px;">
        <h3 style="color:#172554;margin-bottom:18px;">LeetCode Difficulty Breakdown</h3>
        <div style="display:flex;justify-content:center;align-items:center;gap:42px;flex-wrap:wrap;">
            <div style="width:230px;height:230px;border-radius:50%;background:{gradient};display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(15,23,42,.12);">
                <div style="width:145px;height:145px;border-radius:50%;background:white;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:inset 0 0 12px rgba(15,23,42,.08);">
                    <div style="font-size:30px;font-weight:800;color:#172554;">{total}</div>
                    <div style="font-size:13px;color:#64748b;">Solved</div>
                </div>
            </div>
            <div style="text-align:left;min-width:190px;">
                <div style="margin:10px 0;font-weight:700;color:#172554;"><span style="color:#22c55e;font-size:20px;">●</span> Easy &nbsp; {values[0]}</div>
                <div style="margin:10px 0;font-weight:700;color:#172554;"><span style="color:#f59e0b;font-size:20px;">●</span> Medium &nbsp; {values[1]}</div>
                <div style="margin:10px 0;font-weight:700;color:#172554;"><span style="color:#ef4444;font-size:20px;">●</span> Hard &nbsp; {values[2]}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def coding_rating_donut(current, maximum):
    current = max(0, float(current))
    maximum = max(0, float(maximum))
    if maximum <= 0:
        st.info("No rating data available for the donut chart.")
        return

    shown_current = min(current, maximum)
    current_pct = shown_current / maximum * 100
    gradient = f"conic-gradient(#6366f1 0% {current_pct:.2f}%, #e5e7eb {current_pct:.2f}% 100%)"

    st.markdown(f"""
    <div style="text-align:center;margin:18px 0 26px;">
        <h3 style="color:#172554;margin-bottom:18px;">Codeforces Rating</h3>
        <div style="display:flex;justify-content:center;align-items:center;gap:35px;flex-wrap:wrap;">
            <div style="width:220px;height:220px;border-radius:50%;background:{gradient};display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(15,23,42,.12);">
                <div style="width:138px;height:138px;border-radius:50%;background:white;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:inset 0 0 12px rgba(15,23,42,.08);">
                    <div style="font-size:27px;font-weight:800;color:#172554;">{int(current):,}</div>
                    <div style="font-size:12px;color:#64748b;">Current Rating</div>
                </div>
            </div>
            <div style="text-align:left;min-width:170px;">
                <div style="font-size:14px;color:#64748b;">Maximum Rating</div>
                <div style="font-size:27px;font-weight:800;color:#172554;">{int(maximum):,}</div>
                <div style="font-size:13px;color:#6366f1;margin-top:6px;">{current_pct:.1f}% of maximum</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def coding_review_box(title, points):
    items = "".join(f"<li style=\"margin:7px 0;\">{p}</li>" for p in points)
    st.markdown(f"""
    <div style="margin:18px 0 24px;padding:20px 22px;border-radius:20px;
                background:linear-gradient(135deg,#eef2ff,#f5f3ff,#fdf2f8);
                border:1px solid #ddd6fe;box-shadow:0 6px 18px rgba(79,70,229,.07);">
        <h3 style="margin:0 0 10px;color:#172554;">🧠 {title}</h3>
        <ul style="margin:0;padding-left:22px;color:#334155;">{items}</ul>
    </div>
    """, unsafe_allow_html=True)


def leetcode_review(data):
    total = int(data.get("total_solved", data.get("total", 0)) or 0)
    easy = int(data.get("easy_solved", data.get("easy", 0)) or 0)
    medium = int(data.get("medium_solved", data.get("medium", 0)) or 0)
    hard = int(data.get("hard_solved", data.get("hard", 0)) or 0)
    points = [f"Problems solved: <b>{total}</b> (Easy {easy}, Medium {medium}, Hard {hard})."]
    if total:
        if hard > 0:
            points.append("Your profile includes Hard-level problem solving, in addition to Easy and Medium practice.")
        elif medium > 0:
            points.append("Your profile includes Medium-level practice; adding more Hard-level problems can broaden difficulty coverage.")
        else:
            points.append("Your current solved set is concentrated at the Easy level; progressing into Medium problems can broaden difficulty coverage.")
    else:
        points.append("No solved-problem count was returned for this profile yet.")
    coding_review_box("LeetCode Profile Review", points)


def codeforces_review(data):
    rating = int(data.get("rating", 0) or 0)
    maximum = int(data.get("max_rating", 0) or 0)
    solved = int(data.get("total_solved", 0) or 0)
    points = [f"Current rating: <b>{rating:,}</b> | Maximum rating: <b>{maximum:,}</b>."]
    if solved:
        points.append(f"Problems solved: <b>{solved:,}</b>.")
    if maximum and rating:
        points.append(f"Current rating is {rating / maximum * 100:.1f}% of the recorded maximum rating.")
    points.append("Use contest participation and regular problem practice to continue building the profile.")
    coding_review_box("Codeforces Profile Review", points)


def codechef_review(data):
    rating = int(data.get("rating", 0) or 0)
    highest = int(data.get("highest_rating", 0) or 0)
    solved = int(data.get("problems_solved", 0) or 0)
    points = [f"Current rating: <b>{rating:,}</b> | Highest rating: <b>{highest:,}</b>."]
    points.append(f"Problems solved: <b>{solved:,}</b>.")
    if highest and rating:
        points.append(f"Current rating is {rating / highest * 100:.1f}% of the recorded highest rating.")
    points.append("Regular contest participation and problem solving can help strengthen the profile further.")
    coding_review_box("CodeChef Profile Review", points)


def codechef_donut(rating, highest_rating, solved):
    rating = max(0, int(rating))
    highest_rating = max(0, int(highest_rating))
    solved = max(0, int(solved))
    if highest_rating <= 0 and solved <= 0:
        return

    rating_pct = min(rating / highest_rating * 100, 100) if highest_rating else 0
    gradient = f"conic-gradient(#10b981 0% {rating_pct:.2f}%, #e5e7eb {rating_pct:.2f}% 100%)"

    st.markdown(f"""
    <div style="text-align:center;margin:18px 0 26px;">
        <h3 style="color:#172554;margin-bottom:18px;">CodeChef Rating</h3>
        <div style="display:flex;justify-content:center;align-items:center;gap:35px;flex-wrap:wrap;">
            <div style="width:220px;height:220px;border-radius:50%;background:{gradient};display:flex;align-items:center;justify-content:center;box-shadow:0 8px 24px rgba(15,23,42,.12);">
                <div style="width:138px;height:138px;border-radius:50%;background:white;display:flex;flex-direction:column;align-items:center;justify-content:center;box-shadow:inset 0 0 12px rgba(15,23,42,.08);">
                    <div style="font-size:27px;font-weight:800;color:#172554;">{rating:,}</div>
                    <div style="font-size:12px;color:#64748b;">Current Rating</div>
                </div>
            </div>
            <div style="text-align:left;min-width:170px;">
                <div style="font-size:14px;color:#64748b;">Highest Rating</div>
                <div style="font-size:24px;font-weight:800;color:#172554;">{highest_rating:,}</div>
                <div style="font-size:14px;color:#64748b;margin-top:8px;">Problems Solved</div>
                <div style="font-size:24px;font-weight:800;color:#10b981;">{solved:,}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


if page == "🏠 Overview":
    st.header("🏠 AI Career Command Center")
    st.write("Start with your resume. SkillHackAI will personalize the learning path for your target job.")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Resume", "Ready" if st.session_state.resume_uploaded else "Not uploaded")
    with c2:
        st.metric("Current Skills", len(current_skills()))
    with c3:
        st.metric("Skill Gaps", len(st.session_state.missing_skills))
    with c4:
        st.metric("Courses Completed", len(st.session_state.completed_courses))

    st.markdown("### 🔄 How SkillHackAI works")
    steps = [
        ("1", "📄", "Upload Resume", "Extract your existing skills."),
        ("2", "💼", "Add Job Description", "Find the skills required for the job."),
        ("3", "🚨", "Identify Skill Gaps", "Compare required skills with your current skills."),
        ("4", "📚", "Recommended Courses", "Show only courses for your missing skills."),
        ("5", "🎥", "Learn & Practice", "Complete lessons, videos and quizzes."),
        ("6", "🏆", "Complete Course", "Pass the final assessment and earn a certificate."),
        ("7", "➕", "Skill Added", "The completed course skill becomes part of your current skills."),
    ]
    for n, icon, title, desc in steps:
        st.markdown(f"**{n}. {icon} {title}** — {desc}")

    if not st.session_state.resume_uploaded:
        st.info("👉 Go to **Resume Analysis** and upload your PDF or DOCX resume to begin.")
    elif not st.session_state.analysis_done:
        st.info("👉 Your resume is ready. Go to **Career Match** and enter the Job Description.")
    else:
        st.success("✅ Your personalized career learning path is ready. Open **Skill Gaps** or **Recommended Courses**.")

# ============================================================
# RESUME ANALYSIS
# ============================================================

elif page == "📄 Resume Analysis":
    st.header("📄 Resume Analysis")
    st.write("Upload your resume. Your detected skills become the starting point for personalization.")

    uploaded = st.file_uploader("Upload Resume", type=["pdf", "docx"], key="resume_upload")

    if uploaded is not None:
        try:
            text = load_resume(uploaded)
            skills = extract_skills(text)
            st.session_state.resume_text = text
            st.session_state.resume_skills = skills
            st.session_state.resume_uploaded = True
            st.session_state.analysis_done = False
            st.session_state.required_skills = []
            st.session_state.matched_skills = []
            st.session_state.missing_skills = []
            st.success("✅ Resume uploaded and analyzed.")
        except Exception as error:
            st.error(f"Resume processing error: {error}")

    if st.session_state.resume_uploaded:
        st.divider()
        st.subheader("🧠 Skills detected from your resume")
        skills = st.session_state.resume_skills
        if skills:
            cols = st.columns(min(4, len(skills)))
            for i, skill in enumerate(skills):
                with cols[i % len(cols)]:
                    st.markdown(f'<div class="skill-card">💡 <b>{skill.title()}</b></div>', unsafe_allow_html=True)
        else:
            st.warning("No supported skills were detected yet.")

# ============================================================
# CAREER MATCH
# ============================================================

elif page == "🎯 Career Match":
    st.header("🎯 Resume vs Job Description")

    if not st.session_state.resume_uploaded:
        st.warning("📄 Please upload your resume first.")
        st.info("Go to **Resume Analysis** → upload your PDF/DOCX → come back here.")
        st.stop()

    st.success(f"Resume skills loaded: {', '.join(s.title() for s in st.session_state.resume_skills) or 'None detected'}")

    role = st.selectbox(
        "Target Role",
        ["Software Developer", "Data Scientist", "Machine Learning Engineer", "Web Developer", "DevOps Engineer"],
        index=["Software Developer", "Data Scientist", "Machine Learning Engineer", "Web Developer", "DevOps Engineer"].index(st.session_state.target_role),
    )
    st.session_state.target_role = role

    jd = st.text_area(
        "💼 Paste the Job Description",
        value=st.session_state.job_description,
        height=220,
        placeholder="Paste the complete job description here...",
    )

    if st.button("🔍 Analyze Job & Find Skill Gaps", type="primary"):
        st.session_state.job_description = jd
        required = read_job_skills(jd, role)
        percentage, matched, missing = calculate_match(required, current_skills())
        st.session_state.required_skills = required
        st.session_state.matched_skills = matched
        st.session_state.missing_skills = missing
        st.session_state.analysis_done = True
        st.success("✅ Job analysis completed.")
        st.rerun()

    if st.session_state.analysis_done:
        required = st.session_state.required_skills
        matched = st.session_state.matched_skills
        missing = st.session_state.missing_skills
        percentage = int(len(matched) * 100 / len(required)) if required else 0

        st.divider()
        c1, c2, c3 = st.columns(3)
        with c1: st.metric("Job Match", f"{percentage}%")
        with c2: st.metric("Matched Skills", len(matched))
        with c3: st.metric("Skill Gaps", len(missing))

        st.subheader("✅ Skills you already have")
        st.write(", ".join(s.title() for s in matched) if matched else "None")

        st.subheader("🚨 Skills you still need")
        if missing:
            for skill in missing:
                st.markdown(f'<div class="gap-card">❌ <b>{skill.title()}</b> — learning required for this job</div>', unsafe_allow_html=True)
        else:
            st.success("🎉 No remaining skill gaps for this job based on the detected skills.")

# ============================================================
# MY SKILLS
# ============================================================

elif page == "🧠 My Skills":
    st.header("🧠 My Skills")
    if not st.session_state.resume_uploaded:
        st.info("Upload your resume first. Your current skills will appear here.")
    else:
        skills = current_skills()
        st.write("Your skills include both resume-detected skills and skills earned by completing SkillHackAI courses.")
        if skills:
            cols = st.columns(min(4, len(skills)))
            for i, skill in enumerate(skills):
                source = "Resume" if skill in st.session_state.resume_skills else "Course Completed"
                with cols[i % len(cols)]:
                    st.markdown(f'<div class="skill-card"><b>✅ {skill.title()}</b><br><span class="small-muted">{source}</span></div>', unsafe_allow_html=True)
        else:
            st.info("No skills detected yet.")

# ============================================================
# SKILL GAPS
# ============================================================

elif page == "🚨 Skill Gaps":
    st.header("🚨 Skill Gaps")
    if not st.session_state.resume_uploaded:
        st.info("Upload your resume first.")
    elif not st.session_state.analysis_done:
        st.info("Add a Job Description in **Career Match** first.")
    elif not st.session_state.missing_skills:
        st.success("🎉 You currently have no detected skill gaps for this job.")
    else:
        st.write("These are the skills required by the selected job that are not yet in your current skill set.")
        for skill in st.session_state.missing_skills:
            st.markdown(f'<div class="gap-card">🚨 <b>{skill.title()}</b></div>', unsafe_allow_html=True)
        st.info("Only these missing skills are used to generate your Recommended Courses.")

# ============================================================
# RECOMMENDED COURSES
# ============================================================

elif page == "📚 Recommended Courses":
    st.header("📚 Recommended Courses")

    if not st.session_state.resume_uploaded:
        st.info("📄 Upload your resume first. Recommended Courses will appear only after resume analysis.")
    elif not st.session_state.analysis_done:
        st.info("🎯 Analyze a Job Description first. Courses are personalized from the resulting skill gaps.")
    else:
        missing = st.session_state.missing_skills
        recommended = recommendations_for_gaps(missing)

        if not missing:
            st.success("🎉 No courses are required for the current job because no skill gaps remain.")
        elif not recommended:
            st.warning("No in-app course is currently mapped to these missing skills.")
            st.write("Missing skills:", ", ".join(s.title() for s in missing))
        else:
            st.success(f"🎯 {len(recommended)} personalized course(s) based only on your current skill gaps.")
            for key in recommended:
                if key in st.session_state.completed_courses:
                    continue
                title = course_title(key)
                icon = course_icon(key)
                progress = course_progress(key)
                skills_added = ", ".join(s.title() for s in sorted(course_skill_map.get(key, set())))
                st.markdown(
                    f"""
                    <div class="course-card">
                    <h2>{icon} {title}</h2>
                    <p>🎯 Skills addressed: <b>{skills_added}</b></p>
                    <p>📈 Progress: <b>{progress}%</b></p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                st.progress(progress / 100)
                if st.button(f"🎥 Open Full Course — {title}", key=f"recommended_{key}"):
                    st.session_state.selected_course = key
                    st.rerun()

        # Show completed courses only as history inside the same Recommended Courses page.
        completed_here = [k for k in st.session_state.completed_courses if k in course_content or k in courses]
        if completed_here:
            st.divider()
            st.subheader("🏆 Completed Learning")
            st.write("Completed courses are no longer recommended for the same skills, because those skills are now added to My Skills.")
            for key in completed_here:
                st.success(f"✅ {course_icon(key)} {course_title(key)} — Completed")

        selected = st.session_state.selected_course
        if selected and selected in recommended:
            st.divider()
            st.header(f"🎓 {course_title(selected)}")
            if selected in course_content:
                course = course_content[selected]
                modules = course.get("modules", [])
                total_topics = sum(len(m.get("topics", [])) for m in modules)
                done = st.session_state.course_progress.setdefault(selected, set())
                progress = int(len(done) * 100 / total_topics) if total_topics else 0

                a, b, c = st.columns(3)
                with a: st.metric("Modules", len(modules))
                with b: st.metric("Topics", total_topics)
                with c: st.metric("Progress", f"{progress}%")
                st.progress(progress / 100, text=f"Course Progress: {progress}%")

                for mi, module in enumerate(modules):
                    st.subheader(f"📘 Module {mi + 1}: {module.get('title', 'Module')}")
                    for ti, topic in enumerate(module.get("topics", [])):
                        tid = f"{mi}_{ti}"
                        done_topic = tid in done
                        with st.expander(f"{'✅' if done_topic else '📖'} {topic.get('title', 'Topic')}", expanded=(mi == 0 and ti == 0)):
                            st.markdown("### 📖 Learn")
                            st.markdown(topic.get("content", ""))
                            if topic.get("example"):
                                st.markdown("### 💻 Example")
                                st.code(topic["example"], language="python")

                            st.markdown("### 🎬 Video")
                            url = video_url(topic.get("video", ""))
                            if url:
                                try:
                                    st.video(url)
                                except Exception:
                                    st.link_button("▶️ Open Course Video", url)
                            else:
                                st.info("No valid video URL is available for this topic yet.")

                            practice = topic.get("practice", [])
                            if practice:
                                st.markdown("### 🧩 Practice")
                                for n, q in enumerate(practice, 1):
                                    st.write(f"**{n}. {q}**")

                            quiz = topic.get("quiz", [])
                            if quiz:
                                st.markdown("### 📝 Topic Quiz")
                                answers = []
                                for qi, q in enumerate(quiz):
                                    answers.append(st.radio(q["question"], q["options"], key=f"rec_{selected}_{tid}_{qi}"))
                                if st.button("Submit Topic Quiz", key=f"submit_rec_{selected}_{tid}"):
                                    score = sum(answers[i] == q["answer"] for i, q in enumerate(quiz))
                                    pct = int(score * 100 / len(quiz))
                                    st.session_state.topic_scores[f"{selected}_{tid}"] = pct
                                    if pct >= 70:
                                        done.add(tid)
                                        st.session_state.course_progress[selected] = done
                                        st.success(f"🎉 Passed: {score}/{len(quiz)} ({pct}%)")
                                        st.rerun()
                                    else:
                                        st.warning(f"Score: {score}/{len(quiz)} ({pct}%). You need 70% to pass.")

                st.divider()
                st.header("🏆 Final Assessment")
                final_quiz = course.get("final_assessment", course.get("final_quiz", []))
                if len(done) < total_topics:
                    st.warning("🔒 Complete every topic quiz before attempting the final assessment.")
                elif final_quiz:
                    final_answers = []
                    for qi, q in enumerate(final_quiz):
                        final_answers.append(st.radio(q["question"], q["options"], key=f"rec_final_{selected}_{qi}"))
                    if st.button("🏆 Submit Final Assessment", key=f"rec_final_submit_{selected}"):
                        score = sum(final_answers[i] == q["answer"] for i, q in enumerate(final_quiz))
                        pct = int(score * 100 / len(final_quiz))
                        st.session_state.final_scores[selected] = pct
                        if pct >= course.get("passing_score", 70):
                            complete_course(selected)
                            st.success(f"🎓 Course Completed! Final Score: {pct}%")
                            st.balloons()
                            st.session_state.selected_course = None
                            st.rerun()
                        else:
                            st.warning(f"Final Score: {pct}%. You need {course.get('passing_score', 70)}% to complete the course.")
            else:
                # Legacy course fallback. Still appears only when recommended.
                old = courses.get(selected)
                if old:
                    total = len(old.get("lessons", []))
                    done = st.session_state.course_progress.setdefault(selected, set())
                    for i, lesson in enumerate(old.get("lessons", [])):
                        with st.expander(f"Lesson {i + 1}: {lesson.get('title', 'Lesson')}", expanded=i == 0):
                            st.markdown(lesson.get("content", ""))
                            if lesson.get("video"):
                                url = video_url(lesson.get("video"))
                                if url:
                                    try: st.video(url)
                                    except Exception: st.link_button("▶️ Open Course Video", url)
                            if st.button("Mark Lesson Complete", key=f"legacy_{selected}_{i}"):
                                done.add(i)
                                st.session_state.course_progress[selected] = done
                                st.rerun()
                    if len(done) == total and total:
                        if st.button("🏆 Complete Course", key=f"legacy_complete_{selected}"):
                            st.session_state.final_scores[selected] = 100
                            complete_course(selected)
                            st.success("🎓 Course completed and skill added!")
                            st.session_state.selected_course = None
                            st.rerun()

# ============================================================
# CAREER ROADMAP
# ============================================================

elif page == "🗺️ Career Roadmap":
    st.header("🗺️ Personalized Career Roadmap")
    if not st.session_state.resume_uploaded:
        st.info("Upload your resume first.")
    else:
        roadmap = [
            ("📄", "Upload & Analyze Resume", st.session_state.resume_uploaded),
            ("🧠", "Extract Current Skills", bool(st.session_state.resume_skills)),
            ("💼", "Analyze Target Job", st.session_state.analysis_done),
            ("🚨", "Identify Skill Gaps", bool(st.session_state.missing_skills)),
            ("📚", "Complete Recommended Courses", bool(st.session_state.completed_courses)),
            ("💻", "Improve Coding Profiles", False),
            ("🚀", "Prepare for Target Career", False),
        ]
        for i, (icon, title, done) in enumerate(roadmap, 1):
            status = "✅" if done else "⬜"
            st.markdown(f"### {status} Step {i}: {icon} {title}")

# ============================================================
# CODING PROFILES
# ============================================================

elif page == "💻 Coding Profiles":
    st.header("💻 Coding Profile Analyzer")
    st.write("Analyze your LeetCode, Codeforces and CodeChef profiles.")

    st.divider()
    st.subheader("🟡 LeetCode")
    leetcode_username = st.text_input("LeetCode Username", key="leetcode_username")
    if st.button("🔍 Analyze LeetCode", key="leetcode_button"):
        if leetcode_username.strip():
            with st.spinner("Fetching LeetCode profile..."):
                try:
                    data = get_leetcode_profile(leetcode_username.strip())
                    if data:
                        st.success("LeetCode profile loaded!")
                        c1, c2, c3, c4 = st.columns(4)
                        with c1: st.metric("Problems Solved", data.get("total_solved", 0))
                        with c2: st.metric("Ranking", data.get("ranking", 0))
                        with c3: st.metric("Reputation", data.get("reputation", 0))
                        with c4: st.metric("Contest Rating", data.get("contest_rating", 0))
                        coding_difficulty_donut(
                            data.get("easy_solved", 0),
                            data.get("medium_solved", 0),
                            data.get("hard_solved", 0),
                        )
                        leetcode_review(data)
                        languages = data.get("languages", [])
                        if languages: st.write("💻 Languages:", ", ".join(languages))
                    else: st.warning("Unable to retrieve LeetCode data.")
                except Exception as e: st.error(f"LeetCode error: {e}")
        else: st.warning("Please enter your LeetCode username.")

    st.divider()
    st.subheader("🔵 Codeforces")
    cf_username = st.text_input("Codeforces Username", key="codeforces_username")
    if st.button("🔍 Analyze Codeforces", key="codeforces_button"):
        if cf_username.strip():
            with st.spinner("Fetching Codeforces profile..."):
                try:
                    data = get_codeforces_profile(cf_username.strip())
                    if data:
                        st.success("Codeforces profile loaded!")
                        c1,c2,c3,c4,c5 = st.columns(5)
                        with c1: st.metric("Current Rating", data.get("rating",0))
                        with c2: st.metric("Maximum Rating", data.get("max_rating",0))
                        with c3: st.metric("Current Rank", data.get("rank","N/A"))
                        with c4: st.metric("Maximum Rank", data.get("max_rank","N/A"))
                        with c5: st.metric("Problems Solved", data.get("total_solved",0))
                        coding_rating_donut(
                            data.get("rating", 0),
                            data.get("max_rating", 0),
                        )
                        codeforces_review(data)
                    else: st.warning("Unable to retrieve Codeforces data.")
                except Exception as e: st.error(f"Codeforces error: {e}")
        else: st.warning("Please enter your Codeforces username.")

    st.divider()
    st.subheader("🟢 CodeChef")
    cc_username = st.text_input("CodeChef Username", key="codechef_username")
    if st.button("🔍 Analyze CodeChef", key="codechef_button"):
        if cc_username.strip():
            with st.spinner("Fetching CodeChef profile..."):
                try:
                    data = get_codechef_profile(cc_username.strip())
                    if data:
                        st.success("CodeChef profile loaded!")
                        c1,c2,c3,c4 = st.columns(4)
                        with c1: st.metric("Rating", data.get("rating",0))
                        with c2: st.metric("Highest Rating", data.get("highest_rating",0))
                        with c3: st.metric("Stars", data.get("stars","N/A"))
                        with c4: st.metric("Problems Solved", data.get("problems_solved",0))
                        codechef_donut(
                            data.get("rating", 0),
                            data.get("highest_rating", 0),
                            data.get("problems_solved", 0),
                        )
                        codechef_review(data)
                    else: st.warning("Unable to retrieve CodeChef data.")
                except Exception as e: st.error(f"CodeChef error: {e}")
        else: st.warning("Please enter your CodeChef username.")

# ============================================================
# LINKEDIN
# ============================================================

elif page == "🔗 LinkedIn":
    st.header("🔗 LinkedIn Career Profile")
    st.write("Add your LinkedIn profile URL so it stays connected to your SkillHackAI career workspace.")
    linkedin = st.text_input("LinkedIn Profile URL", placeholder="https://www.linkedin.com/in/your-name")
    if linkedin.strip():
        if "linkedin.com/in/" in linkedin.lower():
            st.success("✅ LinkedIn profile URL added for your career workspace.")
            st.link_button("🔗 Open My LinkedIn Profile", linkedin.strip())

            st.divider()
            st.subheader("🧠 LinkedIn Career Review")
            review_points = []
            if st.session_state.resume_uploaded:
                review_points.append(f"Your resume currently contributes <b>{len(st.session_state.resume_skills)}</b> detected skill(s) to your career profile.")
            else:
                review_points.append("Upload your resume so SkillHackAI can compare your LinkedIn profile with your detected skills.")

            if st.session_state.target_role:
                review_points.append(f"Target role: <b>{st.session_state.target_role}</b>. Keep your LinkedIn headline and About section aligned with this role.")

            if st.session_state.analysis_done:
                review_points.append(f"Your current job analysis has <b>{len(st.session_state.matched_skills)}</b> matched skill(s) and <b>{len(st.session_state.missing_skills)}</b> remaining skill gap(s).")
                if st.session_state.missing_skills:
                    review_points.append("Consider adding verified skills to LinkedIn only after you have genuinely learned or demonstrated them.")
                else:
                    review_points.append("Your current detected skills cover the analyzed job requirements; keep your LinkedIn skills consistent with your actual experience.")

            if st.session_state.completed_courses:
                review_points.append(f"You have completed <b>{len(st.session_state.completed_courses)}</b> SkillHackAI course(s). Add relevant completed courses, projects, and certificates to LinkedIn.")
            else:
                review_points.append("Add relevant projects, certifications, and completed learning achievements to strengthen the profile with evidence.")

            review_points.append("Keep your headline, About section, skills, projects, and experience consistent with the work shown in your resume.")
            coding_review_box("LinkedIn Profile Review", review_points)
        else:
            st.warning("Please enter a valid LinkedIn profile URL.")

# ============================================================
# PROGRESS DASHBOARD
# ============================================================

elif page == "📊 Progress Dashboard":
    st.header("📊 Progress Dashboard")
    completed = list(st.session_state.completed_courses)
    gaps = st.session_state.missing_skills
    skills = current_skills()

    c1,c2,c3,c4 = st.columns(4)
    with c1: st.metric("Current Skills", len(skills))
    with c2: st.metric("Remaining Gaps", len(gaps))
    with c3: st.metric("Courses Completed", len(completed))
    with c4: st.metric("Target Job Match", f"{int(len(st.session_state.matched_skills)*100/len(st.session_state.required_skills)) if st.session_state.required_skills else 0}%")

    st.subheader("📚 Course Progress")
    progress_rows = []
    for key in set(list(st.session_state.course_progress.keys()) + completed):
        progress_rows.append({"Course": course_title(key), "Progress": course_progress(key)})
    if progress_rows:
        df = pd.DataFrame(progress_rows).sort_values("Progress", ascending=False)
        for _, row in df.iterrows():
            st.write(f"**{row['Course']}** — {int(row['Progress'])}%")
            st.progress(int(row["Progress"]) / 100)
    else:
        st.info("No course progress yet. Start a Recommended Course.")

# ============================================================
# CERTIFICATES
# ============================================================

elif page == "🏆 Certificates":
    st.header("🏆 Certificates & Achievements")
    if not st.session_state.completed_courses:
        st.info("Complete a Recommended Course and pass its final assessment to earn a certificate.")
    else:
        for key in sorted(st.session_state.completed_courses):
            score = st.session_state.final_scores.get(key, 0)
            st.markdown(
                f"""
                <div class="success-box">
                    <h2>🏅 SkillHackAI Certificate</h2>
                    <p><b>{course_title(key)}</b></p>
                    <p>Final Assessment Score: <b>{score}%</b></p>
                    <span class="badge">SkillHackAI Certified</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

# ============================================================
# FOOTER
# ============================================================

st.divider()
st.caption("SkillHackAI • Resume-driven personalized learning • Complete a missing-skill course and it becomes part of your current skill set.")
