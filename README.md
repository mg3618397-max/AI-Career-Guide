# AI Career Guide 🎓🤖

An AI-powered career guidance platform that helps students discover suitable career paths, identify skill gaps, create personalized learning roadmaps, find learning resources, and interact with an AI career assistant.

## 🌟 Overview

Many students, especially those from rural and semi-urban areas, struggle to choose the right career because they lack access to personalized career guidance.

**AI Career Guide** provides an intelligent and accessible platform where students can enter their education, skills, interests, career goals, and preferred language.

The system combines rule-based career matching with AI-powered guidance to provide personalized recommendations.

---

## 🎯 Problem Statement

Students often face challenges such as:

- Lack of personalized career guidance
- Difficulty choosing the right career path
- Limited awareness of required technical skills
- No clear learning roadmap
- Difficulty identifying skill gaps
- Lack of accessible career resources
- Limited access to mentors and career experts

---

## 💡 Our Solution

AI Career Guide acts as a virtual career mentor for students.

The platform can:

- Recommend suitable career paths
- Generate personalized AI career guidance
- Create a 6-month learning roadmap
- Analyze current skills and identify skill gaps
- Recommend learning resources
- Provide an AI-powered career chatbot
- Support multiple languages
- Store student profiles for administrative analysis

---

## ✨ Key Features

### 1. Career Recommendation

The system analyzes:

- Education
- Skills
- Interests
- Career goals

and recommends suitable career paths.

### 2. AI Career Guidance

The AI provides personalized guidance based on the student's profile.

It can explain:

- Why a career is suitable
- Required skills
- Career opportunities
- Recommended learning direction
- Practical next steps

### 3. Personalized 6-Month Roadmap

The system generates a structured learning plan covering approximately six months.

The roadmap can include:

- Monthly goals
- Technical skills
- Projects
- Practice activities
- Interview preparation

### 4. AI Skill-Gap Analysis

The system compares a student's current skills with the skills required for their target career.

It identifies:

- Current strengths
- Required skills
- Missing skills
- Priority areas
- Recommended projects
- Action plan

### 5. AI Learning Resources

Students can request personalized learning resources based on their career goals and skill gaps.

### 6. AI Career Chatbot

Students can ask career-related questions and receive AI-generated guidance in their preferred language.

### 7. Multilingual Support

The application supports:

- English
- Tamil
- Hindi

### 8. Admin Dashboard

Administrators can view stored student profiles and basic statistics.

---

## 🏗️ System Architecture

```text
                Student
                   │
                   ▼
          ┌─────────────────┐
          │   Web Interface │
          │   HTML/CSS/JS   │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │    FastAPI      │
          │    Backend      │
          └────────┬────────┘
                   │
          ┌────────┴─────────┐
          ▼                  ▼
 ┌─────────────────┐  ┌─────────────────┐
 │ Career Matching │  │   OpenAI API    │
 │   Engine        │  │   AI Services   │
 └─────────────────┘  └─────────────────┘
          │                  │
          └────────┬─────────┘
                   ▼
          ┌─────────────────┐
          │ SQLite Database │
          └─────────────────┘
