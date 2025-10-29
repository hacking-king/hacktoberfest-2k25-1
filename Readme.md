# Hacktoberfest 2025 – Simple Python Apps

Small beginner‑friendly Python scripts you can run in the terminal. Great for first contributions during Hacktoberfest.

## What's inside
- Calculator (`Calculator App.py`): basic math operations with validation
- Chatbot (`chat.py`): rule‑based responses and helpful commands
- To‑Do (`to-do.py`): CLI to‑do list with JSON persistence and done status

## Requirements
- Python 3.8+

## How to run
From the repository root:

```bash
python3 "hacktoberfest-2k25-1/Calculator App.py"
python3 hacktoberfest-2k25-1/chat.py
python3 hacktoberfest-2k25-1/to-do.py
```

### Calculator features
- Operations: `+  -  *  /  **  %`
- Safe division by zero handling
- Input validation for numbers

### Chatbot features
- Greetings, time, date, jokes, thanks, help, and exit with `bye`
- KeyboardInterrupt friendly (Ctrl+C)

### To‑Do features
- Add tasks, toggle done, remove tasks
- Persists to `todo_data.json` automatically
