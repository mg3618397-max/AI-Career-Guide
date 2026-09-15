from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import sqlite3
import os

from dotenv import load_dotenv
from openai import OpenAI


# ==========================================
# CONFIGURATION
# ==========================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

app = FastAPI(
    title="AI Career Guide",
    description="AI-powered personalized career guidance system",
    version="1.0"
)


# ==========================================
# DATABASE
# ==========================================

DATABASE = "career_guide.db"


def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            education TEXT,
            skills TEXT,
            interest TEXT,
            goal TEXT,
            language TEXT
        )
    """)

    conn.commit()
    conn.close()


create_database()


# ==========================================
# DATA MODELS
# ==========================================

class StudentData(BaseModel):

    name: str
    education: str
    skills: str
    interest: str
    goal: str
    language: str = "English"


class ChatData(BaseModel):

    message: str
    language: str = "English"


# ==========================================
# CAREER KEYWORDS
# ==========================================

careers = {

    "Java Backend Developer": [
        "java",
        "spring",
        "backend",
        "developer",
        "software",
        "programming"
    ],

    "Python Developer": [
        "python",
        "programming",
        "backend",
        "developer",
        "software"
    ],

    "Data Analyst": [
        "sql",
        "excel",
        "data",
        "analytics",
        "statistics",
        "analysis"
    ],

    "AI/ML Engineer": [
        "python",
        "machine learning",
        "ai",
        "artificial intelligence",
        "deep learning",
        "data science"
    ],

    "Frontend Developer": [
        "html",
        "css",
        "javascript",
        "frontend",
        "web",
        "ui"
    ]
}


# ==========================================
# HOME
# ==========================================

@app.get("/")
def home():

    return FileResponse(
        "static/index.html"
    )


# ==========================================
# ADMIN
# ==========================================

@app.get("/admin.html")
def admin():

    return FileResponse(
        "static/admin.html"
    )


# ==========================================
# SAVE STUDENT
# ==========================================

def save_student(data: StudentData):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, education, skills, interest, goal, language)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data.name,
        data.education,
        data.skills,
        data.interest,
        data.goal,
        data.language
    ))

    conn.commit()

    conn.close()


# ==========================================
# CAREER RECOMMENDATION
# ==========================================

@app.post("/api/recommend")
def recommend(data: StudentData):

    save_student(data)

    text = (
        data.skills
        + " "
        + data.interest
        + " "
        + data.goal
    ).lower()

    scores = {}

    for career, keywords in careers.items():

        score = 0

        for keyword in keywords:

            if keyword.lower() in text:
                score += 1

        scores[career] = score


    recommended_career = max(
        scores,
        key=scores.get
    )


    best_score = scores[recommended_career]


    if best_score == 0:

        recommended_career = "Software Developer"

        reason = (
            "Your profile does not yet contain enough "
            "specific career keywords."
        )

    else:

        reason = (
            f"Your skills, interests and career goal "
            f"match the {recommended_career} path."
        )


    return {

        "success": True,

        "recommended_career":
            recommended_career,

        "reason":
            reason,

        "scores":
            scores
    }


# ==========================================
# AI CAREER GUIDANCE
# ==========================================

@app.post("/api/ai-guide")
def ai_guide(data: StudentData):

    prompt = f"""
You are an expert AI Career Guide helping college students.

Student information:

Name: {data.name}
Education: {data.education}
Current skills: {data.skills}
Interests: {data.interest}
Career goal: {data.goal}
Preferred language: {data.language}

Create personalized career guidance.

Include:

1. Recommended Career
2. Why this career suits the student
3. Skills to learn
4. Beginner to advanced roadmap
5. Tools and technologies
6. Three practical projects
7. Interview preparation
8. Job preparation
9. Common mistakes
10. Six-month action plan

Use simple language.

Answer in the preferred language.

Do not guarantee employment.
"""

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        return {
            "success": True,
            "ai_guidance": response.output_text
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# PERSONALIZED ROADMAP
# ==========================================

@app.post("/api/roadmap")
def career_roadmap(data: StudentData):

    prompt = f"""
You are a professional career roadmap planner.

Create a personalized 6-month roadmap.

Student:
Name: {data.name}
Education: {data.education}
Skills: {data.skills}
Interest: {data.interest}
Career goal: {data.goal}
Language: {data.language}

Create:

MONTH 1
- Topics
- Skills
- Practice

MONTH 2
- Topics
- Skills
- Practice

MONTH 3
- Topics
- Skills
- Practice

MONTH 4
- Topics
- Skills
- Practice

MONTH 5
- Topics
- Skills
- Practice

MONTH 6
- Topics
- Skills
- Practice

Also include:

DAILY ROUTINE
PROJECTS
INTERVIEW PREPARATION
JOB PREPARATION

Keep it practical.

Do not guarantee employment.

Answer in the preferred language.
"""

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        return {
            "success": True,
            "roadmap": response.output_text
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# SKILL GAP
# ==========================================

@app.post("/api/skill-gap")
def skill_gap(data: StudentData):

    prompt = f"""
You are an expert career skill-gap analyst.

Student:
Name: {data.name}
Education: {data.education}
Current skills: {data.skills}
Interest: {data.interest}
Target career: {data.goal}
Language: {data.language}

Analyze the difference between current skills
and skills needed for the target career.

Give:

CURRENT SKILLS

REQUIRED SKILLS

SKILL GAPS

PRIORITY
- HIGH
- MEDIUM
- LOW

WHAT TO LEARN FIRST
1.
2.
3.
4.
5.

PRACTICAL ACTION PLAN

PROJECT RECOMMENDATION

Suggest two suitable projects.

Keep it realistic and beginner-friendly.

Do not guarantee employment.

Answer in the preferred language.
"""

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        return {
            "success": True,
            "skill_gap": response.output_text
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# COURSE / RESOURCE RECOMMENDATION
# ==========================================

@app.post("/api/resources")
def resources(data: StudentData):

    prompt = f"""
You are an AI learning-resource advisor.

Student profile:

Name: {data.name}

Education:
{data.education}

Current skills:
{data.skills}

Interest:
{data.interest}

Career goal:
{data.goal}

Preferred language:
{data.language}

Recommend learning resources that can help this student
reach their career goal.

Organize the answer into:

1. SKILLS TO LEARN

2. BEGINNER RESOURCES
- Recommend free or widely accessible learning platforms.
- Explain what each resource should be used for.

3. PRACTICE RESOURCES
- Coding practice
- SQL practice
- Projects

4. PROJECT RESOURCES

5. INTERVIEW PREPARATION

6. LEARNING ORDER
Explain exactly what should be learned first, second,
third and so on.

Prefer reputable and accessible resources.

Do not invent specific course URLs.

Do not guarantee employment.

Answer in the preferred language.
"""

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        return {
            "success": True,
            "resources": response.output_text
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# AI CHATBOT
# ==========================================

@app.post("/api/chat")
def ai_chat(data: ChatData):

    prompt = f"""
You are an AI Career Guide for college students.

Student question:
{data.message}

Preferred language:
{data.language}

Answer clearly and practically.

Focus on:

- Career guidance
- Skills
- Learning roadmaps
- Projects
- Programming
- Interviews
- Jobs
- Technology

Use simple language.

If Tamil is requested, answer in Tamil.

If Hindi is requested, answer in Hindi.

Do not guarantee employment.
"""

    try:

        response = client.responses.create(
            model="gpt-5.6-luna",
            input=prompt
        )

        return {
            "success": True,
            "reply": response.output_text
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================================
# ADMIN STUDENTS
# ==========================================

@app.get("/api/students")
def get_students():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            education,
            skills,
            interest,
            goal,
            language
        FROM students
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    students = []

    for row in rows:

        students.append({

            "id": row[0],
            "name": row[1],
            "education": row[2],
            "skills": row[3],
            "interest": row[4],
            "goal": row[5],
            "language": row[6]

        })

    return {

        "success": True,
        "students": students

    }