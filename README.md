# TEACHBACK

## Live Demo

🚀 **[Launch TeachBack](https://teachback.streamlit.app/)**

### Don't learn from AI. Teach it.

TeachBack is an interactive learning experience where students learn by teaching an AI learner.

Instead of simply answering questions, the student meets a learner with a misconception, identifies what went wrong, teaches the concept, and then checks whether the learner actually understood it.

**Find the mistake → Teach the concept → Test the understanding**

---

## The Idea

Most learning apps focus on giving students questions, answers, or explanations.

TeachBack takes a different approach.

The student becomes the teacher.

The learner makes a mistake, and the student has to understand the concept well enough to identify and explain that mistake.

---

## How It Works

### 01  Find the Mistake

The learner gives an incorrect explanation.

The student identifies the misconception behind it.

### 02  Teach the Learner

The student chooses the explanation that correctly addresses the misconception.

### 03  Test the Understanding

The learner encounters a new situation involving the same concept.

The student decides whether the learner has actually understood the concept.

### 04  Learning Profile

The session ends with a profile showing the student's performance across the missions.

---

## Meet the Learners

### BYTE

**The Beginner**

Curious, enthusiastic, and still building the fundamentals.

BYTE makes simpler conceptual mistakes and represents a learner who is still developing their understanding.

### NOVA

**The Confident One**

Confident, challenging, and sometimes too sure.

NOVA's mistakes are less obvious and require the student to examine the reasoning carefully.

### ECHO

**The Analytical One**

Knows the theory. Now learning to apply it.

ECHO represents a learner who understands technical ideas but can struggle when applying them to a new situation.

---

## Current Concepts

The current prototype focuses on programming concepts including:

* Python list references and copying
* Division vs. modulo
* Local variable reassignment
* Modifying objects

The learner scenarios are stored separately so the content can be expanded later.

---

## Technology

* Python
* Streamlit
* HTML/CSS
* JSON
* Streamlit Session State

---

## Project Structure

```text
TEACHBACK/
│
├── app.py
├── README.md
│
└── data/
    └── learners.json
```

`learners.json` contains the learner-related content used by the application.

---

## Application Flow

```text
BOOT
  ↓
INTRO
  ↓
MEET THE LEARNERS
  ↓
CHOOSE YOUR LEARNER
  ↓
MISSION 01
Find the Mistake
  ↓
MISSION 02
Teach the Learner
  ↓
MISSION 03
Test the Understanding
  ↓
FINAL PROFILE
```

---

## Learning Profile

At the end of a session, TeachBack generates a compact learning profile containing:

* Teaching score
* Mission-by-mission results
* Understanding status
* What the student worked on
* A short explanation of the result

The current prototype evaluates performance across three missions.

---

## Validation & Testing

The application was manually tested through the complete user flow.

Tested areas include:

* Boot and introduction screens
* Learner introductions
* Learner selection
* Mission 01
* Mission 01 feedback
* Mission 02
* Mission 02 feedback
* Mission 03
* Final learning profile
* Correct and incorrect answer handling
* Different scenarios for BYTE, NOVA, and ECHO
* Screen-to-screen navigation

Development testing also included resolving Streamlit issues involving duplicate widget IDs, session-state navigation, missing variables, and answer handling.

---

## AI Use Declaration

AI tools were used during development for:

* Debugging Python and Streamlit issues
* Reviewing implementation approaches
* Improving parts of the user experience

The final application was manually assembled, reviewed, and tested during development.

The developer is responsible for the final project concept, implementation, integration, testing, and submitted work.

---

## Limitations

The current version is a focused prototype.

It contains a limited number of concepts and three learner personalities.

The learner behavior is currently represented through predefined scenarios rather than a live generative AI model.

This keeps the current prototype predictable and allows the core learning interaction to be tested reliably.

---

## Future Improvements

Future versions could include:

* More programming concepts
* More learner personalities
* Dynamically generated misconceptions
* Adaptive difficulty
* More missions
* Progress tracking
* Personalized learning recommendations
* AI-generated learner responses
* Additional academic subjects

---

## Running Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project

```bash
cd TEACHBACK
```

### 3. Install Streamlit

```bash
pip install streamlit
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## Hackathon

Built for **CodeMyFYP HACK 26**

### Challenge

**AI for Learning**

TeachBack approaches learning through teaching: instead of asking an AI for the answer, the student has to understand a misconception well enough to help an AI learner understand the concept.

---

## Project Status

**Working prototype  ready for demonstration.**
