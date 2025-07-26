# 🧠 Lesson Engine

The Lesson Engine coordinates all agents and workflows to deliver personalized language lessons with optional ASL support.

---

## 🔄 Flow Overview

The engine loads configuration from:
- `lesson_flow.yaml`: Defines the step-by-step lesson sequence.
- `lesson_engine_rules.yaml`: Contains user logic and flow triggers.

---

## ⚙️ Agent Assignment

Each step in `lesson_flow.yaml` is handled by one of the following agents:

| Step              | Agent             | Role Description                                      |
|-------------------|-------------------|--------------------------------------------------------|
| introduction      | Polyglot Professor | Greets and sets the objective                         |
| cultural_context  | Cultural Curator   | Provides cultural content                             |
| core_lesson       | Polyglot Professor | Teaches main language content                         |
| asl_support       | Silent Tongue      | Delivers ASL translation and visuals (if enabled)     |
| technical_build   | EdTech Architect   | Generates interactive or technical components         |
| review            | Polyglot Professor | Summarizes and closes the lesson                      |

---

## 🧩 Execution Logic

1. Detects user preferences (language, ASL, etc.) via `lesson_engine_rules.yaml`.
2. Loads the `lesson_flow.yaml`.
3. Activates agents in sequence per step definitions.
4. Falls back to Polyglot Professor if any agent fails or content is missing.

---

## 🔐 Access Control & Extensibility

- You can extend this engine with additional rules, agents, or step types.
- The engine can support multilingual branching, quizzes, or personalized pacing.

---

> “Language learning is not linear — this engine allows us to adapt and evolve.”
