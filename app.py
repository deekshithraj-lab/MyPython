
"""
app.py
Main application for PyLearn: Learn Python interactively.
Run using: python -m streamlit run app.py
"""

import streamlit as st

from lessons import LESSONS
from quiz import QUIZZES


# -------------------- Page Configuration --------------------

st.set_page_config(
    page_title="MyPython - Learn Python",
    page_icon="🐍",
    layout="wide",
)

# -------------------- Professional Dark Theme --------------------

st.markdown("""
<style>

/* Main application background */
.stApp {
    background:
        radial-gradient(
            circle at 80% 10%,
            rgba(48, 70, 130, 0.20),
            transparent 35%
        ),
        linear-gradient(135deg, #10172b, #111b32 60%, #101629);
    color: #f1f5f9;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

/* Sidebar gradient */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #344b91 0%,
        #243765 40%,
        #102d38 100%
    );
    border-right: 1px solid rgba(255,255,255,0.10);
}

section[data-testid="stSidebar"] * {
    color: #f1f5f9;
}

/* Sidebar navigation */
section[data-testid="stSidebar"] [data-testid="stRadio"] label {
    padding: 7px 10px;
    border-radius: 9px;
    transition: background 0.2s ease;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    background: rgba(255,255,255,0.10);
}

/* Main headings */
h1, h2, h3 {
    color: #f8fafc !important;
    font-weight: 750 !important;
    letter-spacing: -0.4px;
}

h1 {
    font-size: 2.5rem !important;
}

h2 {
    color: #f5d78e !important;
}

/* Paragraphs and normal text */
.stMarkdown, .stText, p, li {
    color: #e2e8f0;
}

/* Dashboard metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(
        135deg,
        rgba(21, 75, 75, 0.95),
        rgba(35, 53, 91, 0.96)
    );
    border: 1px solid rgba(110, 231, 183, 0.22);
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.18);
}

div[data-testid="stMetricLabel"] {
    color: #dbeafe !important;
}

div[data-testid="stMetricValue"] {
    color: #f5e7b7 !important;
    font-weight: 800;
}

/* Progress bars */
div[data-testid="stProgressBar"] > div {
    background-color: #29364f;
    border-radius: 20px;
}

div[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(
        90deg,
        #10b981,
        #34d399,
        #f5d06f
    );
    border-radius: 20px;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    border: 1px solid rgba(110,231,183,0.35);
    border-radius: 10px;
    padding: 0.55rem 1rem;
    font-weight: 650;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #34d399, #10b981);
    color: #071b19;
    border-color: #6ee7b7;
    box-shadow: 0 0 18px rgba(16,185,129,0.25);
}

/* Select boxes and input fields */
div[data-baseweb="select"] > div,
.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background-color: #18243b !important;
    color: #f8fafc !important;
    border: 1px solid #344765 !important;
    border-radius: 9px !important;
}

/* Code blocks */
div[data-testid="stCode"] {
    border: 1px solid #334155;
    border-radius: 12px;
    overflow: hidden;
}

div[data-testid="stCode"] pre {
    background: #0b1422;
    color: #a7f3d0;
}

/* Expanders */
div[data-testid="stExpander"] {
    background: rgba(30, 41, 59, 0.65);
    border: 1px solid #334155;
    border-radius: 12px;
}

/* Horizontal dividers */
hr {
    border-color: rgba(148,163,184,0.22);
}

/* Info and success messages */
div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Footer text */
small, .stCaption {
    color: #a7b4cc !important;
}

</style>
""", unsafe_allow_html=True)


# -------------------- Session State --------------------

# Keep progress while the app session is active.
if "completed_lessons" not in st.session_state:
    st.session_state.completed_lessons = set()

if "quiz_results" not in st.session_state:
    st.session_state.quiz_results = {}

if "quiz_feedback" not in st.session_state:
    st.session_state.quiz_feedback = {}


# -------------------- Sidebar Navigation --------------------

st.sidebar.markdown("""
<div style="padding: 12px 0 18px 0;">
    <div style="font-size: 30px; font-weight: 800;">
        🐍 MyPython
    </div>
    <div style="font-size: 13px; color: #dbeafe;">
        Your Python learning studio
    </div>
</div>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
    "Navigate",
    ["Home", "Lessons", "Quizzes", "Progress"],
)

st.sidebar.divider()
st.sidebar.write(
    f"Lessons completed: "
    f"{len(st.session_state.completed_lessons)}/{len(LESSONS)}"
)


# -------------------- Home Page --------------------


if page == "Home":

    st.markdown("""
    <div style="
        padding: 28px 30px;
        border-radius: 20px;
        background: linear-gradient(115deg, #111c36, #172849 65%, #20345c);
        border: 1px solid rgba(110, 231, 183, 0.22);
        box-shadow: 0 8px 30px rgba(0,0,0,0.20);
        margin-bottom: 22px;
    ">
        <h1 style="color: #f8fafc; font-size: 38px; margin: 0;">
            🐍 Welcome to Mypython!
        </h1>
        <h3 style="color: #f5d78e; margin-top: 12px; margin-bottom: 10px;">
            Learn Python one step at a time.
        </h3>
        <p style="color: #dbeafe; font-size: 16px; margin-bottom: 0;">
            Learn Python from scratch with interactive lessons,
            practical code examples, quizzes, and progress tracking.
        </p>
    </div>
    """, unsafe_allow_html=True)



    st.write(
        "MyPython helps beginners understand Python through "
        "simple lessons, code examples, and interactive quizzes."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Available Lessons", len(LESSONS))

    with col2:
        st.metric("Quiz Topics", len(QUIZZES))

    with col3:
        st.metric(
            "Lessons Completed",
            len(st.session_state.completed_lessons),
        )

    st.progress(
        len(st.session_state.completed_lessons) / len(LESSONS),
        text="Overall lesson completion",
    )

    st.markdown("## 🗺️ Your Learning Roadmap")

    roadmap = [
        (
            "🟢",
            "Level 1 · Python Fundamentals",
            "Variables · Data Types · Operators · Strings · Input"
        ),
        (
            "🔵",
            "Level 2 · Control Flow",
            "If Statements · For Loops · While Loops"
        ),
        (
            "🟣",
            "Level 3 · Collections and Functions",
            "Lists · Tuples · Sets · Dictionaries · Functions"
        ),
        (
            "🟡",
            "Level 4 · Object-Oriented Python",
            "Classes · Objects · Encapsulation · Inheritance · Polymorphism"
        ),
        (
            "🟠",
            "Level 5 · Practical Python",
            "Modules · Exceptions · File Handling · Mini Projects"
        ),
    ]

    for icon, title, topics in roadmap:
        st.markdown(
            f"""
            <div style="
                background: linear-gradient(110deg, #1e2e4c, #1a2641);
                border: 1px solid rgba(148, 163, 184, 0.22);
                border-left: 4px solid #34d399;
                border-radius: 12px;
                padding: 16px 20px;
                margin: 10px 0;
            ">
                <div style="
                    color: #f5d78e;
                    font-size: 17px;
                    font-weight: 750;
                ">{icon} {title}</div>
                <div style="
                    color: #dbeafe;
                    margin-top: 7px;
                    font-size: 14px;
                ">{topics}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


elif page == "Lessons":
    st.title("📚 Python Lessons")
    st.write("Choose a topic and learn with an example.")

    # Get the title of every lesson.
    lesson_titles = [lesson.title for lesson in LESSONS]

    # Let the user select a lesson.
    selected_title = st.selectbox(
        "Choose a lesson",
        lesson_titles,
    )

    # Find the selected lesson object.
    lesson = next(
        item for item in LESSONS
        if item.title == selected_title
    )

    # Display the lesson.
    st.header(lesson.title)
    st.write(lesson.explanation)

    st.markdown("### Example Code")
    st.code(lesson.example, language="python")

    st.markdown("### Expected Output")
    st.code(lesson.output, language="text")

    # Show completion status.
    if selected_title in st.session_state.completed_lessons:
        st.success("You have completed this lesson!")

    # Mark the lesson as completed.
    if st.button(
        "Mark Lesson as Complete",
        key=f"complete_{selected_title}",
    ):
        st.session_state.completed_lessons.add(selected_title)
        st.success("Lesson marked as complete!")
        st.rerun()


# -------------------- Quizzes Page --------------------

elif page == "Quizzes":
    st.title("🧠 Python Quizzes")
    st.write("Test what you have learned.")

    topic = st.selectbox(
        "Choose a quiz topic",
        list(QUIZZES.keys()),
    )

    quiz = QUIZZES[topic]

    st.header(quiz.title)

    # Collect all answers inside a form.
    with st.form(key=f"form_{topic}"):
        for index, question in enumerate(quiz.questions):
            st.markdown(
                f"**Question {index + 1}: {question.prompt}**"
            )

            st.radio(
                "Select your answer",
                question.options,
                index=None,
                key=f"answer_{topic}_{index}",
            )

        submitted = st.form_submit_button("Submit Quiz")

    # Evaluate the quiz after submission.
    if submitted:
        answers = {
            index: st.session_state.get(
                f"answer_{topic}_{index}"
            ) or ""
            for index in range(len(quiz.questions))
        }

        score, feedback = quiz.evaluate(answers)

        st.session_state.quiz_results[topic] = {
            "score": score,
            "total": len(quiz.questions),
        }

        st.session_state.quiz_feedback[topic] = feedback

    # Display the latest saved result for this topic.
    if topic in st.session_state.quiz_results:
        result = st.session_state.quiz_results[topic]

        st.divider()
        st.subheader("Your Results")

        st.metric(
            "Score",
            f"{result['score']} / {result['total']}",
        )

        percentage = (
            result["score"] / result["total"] * 100
            if result["total"] else 0
        )

        st.progress(
            int(percentage),
            text=f"{percentage:.0f}% correct",
        )

        if percentage == 100:
            st.success("Excellent! All answers are correct.")
        elif percentage >= 50:
            st.info("Good effort! Review any incorrect answers.")
        else:
            st.warning("Keep practising. You can improve!")

        for index, item in enumerate(
            st.session_state.quiz_feedback[topic]
        ):
            st.markdown(
                f"**Question {index + 1}: {item['question']}**"
            )

            if item["correct"]:
                st.success(f"Correct: {item['selected']}")
            else:
                st.error(
                    f"Your answer: {item['selected']}"
                )
                st.write(
                    f"Correct answer: {item['correct_answer']}"
                )

            st.caption(item["explanation"])
# -------------------- Progress Page --------------------

elif page == "Progress":
    st.title("📊 Your Learning Progress")

    completed = len(st.session_state.completed_lessons)
    total_lessons = len(LESSONS)

    st.metric(
        "Lessons Completed",
        f"{completed} / {total_lessons}",
    )

    st.progress(
        completed / total_lessons,
        text="Lesson completion",
    )

    st.subheader("Lesson Checklist")

    for lesson in LESSONS:
        is_completed = (
            lesson.title in st.session_state.completed_lessons
        )

        if is_completed:
            st.success(f"✅ {lesson.title}")
        else:
            st.write(f"⬜ {lesson.title}")

    st.divider()
    st.subheader("Quiz Score Summary")

    if st.session_state.quiz_results:
        total_scored = 0
        total_questions = 0

        for topic, result in st.session_state.quiz_results.items():
            st.write(
                f"**{topic}:** "
                f"{result['score']} / {result['total']}"
            )
            total_scored += result["score"]
            total_questions += result["total"]

        if total_questions:
            overall = total_scored / total_questions * 100

            st.metric("Overall Quiz Accuracy", f"{overall:.0f}%")
    else:
        st.info("Complete a quiz to see your scores here.")

    st.caption(
        "Progress is stored for the current app session. "
        "It resets when the session state is cleared."
    )